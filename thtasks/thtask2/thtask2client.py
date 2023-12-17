import socket

HOST = "127.0.0.1"
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))
    sock.settimeout(5)
    while True:
        message = input('Enter your message (or "exit" to quit): ')
        if message == "exit":
            print("Client session ended.")
            break

        try:
            message = message.encode("utf-8")
            sock.sendall(message)

        except ConnectionError as err:
            print("Connection lost.")
            break
        except socket.timeout:
            print("Request time out.")
        except Exception as err:
            print(f"Message not sent! {err}")

        try:
            data, server = sock.recvfrom(1024)
            print(f'ECHO: {data.decode("utf-8")}')
            if data.decode("utf-8") == "Server stopped.":
                print("Client session ended.")
                break

        except ConnectionError as err:
            print("Connection lost.")
            break
        except socket.timeout:
            print("Request time out.")
        except Exception as err:
            print(f"Message not sent. {err}")
