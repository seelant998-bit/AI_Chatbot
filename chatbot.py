import json
import nltk
from nltk.tokenize import word_tokenize

nltk.download("punkt")

with open("questions.json") as file:
    data = json.load(file)

print("AI Assistant: Hello! Ask me something")

while True:
    user = input("You: ").lower()

    if user == "exit":
        print("AI Assistant: Bye!")
        break

    words = word_tokenize(user)

    found = False

    for question in data:
        if question in words or question in user:
            print("AI Assistant:", data[question])
            found = True
            break

    if not found:
        print("AI Assistant: Sorry, I don't know that yet.")