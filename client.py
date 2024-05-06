# Import the necessary libraries
import socket
import threading
import tkinter as tk
from tkinter import scrolledtext

# Create a socket object
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
host = "127.0.0.1"
port = 8000
my_socket.connect((host, port))

# Prompt the user to enter a nickname
nickname = input("Choose your nickname : ").strip()
while not nickname:
    nickname = input("Your nickname should not be empty : ").strip()

# Function to send a message
def send_message(event=None):  # event is passed by binders.
    # Get the message from the input field
    message_to_send = input_field.get()
    # Clear the input field
    input_field.delete(0, 'end')
    # If there is a message to send, prepend the nickname and send it
    if message_to_send:
        message_with_nickname = nickname + " : " + message_to_send
        my_socket.send(message_with_nickname.encode())

# Function to receive messages in a separate thread
def thread_receiving():
    while True:
        try:
            # Receive a message
            message = my_socket.recv(1024).decode()
            # Insert the message into the chat window
            chat_window.insert(tk.END, message + '\n')
        except OSError:  # Possibly client has left the chat.
            break

# Create the GUI
window = tk.Tk()
window.title("Chat Client")

# Create a frame for the messages
messages_frame = tk.Frame(window)
# Create an input field and bind the Return key to the send_message function
input_field = tk.Entry(messages_frame, width=50)
input_field.bind("<Return>", send_message)
input_field.pack(side=tk.LEFT, fill=tk.BOTH)
# Create a send button that calls the send_message function when clicked
send_button = tk.Button(messages_frame, text="Send", command=send_message)
send_button.pack(side=tk.LEFT, fill=tk.X)

# Pack the messages frame
messages_frame.pack(side=tk.BOTTOM, fill=tk.X)

# Create a scrolled text widget for the chat window
chat_window = scrolledtext.ScrolledText(window, wrap=tk.WORD)  # Messages are wrapped around.
chat_window.pack(side=tk.TOP, fill=tk.BOTH)

# Start the thread for receiving messages
thread_receive = threading.Thread(target=thread_receiving)
thread_receive.start()

# Start the GUI execution
tk.mainloop()  # Starts GUI execution.
