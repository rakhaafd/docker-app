# server.py
import socket

def start_server():
    host = "0.0.0.0"  # Bind to all interfaces
    port = 12345

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen(5)
        print(f"Server started on {host}:{port}")

        while True:
            client_socket, client_address = server_socket.accept()
            print(f"Connection from {client_address}")

            with client_socket:
                client_socket.sendall(b"Hello from server! Type something and press enter:\n")
                data = client_socket.recv(1024)
                print(f"Received from client: {data.decode('utf-8')}")
                client_socket.sendall(b"Goodbye from server!\n")

if __name__ == "__main__":
    start_server()
