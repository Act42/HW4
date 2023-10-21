import socket


def client():
    host = "127.0.0.1"
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    while True:
        message = input("Введіть повідомлення: ")
        client_socket.send(message.encode('utf-8'))

    client_socket.close()


if __name__ == "__main__":
    client()