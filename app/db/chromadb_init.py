import chromadb
from chromadb.config import Settings
from openai import OpenAI
import os
import logging
from dotenv import load_dotenv

load_dotenv()

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize ChromaDB client
client = chromadb.Client(Settings(persist_directory="./db/chroma_data"))

# Collection name for book summaries
collection_name = "book_summaries"

# Get absolute path for book summaries file
def get_book_summaries_path():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_dir, "..", "book_summaries", "book_summaries.txt")

# Read book summaries from file
def load_book_summaries(file_path):
    books = []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except Exception as e:
        logger.error(f"Failed to read book summaries file: {e}")
        return books
    title = None
    summary = []
    for line in lines:
        if line.startswith("## Title:"):
            if title and summary:
                books.append({"title": title, "summary": " ".join(summary).strip()})
            title = line.replace("## Title:", "").strip()
            summary = []
        elif line.strip():
            summary.append(line.strip())
    if title and summary:
        books.append({"title": title, "summary": " ".join(summary).strip()})
    return books

# Get OpenAI embeddings
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY not found in environment variables.")
openai_client = OpenAI(api_key=api_key)

def get_embedding(text):
    try:
        response = openai_client.embeddings.create(
            input=text, model="text-embedding-3-small"
        )
        return response.data[0].embedding
    except Exception as e:
        logger.error(f"Failed to get embedding from OpenAI: {e}")
        return None

# Upload to ChromaDB
books_path = get_book_summaries_path()
books = load_book_summaries(books_path)
collection = client.get_or_create_collection(collection_name)

for book in books:
    embedding = get_embedding(book["summary"])
    if embedding is None:
        logger.warning(f"Skipping book '{book['title']}' due to embedding error.")
        continue
    try:
        collection.add(
            embeddings=[embedding], documents=[book["summary"]], ids=[book["title"]]
        )
    except Exception as e:
        logger.error(f"Failed to add book '{book['title']}' to ChromaDB: {e}")

logger.info(f"Uploaded {len(books)} books to ChromaDB.")

# Semantic search retriever
def search_books(query, top_k=3):
    query_embedding = get_embedding(query)
    if query_embedding is None:
        logger.error("Query embedding failed. Returning empty results.")
        return {"documents": [[]], "ids": [[]]}
    try:
        results = collection.query(query_embeddings=[query_embedding], n_results=top_k)
        if not results or "documents" not in results or not results["documents"]:
            logger.warning("No results found or query failed.")
            return {"documents": [[]], "ids": [[]]}
        return results
    except Exception as e:
        logger.error(f"ChromaDB query failed: {e}")
        return {"documents": [[]], "ids": [[]]}

# Example usage
if __name__ == "__main__":
    results = search_books("friendship and magic")
    if results and "documents" in results and results["documents"]:
        for i, doc in enumerate(results["documents"][0]):
            print(f"Result {i + 1}: {doc}")
    else:
        print("No results found or query failed.")