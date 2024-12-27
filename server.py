import socket
import logging
from threading import Thread
from collections import defaultdict

# Logging setup
logging.basicConfig(filename='server.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Server:
    def __init__(self, host='127.0.0.1', port=2004):
        self.host = host
        self.port = port
        self.nodes = defaultdict(lambda: None)  # Map of node identifiers to connections
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self):
        try:
            self.server_socket.bind((self.host, self.port))
            self.server_socket.listen(5)
            logging.info(f"Server started and listening on {self.host}:{self.port}")
            print(f"Server listening on {self.host}:{self.port}")
            self.accept_connections()
        except Exception as e:
            logging.error(f"Error starting server: {e}")
            print(f"Error: {e}")
            self.server_socket.close()

    def accept_connections(self):
        while True:
            client_socket, address = self.server_socket.accept()
            logging.info(f"Connection established with {address}")
            print(f"Connected to: {address}")
            Thread(target=self.handle_client, args=(client_socket,)).start()

    def handle_client(self, client_socket):
        try:
            # Register node
            initial_message = client_socket.recv(1024).decode('utf-8')
            node_id = initial_message.split()[-1]  # Extract node identifier
            self.nodes[node_id] = client_socket
            logging.info(f"Node '{node_id}' registered")

            client_socket.send(str.encode("Server: Connection established and node registered."))

            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                self.process_message(data.decode('utf-8'), node_id)
        except Exception as e:
            logging.error(f"Error handling client {node_id}: {e}")
        finally:
            self.disconnect_node(node_id)
            client_socket.close()

    def process_message(self, message, sender_node):
        target_node = message[-1]
        payload = message[1:-1]
        logging.info(f"Message received from {sender_node} to {target_node}: {payload}")

        if target_node in self.nodes and self.nodes[target_node]:
            self.nodes[target_node].send(str.encode(f"{sender_node}: {payload}"))
            logging.info(f"Message forwarded to {target_node}")
        else:
            logging.warning(f"Target node {target_node} is not connected")
            if self.nodes[sender_node]:
                self.nodes[sender_node].send(str.encode(f"Server: Node {target_node} is not connected."))

    def disconnect_node(self, node_id):
        if node_id in self.nodes:
            self.nodes[node_id] = None
            logging.info(f"Node '{node_id}' disconnected")
            print(f"Node '{node_id}' disconnected")

    def shutdown(self):
        self.server_socket.close()
        logging.info("Server shutdown")
        print("Server shutdown")


if __name__ == "__main__":
    server = Server(port=2004)
    try:
        server.start()
    except KeyboardInterrupt:
        server.shutdown()
