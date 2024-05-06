# LAN Chat Application

## Team Members
- Zeyad Salah Mohamed Fathi Mohamed Moussa (120210297)

## Introduction
The project is a local chat application developed in Python. It allows two devices on the same Local Area Network (LAN) to communicate with each other. The application uses the socket and threading libraries in Python.

## Implementation

### Server
The server is implemented using Python’s socket and threading libraries. The server listens for incoming connections from clients and accepts them. Once a client is connected, a new thread is started to listen for messages from that client. When a message is received, it is broadcasted to all connected clients.

### Client
The client is also implemented using Python’s socket, threading, and tkinter libraries. The client connects to the server and sends messages. It also receives and displays messages from the server. The GUI for the client was created using tkinter.

## Test Cases

### Test Case 1: Successful Connection
**Description:** This test case verifies that a client can successfully connect to the server.

**Steps:**
1. Start the server.
2. Start the client and enter a nickname.
3. Observe that the client successfully connects to the server.

**Expected Result:** The client should successfully connect to the server.

### Test Case 2: Message Delivery
**Description:** This test case verifies that a message sent by a client is received by the server.

**Steps:**
1. Start the server.
2. Start a client and enter its nickname.
3. Send a message from the client.
4. Observe the message on the server.

**Expected Result:** The message should be received by the server and printed in the console.

### Test Case 3: Message Exchange
**Description:** This test case verifies that messages can be successfully sent and received between two clients.

**Steps:**
1. Start the server.
2. Start two clients and enter a nickname for each.
3. Send a message from one client.
4. Observe that the message is received by the other client.

**Expected Result:** The message should be successfully sent from one client and received by the other client.

### Test Case 4: Empty Message
**Description:** This test case verifies that the server can handle an empty message from a client.

**Steps:**
1. Start the server.
2. Start a client and enter a nickname.
3. Send an empty message from the client.
4. Observe the server’s behavior.

**Expected Result:** The server should ignore the empty message and not broadcast it to other clients.

### Test Case 5: Client Disconnection
**Description:** This test case verifies that the server can handle a client disconnection gracefully.

**Steps:**
1. Start the server.
2. Start two clients and enter a nickname for each.
3. Send a message from one client.
4. Disconnect one client.
5. Observe the server’s behavior.

**Expected Result:** The server should continue. The disconnected client should no longer receive messages.

## Conclusion
This project successfully implements a local chat application using Python. The application allows two devices on the same LAN to communicate with each other. The project demonstrates the use of sockets for network communication and threading for handling multiple clients simultaneously.
