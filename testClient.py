import socket

HOST = '192.168.0.211'  # should be the same as server when on same LAN
PORT = 9090

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST, PORT))

socket.send("Hello World!".encode('utf-8'))
print(socket.recv(1024).decode('utf-8'))
