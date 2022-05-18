import paho.mqtt.publish as publish
import paho.mqtt.subscribe as subscribe

import socket
import time

HOST_socket = 'xx.xx.xx.xx'
PORT_socket = 5432
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST_socket, PORT_socket))
s.listen()

hostname = 'xx.xx.xx.xx'
port = 1883
auth = {
    'username': ' ',
    'password': ' '
}
print("waiting for connection")

while True:
    Unit = 0
    Power_supply = 0
    Tube = 0
    Filter = 0
    Label = 0
    Flag_background = 0
    while True:
        # connection, client_address = s.accept()
        # data = connection.recv(1024)
        # if data:
        '''
        print("sending data back to the client")
        msg = subscribe.simple("data", hostname=hostname, port=port, auth=auth)
        print("%s %s " % (msg.topic, msg.payload))
        msg1 = subscribe.simple("time", hostname=hostname, port=port, auth=auth)
        print("%s %s " % (msg1.topic, msg1.payload))
        msg2 = subscribe.simple("status_data", hostname=hostname, port=port, auth=auth)
        print("%s %s " % (msg2.topic, msg2.payload))
        msg3 = subscribe.simple("image", hostname=hostname, port=port, auth=auth)
        print("%s %s " % (msg3.topic, msg3.payload))
        '''
        msg4 = subscribe.simple("countS", hostname=hostname, port=port, auth=auth)
        # print(" %s " % ( msg4.payload.decode("utf-8")))
        text = msg4.payload.decode("utf-8")
        # print(text)
        list_1 = text.split(":", 1)
        list_2 = ' '.join(map(str, list_1[1]))
        list_3 = list_2.split(" ")
        list_4 = list_3[1]
        # print(list_4)

        if list_4 == "0" :
            if  Flag_background == 0:
                Flag_background = 1
                print("Back ground")
                Unit = 0
                Power_supply = 0
                Tube = 0
                Filter = 0
                Label = 0
                publish.single("Power_supply", "OK", hostname=hostname, port=port, auth=auth)
                publish.single("Tube", "OK", hostname=hostname, port=port, auth=auth)
                publish.single("Filter", "OK", hostname=hostname, port=port, auth=auth)
                publish.single("Label", "OK", hostname=hostname, port=port, auth=auth)
                publish.single("Unit", "OK", hostname=hostname, port=port, auth=auth)

                if Unit == 1 & Power_supply == 1 & Tube == 1 & Filter == 1 & Label == 1:
                    publish.single("final_status", "OK", hostname=hostname, port=port, auth=auth)
                    print("OK")
                else:
                    print("NG")
                    publish.single("final_status", "NG", hostname=hostname, port=port, auth=auth)


                publish.single("Power_supply", " ", hostname=hostname, port=port, auth=auth)
                publish.single("Tube", " ", hostname=hostname, port=port, auth=auth)
                publish.single("Filter", " ", hostname=hostname, port=port, auth=auth)
                publish.single("Label", " ", hostname=hostname, port=port, auth=auth)
                publish.single("Unit", " ", hostname=hostname, port=port, auth=auth)
                publish.single("final_status", " ", hostname=hostname, port=port, auth=auth)

        if list_4 == "2":
            Flag_background = 0
            print("Power Supply")
            Power_supply = 1
            publish.single("Power_supply", "OK", hostname=hostname, port=port, auth=auth)
        if list_4 == "3":
            print("Tube")
            Tube = 1
            publish.single("Tube", "OK", hostname=hostname, port=port, auth=auth)
        if list_4 == "4":
            print("Filter")
            Filter = 1
            publish.single("Filter", "OK", hostname=hostname, port=port, auth=auth)
        if list_4 == "5":
            print("Label")
            Label = 1
            publish.single("Label", "OK", hostname=hostname, port=port, auth=auth)
        if list_4 == "6":
            print("Unit")
            Unit = 1
            publish.single("Unit", "OK", hostname=hostname, port=port, auth=auth)


            # connection.sendall( msg.payload + msg1.payload + msg2.payload + msg3.payload)
