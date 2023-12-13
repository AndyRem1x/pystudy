import socket
import threading

HOST = "127.0.0.1"
PORT = 65432


def connection_handler(connection):
    while True:
        data = connection.recv(1024)
        if not data:
            break
        print(f"Received data: {data.decode('utf-8')}")
        print("Sending data back to the client")
        connection.sendall(data)
    connection.close()


def run_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind((HOST, PORT))
        sock.listen(1)
        print(f"Starting up on {HOST}:{PORT}")

        while True:
            print("Waiting for a connection...")
            connection, address = sock.accept()
            print(f"Accepted address: {address}")

            tread = threading.Thread(target=connection_handler, args=(connection,))

            tread.start()
            tread.join()
            print(f"Client session ended. Address: {address}")


if __name__ == "__main__":
    run_server()
