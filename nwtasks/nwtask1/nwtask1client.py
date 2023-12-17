import socket

HOST = "127.0.0.1"
PORT = 65431

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    sock.settimeout(5)
    while True:
        message = input('Enter your message (or "exit" to quit): ')
        if message == "exit":
            print("Client session ended.")
            break

        try:
            message = message.encode("utf-8")
            sock.sendto(message, (HOST, PORT))
        except Exception as err:
            print(f"Message not sent! {err}")

        try:
            data, server = sock.recvfrom(1024)
            print(f'ECHO: {data.decode("utf-8")}')
            if data.decode("utf-8") == "Server stopped.":
                print("Client session ended.")
                break

        except socket.timeout:
            print("Request time out.")
