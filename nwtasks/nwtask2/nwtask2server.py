import json
import socket

HOST = "127.0.0.1"
PORT = 65432

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print(f"starting up on {HOST} port {PORT}")
sock.bind((HOST, PORT))

sock.listen(1)


def caesar_encryption(string: str, shift: int):
    encoded_str = ""
    for char in string:
        if char.isalpha():
            if char.isupper():
                encoded_str += chr((ord(char) + shift - ord("A")) % 26 + ord("A"))
            else:
                encoded_str += chr((ord(char) + shift - ord("a")) % 26 + ord("a"))
        else:
            encoded_str += char
    return encoded_str


while True:
    print("waiting for a connection")
    connection, client_address = sock.accept()
    try:
        print("connection from", client_address)
        while True:
            data = connection.recv(1024)
            if data:
                print(f"Received data: {data}")
                data_json = json.loads(data.decode("utf-8"))
                message = data_json.get("message")
                key = data_json.get("key")

                print("Sending data back to the client")
                res_data = caesar_encryption(message, key).encode("utf-8")
                connection.sendall(res_data)

            else:
                print("No data from", client_address)
                break

    finally:
        connection.close()
