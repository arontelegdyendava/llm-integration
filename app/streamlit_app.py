import streamlit as st
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from chatbot.chatbot import get_book_recommendation
from openai import OpenAI

# Set your OpenAI API key (use environment variable for security)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "YOUR_OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

st.title("Smart Librarian Chatbot")
st.write("Ask for a book recommendation based on your interests!")

# Initialize session state variables for title and summary
if "title" not in st.session_state:
    st.session_state["title"] = None
if "full_summary" not in st.session_state:
    st.session_state["full_summary"] = None

user_query = st.text_input(
    "Enter your question:", "I want a book about friendship and magic"
)

if st.button("Get Recommendation"):
    result = get_book_recommendation(user_query)
    # Ensure result is not None and is a tuple/list with 3 elements
    if result is not None and isinstance(result, (list, tuple)) and len(result) == 3:
        reply, title, full_summary = result
        st.subheader("Recommendation:")
        st.write(reply if reply else "No reply available.")
        if title:
            st.info(f"Book: {title}")
            st.subheader("Full Summary:")
            st.write(full_summary if full_summary else "No summary available.")
            # Save title and summary to session state
            st.session_state["title"] = title
            st.session_state["full_summary"] = full_summary
        else:
            st.warning("Sorry, I couldn't find a book matching your interests.")
    else:
        st.warning("Sorry, I couldn't find a book matching your interests.")

# Show image generation button only if a valid recommendation exists
if st.session_state.get("title") and st.session_state.get("full_summary"):
    if st.button("Generate Book Image"):
        image_prompt = f"Book cover for '{st.session_state['title']}': {st.session_state['full_summary']}"
        try:
            image_response = client.images.generate(
                prompt=image_prompt, n=1, size="512x512"
            )
            if image_response and image_response.data and image_response.data[0].url:
                image_url = image_response.data[0].url
                st.image(
                    image_url,
                    caption=f"Generated image for {st.session_state['title']}",
                )
            else:
                st.error("Image generation failed or no image returned.")
        except Exception as e:
            st.error(f"Image generation failed: {e}")
