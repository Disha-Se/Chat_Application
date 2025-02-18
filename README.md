# Chat_Application
---
# Chat Application with Encryption

This is a simple chat application that uses encryption for secure communication between the client and server. The server listens for incoming connections and responds to each client with an encrypted acknowledgment message. Both the client and server use **Fernet encryption** from the `cryptography` library for secure message exchange.

## Features

- **Encrypted Communication:** All messages exchanged between the client and server are encrypted using Fernet symmetric encryption.
- **Server Response:** After receiving a message from the client, the server responds with an acknowledgment.
- **Real-time Chat:** Clients can send messages, and the server responds to each client individually.

## Requirements

Before running the chat application, ensure you have the following dependencies installed:

- Python 3.x
- `cryptography` library

To install the required dependencies, run the following command:

```bash
pip install cryptography
```

## Files

- `server.py`: The server code that listens for incoming client connections and responds to them.
- `client.py`: The client code that connects to the server, sends messages, and displays server responses.
- `secret.key`: The encryption key file used for Fernet encryption (automatically generated during setup).

## Setup and Usage

### Step 1: Generate Encryption Key

Before running the server and client, you'll need to generate an encryption key. The server will use this key for encrypting and decrypting messages.

1. Open the Python shell or a script and run the following to generate the encryption key and save it to `secret.key`:

   ```python
   from cryptography.fernet import Fernet

   # Generate the key
   key = Fernet.generate_key()

   # Save the key to a file
   with open("secret.key", "wb") as key_file:
       key_file.write(key)
   ```

   This will create a `secret.key` file, which is used by both the server and client for encryption.

### Step 2: Run the Server

1. Open a terminal or command prompt.
2. Navigate to the directory where your `server.py` is located.
3. Run the server by executing the following command:

   ```bash
   python server.py
   ```

   The server will start listening for incoming connections on port `5555`.

### Step 3: Run the Client

1. Open another terminal or command prompt.
2. Navigate to the directory where your `client.py` is located.
3. Run the client by executing the following command:

   ```bash
   python client.py
   ```

   The client will connect to the server at `127.0.0.1` (localhost) on port `5555`.

### Step 4: Start Chatting

Once both the server and client are running, you can start typing messages in the client's UI. The server will acknowledge each message by sending a response, and the client will display the server's response.

- The server will only respond to the client that sent the message.
- Messages are encrypted during transmission for security.

### Example Chat Flow:

- **Client:** Sends a message, e.g., "Hello, Server!"
- **Server:** Acknowledges by replying, "Server received: Hello, Server!"
- **Client:** Displays the server's response.

## Project Structure

```
chat-app/
│
├── server.py           # Server-side chat functionality
├── client.py           # Client-side chat functionality
├── secret.key          # Encryption key (generated once)
└── README.md           # Project documentation (this file)
```

## Notes

- The application uses the `cryptography` library to implement Fernet encryption, ensuring that all messages are securely transmitted.
- The server listens for incoming client connections on port `5555`. Ensure this port is open and not being used by other applications.

## Troubleshooting

- **"Connection refused" error:** Ensure the server is running before starting the client.
- **Tkinter errors on Windows:** Make sure you're using Python 3.x with Tkinter installed. If you encounter issues with Tkinter, verify your Python installation.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
