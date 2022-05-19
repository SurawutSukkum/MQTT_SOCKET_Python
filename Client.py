import paho.mqtt.publish as publish
import paho.mqtt.subscribe as subscribe

import socket
import time

HOST_socket = 'x.x.x.x'
PORT_socket = 5432
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST_socket, PORT_socket))
s.listen()

hostname = "x.x.x.x"
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
    Flag_Unit = 0
    Flag_Power_supply = 0
    Flag_Tube = 0
    Flag_Filter = 0
    Flag_Label = 0
    Flag_final_status = 0

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
        print(text)
        list_1 = text.split(":", 1)
        list_2 = ' '.join(map(str, list_1[1]))
        list_3 = list_2.split(" ")
        list_4 = list_3[1]
        print(list_4)

        '''
        msg_reset = subscribe.simple("status_reset", hostname=hostname, port=port, auth=auth)
        msg_reset = msg_reset.payload.decode("utf-8")
        msg_resetlist_1 = msg_reset.split(":", 1)
        msg_resetlist_2 = ' '.join(map(str, msg_resetlist_1[1]))
        msg_resetlist_3 = msg_resetlist_2.split(" ")
        msg_resetlist_4 = msg_resetlist_3[1]
        print(msg_resetlist_4)
        '''
        if(list_4 == "r"):
            Unit = 0
            Power_supply = 0
            Tube = 0
            Filter = 0
            Label = 0
            Flag_background = 0
            Flag_Unit = 0
            Flag_Power_supply = 0
            Flag_Tube = 0
            Flag_Filter = 0
            Flag_Label = 0
            Flag_final_status = 0
            publish.single("Power_supply", " ", hostname=hostname, port=port, auth=auth)
            publish.single("Tube", " ", hostname=hostname, port=port, auth=auth)
            publish.single("Filter", " ", hostname=hostname, port=port, auth=auth)
            publish.single("Label", " ", hostname=hostname, port=port, auth=auth)
            publish.single("Unit", " ", hostname=hostname, port=port, auth=auth)
            publish.single("final_status", " ", hostname=hostname, port=port, auth=auth)

        if list_4 == "c" :
            if  Flag_background == 0:
                Flag_background = 0
                Flag_Unit = 0
                Flag_Power_supply = 0
                Flag_Tube = 0
                Flag_Filter = 0
                Flag_Label = 0
                print("Back ground")

                Flag_final_status= 0

                if Unit == 1 & Power_supply == 1 & Tube == 1 & Filter == 1 & Label == 1:
                    publish.single("final_status", "OK", hostname=hostname, port=port, auth=auth)
                    print("OK")
                    publish.single("Power_supply", " ", hostname=hostname, port=port, auth=auth)
                    publish.single("Tube", " ", hostname=hostname, port=port, auth=auth)
                    publish.single("Filter", " ", hostname=hostname, port=port, auth=auth)
                    publish.single("Label", " ", hostname=hostname, port=port, auth=auth)
                    publish.single("Unit", " ", hostname=hostname, port=port, auth=auth)
                    Unit = 0
                    Power_supply = 0
                    Tube = 0
                    Filter = 0
                    Label = 0
                else:
                    print("NG")
                    publish.single("final_status", "NG", hostname=hostname, port=port, auth=auth)
                    publish.single("Power_supply", " ", hostname=hostname, port=port, auth=auth)
                    publish.single("Tube", " ", hostname=hostname, port=port, auth=auth)
                    publish.single("Filter", " ", hostname=hostname, port=port, auth=auth)
                    publish.single("Label", " ", hostname=hostname, port=port, auth=auth)
                    publish.single("Unit", " ", hostname=hostname, port=port, auth=auth)
                    Unit = 0
                    Power_supply = 0
                    Tube = 0
                    Filter = 0
                    Label = 0


        if list_4 == "2":
            if Flag_Power_supply == 0:
                Flag_background = 0
                Flag_Power_supply = 1
                print("Power Supply")
                Power_supply = 1
                publish.single("Power_supply", "OK", hostname=hostname, port=port, auth=auth)
        if list_4 == "3":
            if Flag_Tube == 0:
                Flag_Tube = 1
                print("Tube")
                Tube = 1
                publish.single("Tube", "OK", hostname=hostname, port=port, auth=auth)
        if list_4 == "4":
            if Flag_Filter == 0:
                Flag_Filter = 1
                print("Filter")
                Filter = 1
                publish.single("Filter", "OK", hostname=hostname, port=port, auth=auth)
        if list_4 == "5":
            if Flag_Label == 0:
                Flag_Label = 1
                print("Label")
                Label = 1
                publish.single("Label", "OK", hostname=hostname, port=port, auth=auth)
        if list_4 == "6":
            if Flag_Unit == 0:
                Flag_Unit = 1
                print("Unit")
                Unit = 1
                publish.single("Unit", "OK", hostname=hostname, port=port, auth=auth)

        '''
        if Unit == 1 & Power_supply == 1 & Tube == 1 & Filter == 1 & Label == 1:
            if Flag_final_status == 0:
                Flag_final_status= 1
                publish.single("final_status", "OK", hostname=hostname, port=port, auth=auth)
                print("OK")
                publish.single("Power_supply", " ", hostname=hostname, port=port, auth=auth)
                publish.single("Tube", " ", hostname=hostname, port=port, auth=auth)
                publish.single("Filter", " ", hostname=hostname, port=port, auth=auth)
                publish.single("Label", " ", hostname=hostname, port=port, auth=auth)
                publish.single("Unit", " ", hostname=hostname, port=port, auth=auth)
            '''
            # connection.sendall( msg.payload + msg1.payload + msg2.payload + msg3.payload)
