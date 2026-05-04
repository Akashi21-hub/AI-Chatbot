from openai import OpenAI
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Get API key from .env
api_key = os.getenv("OPENAI_API_KEY")

# Create client
client = OpenAI(api_key=api_key)

print("🤖 Smart Chatbot Ready! Type 'exit' to stop.\n")

messages = []

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Chatbot: Goodbye 👋")
        break

    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=messages
    )

    reply = response.choices[0].message.content

    messages.append({"role": "assistant", "content": reply})

    print("Chatbot:", reply)

# from openai import OpenAI
# from dotenv import load_dotenv
# import os

# load_dotenv(dotenv_path=".env")

# api_key = os.getenv("OPENAI_API_KEY")

# # 👇 ADD THIS LINE HERE
# print("API KEY:", api_key)

# client = OpenAI(api_key=api_key)