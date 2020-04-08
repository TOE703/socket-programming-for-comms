import socket

# specify type and protocol should be TCP/IP, must match server to connect
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# ip of server to connect to (reserved for localhost)
client_socket.connect(("127.0.0.1", 8081))
print("connected")

# receiving message
incoming_data = client_socket.recv(1024)
incoming_message = incoming_data.decode()
print(incoming_message)

# sending message
outgoing_message = "hello server. i am the client"
outgoing_data = outgoing_message.encode()
client_socket.send(outgoing_data)

client_socket.close()
