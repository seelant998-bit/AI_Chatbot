import tkinter as tk
import json

with open("questions.json") as file:
    data = json.load(file)


def get_response(event=None):
    user = entry.get().lower()

    if user.strip() == "":
        return

    chat_box.insert(tk.END, "You: " + user + "\n")

    found = False

    for question in data:
        if question in user:
            chat_box.insert(
                tk.END,
                "AI Assistant: " + data[question] + "\n\n"
            )
            found = True
            break

    if not found:
        chat_box.insert(
            tk.END,
            "AI Assistant: Sorry, I don't know that yet.\n\n"
        )

    entry.delete(0, tk.END)
    chat_box.see(tk.END)


def clear_chat():
    chat_box.delete("1.0", tk.END)


window = tk.Tk()
window.title("AI Assistant Chatbot")
window.geometry("600x500")


chat_box = tk.Text(
    window,
    height=20,
    width=70
)

chat_box.pack(padx=10, pady=10)


scrollbar = tk.Scrollbar(window)

scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

scrollbar.config(command=chat_box.yview)

chat_box.config(yscrollcommand=scrollbar.set)


entry = tk.Entry(
    window,
    width=50
)

entry.pack(pady=5)

entry.bind("<Return>", get_response)


send_button = tk.Button(
    window,
    text="Send",
    command=get_response
)

send_button.pack()


clear_button = tk.Button(
    window,
    text="Clear Chat",
    command=clear_chat
)

clear_button.pack(pady=5)


window.mainloop()