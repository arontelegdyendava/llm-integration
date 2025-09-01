from client.client import get_openai_client
from db.chromadb_init import search_books
from chatbot.tools import get_summary_by_title
import os

client = get_openai_client()

# Get absolute path for book summaries (for chromadb_init.py)
def get_book_summaries_path():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_dir, "..", "book_summaries", "book_summaries.txt")


# Chatbot logic
def get_book_recommendation(user_query):
    # Search vector store for relevant books
    results = search_books(user_query, top_k=1)
    # Defensive checks for None or missing keys
    docs = results.get("documents")
    ids = results.get("ids")
    if (
        not docs
        or not isinstance(docs, list)
        or not docs[0]
        or not isinstance(docs[0], list)
        or not ids
        or not isinstance(ids, list)
        or not ids[0]
        or not isinstance(ids[0], list)
    ):
        return "Sorry, I couldn't find a book matching your interests.", None, None
    recommended_summary = docs[0][0]
    recommended_title = ids[0][0]
    # Generate conversational reply using GPT
    prompt = f"A user asked: '{user_query}'. Recommend a book based on this query.\nBook: {recommended_title}\nSummary: {recommended_summary}\nReply conversationally with a recommendation."
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful librarian."},
            {"role": "user", "content": prompt},
        ],
    )
    reply = response.choices[0].message.content
    # Get full summary using the tool
    full_summary = get_summary_by_title(recommended_title)
    return reply, recommended_title, full_summary


if __name__ == "__main__":
    print("Welcome to the Smart Librarian Chatbot!")
    while True:
        user_query = input("Ask for a book recommendation (or type 'exit' to quit): ")
        if user_query.lower() == "exit":
            break
        reply, title, full_summary = get_book_recommendation(user_query)
        print("\nRecommendation:", reply)
        if title:
            print(f"(Book: {title})\n")
            print("Full Summary:", full_summary)
