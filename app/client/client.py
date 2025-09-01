import os
from dotenv import load_dotenv
from openai import OpenAI

def get_openai_client():
    # Load OpenAI API key from environment variable
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY not found in environment variables.")
    return OpenAI(api_key=api_key)