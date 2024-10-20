from dotenv import load_dotenv
from openai import OpenAI
from openai import OpenAIError
import os

client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key=f"{os.getenv("API_KEY")}",
)

def chatWithGPT(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response
    except OpenAIError as e:
        # Handle all OpenAI API errors
        #print(f"Error: {e}")
        return f"Error: {e}"

if __name__ == "__main__":
    while True:
        user_input=input("You: ")
        if user_input.lower() in ["quit","exit","bye"]:
            break
        response=chatWithGPT(user_input)
        print("OpenAI ChatBot: " + response)