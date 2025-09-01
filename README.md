# Smart Librarian - AI Book Recommendation System

## Description
Smart Librarian is an AI-powered chatbot that recommends books based on your interests. It uses OpenAI GPT for conversational replies and ChromaDB with RAG (Retrieval-Augmented Generation) for semantic search. The system finds the best book match for your query and provides a detailed summary using a custom tool.

## Prerequisites
- Python 3.8+
- All dependencies from `requirements.txt` installed
- OpenAI API key (get one from https://platform.openai.com)

## Setup
1. **Clone the repository**
2. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```
3. **Set your OpenAI API key:**
   - Option A: In PowerShell, run:
     ```
     $env:OPENAI_API_KEY="your-openai-api-key"
     ```
   - Option B: Create a `.env` file in the project root:
     ```
     OPENAI_API_KEY=your-openai-api-key
     ```

## Running the Application
- **CLI Chatbot:**
  ```
  python app/cli_app.py
  ```
- **Streamlit Web App:**
  ```
  streamlit run app/streamlit_app.py
  ```
  (Run this from the project root folder)

## Example Questions
- I want a book about friendship and magic
- What do you recommend for someone who loves war stories?

## Troubleshooting
- If you get `ModuleNotFoundError`, make sure you run from the project root and that `__init__.py` exists in all relevant folders.
- If you get API key errors, check your environment variable or `.env` file.

---
For more details, see the assignment description in `description.txt`.
