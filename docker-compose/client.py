# client.py
import socket
import time

def start_client():
    host = "server"  # Hostname server di Docker Compose
    port = 12345

    for _ in range(5):  # Coba terhubung 5 kali
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
                client_socket.connect((host, port))
                print(f"Connected to server at {host}:{port}")

                data = client_socket.recv(1024)
                print(f"Received from server: {data.decode('utf-8')}")

                client_socket.sendall(b"Hello from client!")
                data = client_socket.recv(1024)
                print(f"Received from server: {data.decode('utf-8')}")
                break
        except ConnectionRefusedError:
            print("Server not ready, retrying in 2 seconds...")
            time.sleep(2)
    else:
        print("Failed to connect to server after multiple attempts.")

if __name__ == "__main__":
    start_client()