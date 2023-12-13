import socket

HOST = "127.0.0.1"
PORT = 65431

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    sock.bind((HOST, PORT))
    print(f"starting up on {HOST} port {PORT}")

    while True:
        try:
            message, client_address = sock.recvfrom(1024)
            print(
                f'Received message from address {client_address}: {message.decode("utf-8")}'
            )
            if not message or message.decode("UTF-8").lower() == "stop server":
                sock.sendto("Server stopped!".encode("utf-8"), client_address)
                print("Server stopped!", client_address)
                break

            print(f"Sending message back to the client address: {client_address}")
            sock.sendto(message.upper(), client_address)

        except Exception as err:
            print(f"ERROR: {err}")
