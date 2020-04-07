# https://www.futurelearn.com/courses/networking-with-python-socket-programming-for-communication/1/steps/688534
import socket

# AF_INET specifies IPv4 and SOCK_STREAM denotes TCP, so a TCP/IP socket is created
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind (set up) the socket to use an address and port, 0000 listens to all ips
server_socket.bind(("0.0.0.0", 8081))

# set the socket to listen for a connection to be made
server_socket.listen()
print("waiting for connection...")

# wait for a connection and accept it
connection_socket, address = server_socket.accept()
# connection_socket and is the connection to the client
# address of the client that connected, including its IP address and port
print("connected")
