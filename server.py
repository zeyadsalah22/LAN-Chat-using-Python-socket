# Import the necessary libraries
import socket
import threading

# Create a socket object
my_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# Bind the socket to a specific address and port
port = 8000
address = "0.0.0.0"
my_socket.bind((address,port))

# Initialize an empty list to keep track of connected clients
clients = []

# Function to accept incoming client connections
def accept_clients():
    while True:
        # Listen for incoming connections
        my_socket.listen()
        # Accept a client connection and get the client object and address
        client, client_address = my_socket.accept()
        # Add the new client to the clients list
        clients.append(client)
        # Start a new thread to listen for messages from this client
        start_listening_thread(client)

# Function to start a new thread that listens for messages from a specific client
def start_listening_thread(client):
    client_thread = threading.Thread(target=listen_thread, args=(client,))
    client_thread.start()

# Function to listen for messages from a specific client
def listen_thread(client):
    while True:
        # Receive a message from the client
        message = client.recv(1024).decode()
        # If a message is received, print it and broadcast it to all clients
        if message:
            print(f"Received message : {message}")
            broadcast(message)
        # If no message is received (client disconnected), return and end the thread
        else:
            return

# Function to broadcast a message to all connected clients
def broadcast(message):
    for client in clients:
        client.send(message.encode())

# Start accepting clients
accept_clients()
