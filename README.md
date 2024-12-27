# Multi-Node Messaging System Using Sockets and Threading

This project implements a **multi-node communication system** where a server manages multiple nodes (clients) to send and forward messages dynamically. The server and clients are built using Python with robust logging and error handling for scalability and ease of debugging.

---

## Features
- **Dynamic Node Registration**: Nodes (clients) register with the server on connection.
- **Message Forwarding**: Clients can send messages to other nodes via the server.
- **Scalability**: Supports multiple nodes and dynamic message routing.
- **Logging**: Logs all server and client activities in separate log files (`server.log`, `client.log`).
- **Error Handling**: Handles disconnections and invalid messages gracefully.

---

## How It Works
1. **Server**:
   - Accepts client connections and registers nodes dynamically.
   - Routes messages between nodes based on the target node ID.
   - Logs all activities and handles disconnections.

2. **Client**:
   - Connects to the server and registers with a unique node ID.
   - Sends messages to target nodes via the server.
   - Listens for incoming messages.

---

## File Structure
- `server.py`: Server code to manage and route messages between clients.
- `client.py`: Client code to send and receive messages.
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
- The server automatically disconnects inactive nodes and logs the event.
- Extendable to support additional message processing or node configurations.
