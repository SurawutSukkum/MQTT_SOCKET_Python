import socket
HOST_socket = 'xx.xx.xx.xx'  
PORT_socket = 5432
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST_socket, PORT_socket))
s.sendall(b'Hello World')
data = s.recv(1024)
print('received:', repr(data))
