from client.client import get_openai_client
from chatbot.chatbot import get_book_recommendation
import requests

client = get_openai_client()

def generate_book_image(title, summary):
    image_prompt = f"Book cover for '{title}': {summary}"
    try:
        image_response = client.images.generate(
            prompt=image_prompt, n=1, size="512x512"
        )
        if image_response and image_response.data and image_response.data[0].url:
            image_url = image_response.data[0].url
            # Download and save image locally
            img_data = requests.get(image_url).content
            filename = f"generated_{title.replace(' ', '_')}.png"
            with open(filename, 'wb') as handler:
                handler.write(img_data)
            return filename, image_url
        else:
            print("Image generation failed or no image returned.")
            return None, None
    except Exception as e:
        print(f"Image generation failed: {e}")
        return None, None

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
            img_choice = input("Generate a book image? (y/n): ").strip().lower()
            if img_choice == 'y':
                filename, image_url = generate_book_image(title, full_summary)
                if filename:
                    print(f"Image saved as {filename}")
                    print(f"Image URL: {image_url}")
                else:
                    print("Image generation failed.")
        else:
            print("Sorry, I couldn't find a book matching your interests.")
