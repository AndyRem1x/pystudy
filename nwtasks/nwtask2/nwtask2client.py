import json
import socket

HOST = "127.0.0.1"
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))
    sock.settimeout(5)

    is_session = True
    while is_session:
        message = input('Enter your message in English (or "exit" to quit): ')
        if message == "exit":
            print("Client session ended.")
            is_session = False
            continue
        if not message:
            continue

        key = None
        while not key:
            key_str = input(
                'Enter your secret key - a non-zero number (or "exit" to quit): '
            )
            if key_str == "exit":
                print("Client session ended.")
                is_session = False
                break
            if key_str.isdigit() and key_str != 0:
                key = int(key_str)

        if message and key:
            try:
                data = json.dumps({"message": message, "key": key})
                sock.send(data.encode("utf-8"))

                try:
                    data, server = sock.recvfrom(1024)
                    print(f'ECHO: {data.decode("utf-8")}')

                except ConnectionResetError as err:
                    print(f"Connection Error. {err}")

                except socket.timeout:
                    print("Request time out.")

            except ConnectionResetError as err:
                print(f"Connection Error. {err}")

            except Exception as err:
                print(f"Message not sent. {err}")
