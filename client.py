import socket
import threading
from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import scrolledtext

# Load the encryption key
def load_key():
    with open("secret.key", "rb") as key_file:
        return key_file.read()

key = load_key()
cipher_suite = Fernet(key)

# Global client socket
client = None

def receive_messages():
    global client
    while True:
        try:
            encrypted_msg = client.recv(1024)
            if encrypted_msg:
                message = cipher_suite.decrypt(encrypted_msg).decode()
                display_message(f"Server: {message}")
        except:
            display_message("Connection closed.")
            client.close()
            break

def send_message():
    global client
    message = message_input.get()
    if message:
        encrypted_msg = cipher_suite.encrypt(message.encode())
        client.send(encrypted_msg)
        display_message(f"You: {message}")
    message_input.delete(0, tk.END)

def display_message(message):
    chat_window.config(state=tk.NORMAL)
    chat_window.insert(tk.END, message + "\n")
    chat_window.config(state=tk.DISABLED)
    chat_window.yview(tk.END)

def start_client():
    global client
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("127.0.0.1", 5555))

    # Start the thread to receive messages from the server
    threading.Thread(target=receive_messages, daemon=True).start()

    # Run the main event loop
    root.mainloop()

# GUI setup
root = tk.Tk()
root.title("Client Chat")

# Chat window
chat_window = scrolledtext.ScrolledText(root, width=50, height=20, state=tk.DISABLED)
chat_window.pack(pady=10)

# Message input field
message_input = tk.Entry(root, width=40)
message_input.pack(pady=5)

# Send button
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(pady=5)

# Start client connection (in the main thread)
start_client()
