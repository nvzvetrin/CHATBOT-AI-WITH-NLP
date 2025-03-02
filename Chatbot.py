import nltk
from nltk.chat.util import Chat, reflections
import tkinter as tk
from tkinter import scrolledtext

# Define conversation patterns with responses
chat_pairs = [
    (r'hey|hello', ["Hi there! What's your name?"] ),
    (r'my name is (.*)', ["Nice to meet you, \1! How can I assist you today?"]),
    (r'(.*)how are you?', ['I’m just a chatbot, but I’m doing great! How about you?']),
    (r'what can you do?', ['I can chat with you, tell jokes, and keep you entertained!']),
    (r'(.*)your name?', ['You can call me ChatMate, your virtual assistant!']),
    (r'(.*)tell me a joke', ["Alright! Why don’t some couples go to the gym? Because some relationships don’t work out!"]),
    (r'(.*)what do you do?', ['I engage in conversations and try to make your day a little better!']),
    (r'thank you|thanks', ['You’re welcome! Let me know if you need anything else.']),
    (r'(.*)see you|goodbye', ['Goodbye! Have a great day ahead!'])
]

# Chatbot initialization
chatbot = Chat(chat_pairs, reflections)

def send_message():
    user_input = user_entry.get()
    chat_area.insert(tk.END, "You: " + user_input + "\n")
    response = chatbot.respond(user_input)
    if response:
        chat_area.insert(tk.END, "ChatMate: " + response + "\n\n")
    else:
        chat_area.insert(tk.END, "ChatMate: I'm not sure how to respond to that.\n\n")
    user_entry.delete(0, tk.END)

# Create GUI window
root = tk.Tk()
root.title("ChatMate - AI Chatbot")

chat_area = scrolledtext.ScrolledText(root, width=50, height=20, wrap=tk.WORD)
chat_area.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
chat_area.insert(tk.END, "ChatMate: Hello! What's your name?\n\n")

user_entry = tk.Entry(root, width=40)
user_entry.grid(row=1, column=0, padx=10, pady=10)

send_button = tk.Button(root, text="Send", command=send_message)
send_button.grid(row=1, column=1, padx=10, pady=10)

root.mainloop()