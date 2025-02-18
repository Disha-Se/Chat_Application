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

clients = []

def handle_client(client_socket):
    while True:
        try:
            encrypted_msg = client_socket.recv(1024)
            if not encrypted_msg:
                break

            # Decrypt and display message on the server side
            message = cipher_suite.decrypt(encrypted_msg).decode()
            print(f"Received: {message}")

            # Send response only to the client that sent the message
            response = f"Server received: {message}"
            encrypted_response = cipher_suite.encrypt(response.encode())
            client_socket.send(encrypted_response)

            # Display the received message in the server chat window
            display_message(f"Client: {message}")
            display_message(f"Server Response: {response}")

        except:
            clients.remove(client_socket)
            client_socket.close()
            break

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 5555))
    server.listen(5)
    display_message("Server is listening on port 5555...")

    while True:
        client_socket, addr = server.accept()
        display_message(f"New connection from {addr}")
        clients.append(client_socket)
        threading.Thread(target=handle_client, args=(client_socket,)).start()

# UI functions
def display_message(message):
    chat_window.config(state=tk.NORMAL)
    chat_window.insert(tk.END, message + "\n")
    chat_window.config(state=tk.DISABLED)
    chat_window.yview(tk.END)

# GUI setup
root = tk.Tk()
root.title("Server Chat")

# Chat window
chat_window = scrolledtext.ScrolledText(root, width=50, height=20, state=tk.DISABLED)
chat_window.pack(pady=10)

# Start server in a new thread
threading.Thread(target=start_server, daemon=True).start()

root.mainloop()
