import socket
import logging

# Logging setup
logging.basicConfig(filename='client.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Client:
    def __init__(self, node_id, host='127.0.0.1', port=2004):
        self.node_id = node_id
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        try:
            self.client_socket.connect((self.host, self.port))
            logging.info(f"Node '{self.node_id}' connected to server at {self.host}:{self.port}")
            self.client_socket.send(str.encode(f"This is node {self.node_id}"))
            print(f"Connected to server as node '{self.node_id}'")
        except Exception as e:
            logging.error(f"Error connecting to server: {e}")
            print(f"Error: {e}")

    def send_message(self, target_node, message):
        try:
            payload = f"{self.node_id}{message}{target_node}"
            self.client_socket.send(str.encode(payload))
            logging.info(f"Message sent to {target_node}: {message}")
        except Exception as e:
            logging.error(f"Error sending message: {e}")
            print(f"Error: {e}")

    def listen(self):
        while True:
            try:
                response = self.client_socket.recv(1024).decode('utf-8')
                if response:
                    print(f"Server: {response}")
                    logging.info(f"Message received: {response}")
            except Exception as e:
                logging.error(f"Error receiving message: {e}")
                break

    def run(self):
        self.connect()
        while True:
            command = input("Enter 'm' to send a message or 'q' to quit: ").strip().lower()
            if command == 'm':
                target_node = input("Enter target node (e.g., a, b, c): ").strip().lower()
                message = input("Enter your message: ").strip()
                self.send_message(target_node, message)
            elif command == 'q':
                print("Disconnecting...")
                self.client_socket.close()
                break
            else:
                print("Invalid command. Try again.")


if __name__ == "__main__":
    client_node = input("Enter your node ID (e.g., a, b, c): ").strip().lower()
    client = Client(node_id=client_node, port=2004)
    client.run()
