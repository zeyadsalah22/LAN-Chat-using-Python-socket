# LAN Chat Application

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

[![LAN Chat 1](https://github.com/zeyadsalah22/LAN-Chat-using-Python-socket/blob/main/images/lanchat1.png)](https://github.com/zeyadsalah22/LAN-Chat-using-Python-socket/blob/main/images/lanchat1.png)

In this case, clicking on the image in the rendered Markdown will take you to the image URL. I hope this helps! If you need any more assistance, feel free to ask. 😊

### Test Case 2: Message Delivery
**Description:** This test case verifies that a message sent by a client is received by the server.

**Steps:**
1. Start the server.
2. Start a client and enter its nickname.
3. Send a message from the client.
4. Observe the message on the server.

**Expected Result:** The message should be received by the server and printed in the console.

I see, you want to display the image and also have it link to the source. You can do this by combining the Markdown syntax for images and links. Here's how you can do it:

[![LAN Chat 2](https://github.com/zeyadsalah22/LAN-Chat-using-Python-socket/blob/main/images/lanchat2.png)](https://github.com/zeyadsalah22/LAN-Chat-using-Python-socket/blob/main/images/lanchat2.png)

In this case, clicking on the image in the rendered Markdown will take you to the image URL. I hope this helps! If you need any more assistance, feel free to ask. 😊

### Test Case 3: Message Exchange
**Description:** This test case verifies that messages can be successfully sent and received between two clients.

**Steps:**
1. Start the server.
2. Start two clients and enter a nickname for each.
3. Send a message from one client.
4. Observe that the message is received by the other client.

**Expected Result:** The message should be successfully sent from one client and received by the other client.

[![LAN Chat 3](https://github.com/zeyadsalah22/LAN-Chat-using-Python-socket/blob/main/images/lanchat3.png)](https://github.com/zeyadsalah22/LAN-Chat-using-Python-socket/blob/main/images/lanchat3.png)


### Test Case 4: Empty Message
**Description:** This test case verifies that the server can handle an empty message from a client.

**Steps:**
1. Start the server.
2. Start a client and enter a nickname.
3. Send an empty message from the client.
4. Observe the server’s behavior.

**Expected Result:** The server should ignore the empty message and not broadcast it to other clients.

[![LAN Chat 4](https://github.com/zeyadsalah22/LAN-Chat-using-Python-socket/blob/main/images/lanchat4.png)](https://github.com/zeyadsalah22/LAN-Chat-using-Python-socket/blob/main/images/lanchat4.png)


### Test Case 5: Client Disconnection
**Description:** This test case verifies that the server can handle a client disconnection gracefully.

**Steps:**
1. Start the server.
2. Start two clients and enter a nickname for each.
3. Send a message from one client.
4. Disconnect one client.
5. Observe the server’s behavior.

**Expected Result:** The server should continue. The disconnected client should no longer receive messages.

[![LAN Chat 5](https://github.com/zeyadsalah22/LAN-Chat-using-Python-socket/blob/main/images/lanchat5.png)](https://github.com/zeyadsalah22/LAN-Chat-using-Python-socket/blob/main/images/lanchat5.png)

[![LAN Chat 6](https://github.com/zeyadsalah22/LAN-Chat-using-Python-socket/blob/main/images/lanchat6.png)](https://github.com/zeyadsalah22/LAN-Chat-using-Python-socket/blob/main/images/lanchat6.png)


## Conclusion
This project successfully implements a local chat application using Python. The application allows two devices on the same LAN to communicate with each other. The project demonstrates the use of sockets for network communication and threading for handling multiple clients simultaneously.
