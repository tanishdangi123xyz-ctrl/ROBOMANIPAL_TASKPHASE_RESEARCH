import os
from google import genai

def llm():
    inp = input("Please enter your prompt: ")
    key = os.environ.get("GEMAPI")
    if not key:
        print("Key not set")
        return

    client = genai.Client(api_key=key)
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=inp
        )
        print("\nLLM Response:")
        print(response.text)

    except Exception as e:
        print(f"An API error occurred: {e}")

if __name__ == "__main__":
    llm()