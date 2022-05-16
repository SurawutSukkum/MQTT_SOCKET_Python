import paho.mqtt.publish as publish
import paho.mqtt.subscribe as subscribe

import socket
import time

HOST_socket = '10.144.241.230'  
PORT_socket = 5432         
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST_socket, PORT_socket))
s.listen()

hostname = "10.144.241.230"
port = 1883
auth = {
 'username':' ',
 'password':' '
}
print("waiting for connection")
while True:
 connection, client_address = s.accept() 
 data = connection.recv(1024)
 if data:
   print("sending data back to the client")
   msg = subscribe.simple("data",  hostname=hostname, port=port, auth=auth)
   print("%s %s" % (msg.topic, msg.payload))
   connection.sendall(data)

  


