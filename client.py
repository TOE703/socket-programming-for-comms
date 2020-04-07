import socket

# specify type and protocol should be TCP/IP, must match server to connect
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# ip of server to connect to (reserved for localhost)
client_socket.connect(("127.0.0.1", 8081))
print("connected")
