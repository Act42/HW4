import socket

def server():
    host = "127.0.0.1"
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print("Очікування підключення...")
    conn, addr = server_socket.accept()
    print(f"З'єднано з {addr[0]}:{addr[1]}")

    while True:
        data = conn.recv(1024).decode('utf-8')
        if not data:
            break
        print(f"Користувач: {data}")

    conn.close()

if __name__ == "__main__":
    server()
