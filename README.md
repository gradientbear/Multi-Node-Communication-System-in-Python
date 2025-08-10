# Multi-Node Messaging System Using Sockets and Threading

---

## Project Overview

This project implements a **multi-node messaging system** enabling dynamic communication between multiple clients (nodes) via a centralized server. Built with Python, the system leverages sockets and threading for concurrent client management, robust logging, and comprehensive error handling to ensure scalability and reliability.

---

## Features

- **Dynamic Node Registration:** Clients register with the server upon connection using unique node IDs.  
- **Message Forwarding:** Enables clients to send messages to any connected node through the server.  
- **Scalable Architecture:** Supports multiple simultaneous nodes with dynamic message routing.  
- **Comprehensive Logging:** Server and client activities are logged separately (`server.log` and `client.log`).  
- **Robust Error Handling:** Gracefully manages disconnections, invalid messages, and other edge cases.

---

## System Architecture

### Server
- Listens for incoming client connections.  
- Registers nodes dynamically with their unique IDs.  
- Routes messages from source clients to designated target nodes.  
- Logs all activities and manages client disconnections.

### Client
- Connects to the server and registers with a chosen node ID.  
- Sends messages to other nodes via the server.  
- Listens for and displays incoming messages from other clients.

---

## Repository Structure

- `server.py` — Server implementation handling client management and message routing.  
- `client.py` — Client implementation for sending and receiving messages.

---

## Setup & Usage

### Step 1: Start the Server
Run the server to listen for client connections.
```bash
python server.py
```

### Step 2: Connect Clients
Run the client code and register each client with a unique node ID.
```bash
python client.py
```
Follow the prompts to enter the node ID (e.g., `a`, `b`, `c`).

### Step 3: Send Messages
1. On the client, enter `m` to send a message.
2. Provide the target node ID (e.g., `a`, `b`, `c`).
3. Enter the message content.
4. The message is routed to the target node.

### Step 4: Quit
Enter `q` to disconnect the client.

---

## Example Workflow
1. **Server**: Start the server:
   ```bash
   python server.py
   ```
   Output:
   ```
   Server listening on 127.0.0.1:2004
   ```

2. **Client A**: Connect as `a`:
   ```bash
   python client.py
   ```
   Output:
   ```
   Connected to server as node 'a'
   ```

3. **Client B**: Connect as `b`:
   ```bash
   python client.py
   ```
   Output:
   ```
   Connected to server as node 'b'
   ```

4. **Message Sending**: From Client A to Client B:
   - Client A:
     ```
     Enter 'm' to send a message or 'q' to quit: m
     Enter target node (e.g., a, b, c): b
     Enter your message: Hello from A
     ```
   - Client B receives:
     ```
     Server: a: Hello from A
     ```

---
## Notes
- The server monitors and disconnects inactive clients automatically, logging all relevant events.
- The system can be extended with additional features such as encrypted messaging, authentication, or advanced routing logic.
