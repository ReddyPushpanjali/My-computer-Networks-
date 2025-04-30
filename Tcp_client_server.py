import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 12345))
server.listen(1)
print("Server is listening on port 12345...")

conn, addr = server.accept()
print(f"Connected to {addr}")

while True:
    data = conn.recv(1024).decode()
    if not data:
        break
    print(f"Client says: {data}")
    conn.send("Message received".encode())

conn.close()
