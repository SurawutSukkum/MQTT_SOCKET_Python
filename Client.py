import paho.mqtt.publish as publish
import paho.mqtt.subscribe as subscribe

import socket
import time

HOST_socket = 'xxx.xxx.xxx.xxx'
PORT_socket = 5432
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST_socket, PORT_socket))
s.listen()

hostname = "10.144.241.230"
port = 1883
auth = {
    'username': ' ',
    'password': ' '
}
print("waiting for connection")
while True:
    connection, client_address = s.accept()
    data = connection.recv(1024)
    if data:
        print("sending data back to the client")
        msg = subscribe.simple("data", hostname=hostname, port=port, auth=auth)
        msg1 = subscribe.simple("time", hostname=hostname, port=port, auth=auth)
        msg2 = subscribe.simple("status_data", hostname=hostname, port=port, auth=auth)
        msg3 = subscribe.simple("image", hostname=hostname, port=port, auth=auth)
        print("%s %s %s %s %s %s %s %s" % (msg.topic, msg.payload,msg1.topic, msg1.payload,msg2.topic, msg2.payload, msg3.topic, msg3.payload))
        connection.sendall( msg.payload + msg1.payload + msg2.payload + msg3.payload)




