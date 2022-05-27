import paho.mqtt.publish as publish
import paho.mqtt.subscribe as subscribe

import socket
import time
from datetime import datetime
import json

import csv

''''''

HOST_socket = 'xx.xx.xx.xx'
PORT_socket = 5432
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST_socket, PORT_socket))
s.listen()

hostname = "xx.xx.xx.xx"
port = 1883
auth = {
    'username': ' ',
    'password': ' '
}
print("waiting for connection")

'''assembly_path = r'D:\pythonProject4\KETL_DLL.dll'
sys.path.append(assembly_path)
clr.AddReference("KETL_DLL")
from KETL_DLL import Main_Function
bc = Main_Function()
ser_num = "MDH00000001"
station_name = "MAN_HSG01"
Station_Desc = "MANUAL INSTALL COVER LABEL"
ent_time = "2020-08-11 10:10:18"
ext_time = "2020-08-11 10:11:18"
print(bc.Backcheck_Data(ser_num,station_name ))
rt_insert = bc.Insert_Process_Data(ser_num, station_name, Station_Desc, ent_time, ext_time, 1)
if rt_insert == True:
    print("insert complete!!")
else:
    print("insert does not complete!!")'''

'''from ctypes import*

libc = cdll.WinDLL("D:\pythonProject4\KETL_DLL.dll")
#libc = ctypes.WinDLL('D:/Test Object-Classification - GUI/KETL_DLL.dll')
print(libc)
ser_num = 'MDH00000001'
station_name = 'MAN_HSG01'
#Station_Desc = "MANUAL INSTALL COVER LABEL"
result1= libc.Backcheck_Data(ser_num, station_name)
print(result1)'''



while True:
    Unit = 0
    Power_supply = 0
    Tube = 0
    Filter = 0
    Label = 0
    Bag = 0
    Bag1 = 0
    Bag2 = 0
    Flag_Bag = 0
    Flag_Bag1 = 0
    Flag_Bag2 = 0
    Flag_Unit = 0
    Flag_Power_supply = 0
    Flag_Tube = 0
    Flag_Filter = 0
    Flag_Label = 0
    Flag_final_status = 0
    # current date and time

    while True:
        # connection, client_address = s.accept()
        # data = connection.recv(1024)
        # if data:

        # current date and time
        now = datetime.now()

        timestamp = datetime.fromtimestamp(datetime.timestamp(now))
        timestamp = timestamp.strftime("%d%m%Y_%H%M%S")

        file_timestamp = datetime.fromtimestamp(datetime.timestamp(now))
        file_timestamp = file_timestamp.strftime("%d%m%Y")

        print(timestamp)

        msg4 = subscribe.simple("countS", hostname=hostname, port=port, auth=auth)
        # print(" %s " % ( msg4.payload.decode("utf-8")))
        text = msg4.payload.decode("utf-8")
        print(text)
        # json string

        # parse json file
        pythonObj = json.loads(text)
        print(type(pythonObj))
        list_4 = pythonObj['DeepDetect']['obj_count_str']
        print("list_4= ",list_4)

        print("Bag =",list_4.find("Bag"))
        print("Power Supply =",list_4.find("Power Supply"))
        print("Filter =",list_4.find("Filter"))
        print("Tube =",list_4.find("Tube"))
        print("Label =",list_4.find("Label"))
        print("Unit =",list_4.find("Unit"))
        print("Bag1 =",list_4.find("Bag1"))
        print("Bag2 =",list_4.find("Bag2"))

        '''
        print(list_1)
        print(list_2)
        print(list_3)
        print(list_4)
        '''


        '''
        msg_reset = subscribe.simple("status_reset", hostname=hostname, port=port, auth=auth)
        msg_reset = msg_reset.payload.decode("utf-8")
        msg_resetlist_1 = msg_reset.split(":", 1)
        msg_resetlist_2 = ' '.join(map(str, msg_resetlist_1[1]))
        msg_resetlist_3 = msg_resetlist_2.split(" ")
        msg_resetlist_4 = msg_resetlist_3[1]
        print(msg_resetlist_4)
        '''

        if list_4.find("Power Supply") == 0:
            if Flag_Power_supply == 0:
                Flag_Power_supply = 1
                Power_supply = 1
                publish.single("capture", timestamp, hostname=hostname, port=port, auth=auth)
                publish.single("Power_supply", "OK", hostname=hostname, port=port, auth=auth)
                publish.single("time", timestamp, hostname=hostname, port=port, auth=auth)
                print(timestamp)

        if list_4.find("Bag") == 0:
            if Flag_Bag == 0:
                Flag_Bag = 1
                Bag = 1
                publish.single("capture", timestamp, hostname=hostname, port=port, auth=auth)
                publish.single("Bag", "OK", hostname=hostname, port=port, auth=auth)
                publish.single("time", timestamp, hostname=hostname, port=port, auth=auth)
                print(timestamp)

        if list_4.find("Tube") == 0:
            if Flag_Tube == 0:
                Flag_Tube = 1
                Tube = 1
                publish.single("capture", timestamp, hostname=hostname, port=port, auth=auth)
                publish.single("Tube", "OK", hostname=hostname, port=port, auth=auth)
                publish.single("time", timestamp, hostname=hostname, port=port, auth=auth)
                print(timestamp)

        if list_4.find("Filter") == 0:
            if Flag_Filter == 0:
                Flag_Filter = 1
                Filter = 1
                publish.single("capture", timestamp, hostname=hostname, port=port, auth=auth)
                publish.single("Filter", "OK", hostname=hostname, port=port, auth=auth)
                publish.single("time", timestamp, hostname=hostname, port=port, auth=auth)
                print(timestamp)

        if list_4.find("Label") == 0:
            if Flag_Label == 0:
                Flag_Label = 1
                Label = 1
                publish.single("capture", timestamp, hostname=hostname, port=port, auth=auth)
                publish.single("Label", "OK", hostname=hostname, port=port, auth=auth)
                publish.single("time", timestamp, hostname=hostname, port=port, auth=auth)
                print(timestamp)

        if list_4.find("Unit") == 0:
            if Flag_Unit == 0:
                Flag_Unit = 1
                Unit = 1
                publish.single("capture", timestamp, hostname=hostname, port=port, auth=auth)
                publish.single("Unit", "OK", hostname=hostname, port=port, auth=auth)
                publish.single("time", timestamp, hostname=hostname, port=port, auth=auth)
                print(timestamp)


        if list_4.find("Bag1") == 0:
            if Flag_Bag1 == 0:
                Flag_Bag1 = 1
                Bag1 = 1
                publish.single("capture", timestamp, hostname=hostname, port=port, auth=auth)
                publish.single("Bag1", "OK", hostname=hostname, port=port, auth=auth)
                publish.single("time", timestamp, hostname=hostname, port=port, auth=auth)
                print(timestamp)

        if list_4.find("Bag2") == 0:
            if Flag_Bag2 == 0:
                Flag_Bag2 = 1
                Bag2 = 1
                publish.single("capture", timestamp, hostname=hostname, port=port, auth=auth)
                publish.single("Bag2", "OK", hostname=hostname, port=port, auth=auth)
                publish.single("time", timestamp, hostname=hostname, port=port, auth=auth)
                print(timestamp)

        if Unit == 1:
            if Power_supply == 1 & Tube == 1 & Filter == 1 & Label == 1 & Bag == 1 & Bag1 == 1 | Bag2 == 1:
                publish.single("final_status", "OK", hostname=hostname, port=port, auth=auth)
                publish.single("time", timestamp, hostname=hostname, port=port, auth=auth)
                with open(file_timestamp+'.csv', 'a') as csv_file:
                    # test_writer = csv.writer(test_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    fieldnames = ['final_status', 'Unit', 'Power_supply', 'Tube', 'Label', 'Bag', 'Bag1', 'Bag2',
                                  'Timestamp']
                    test_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                    test_writer.writerow(
                        {'final_status': 'OK', 'Unit': Unit, 'Power_supply': Power_supply, 'Tube': Tube,
                         'Label': Label, 'Bag': Bag, 'Bag1': Bag1, 'Bag2': Bag2, 'Timestamp': timestamp})

                Unit = 0
                Power_supply = 0
                Tube = 0
                Filter = 0
                Label = 0
                Bag = 0
                Bag1 = 0
                Bag2 = 0
                Flag_Bag = 0
                Flag_Bag1 = 0
                Flag_Bag2 = 0
                Flag_Unit = 0
                Flag_Power_supply = 0
                Flag_Tube = 0
                Flag_Filter = 0
                Flag_Label = 0
                Flag_final_status = 0
                time.sleep(3)
                publish.single("Power_supply", " ", hostname=hostname, port=port, auth=auth)
                publish.single("Tube", " ", hostname=hostname, port=port, auth=auth)
                publish.single("Filter", " ", hostname=hostname, port=port, auth=auth)
                publish.single("Label", " ", hostname=hostname, port=port, auth=auth)
                publish.single("Unit", " ", hostname=hostname, port=port, auth=auth)
                publish.single("Bag", " ", hostname=hostname, port=port, auth=auth)
                publish.single("Bag1", " ", hostname=hostname, port=port, auth=auth)
                publish.single("Bag2", " ", hostname=hostname, port=port, auth=auth)
                publish.single("final_status", " ", hostname=hostname, port=port, auth=auth)
                publish.single("time", timestamp, hostname=hostname, port=port, auth=auth)
                time.sleep(3)
                print(timestamp)
            else:
                with open(file_timestamp+'.csv', 'a') as csv_file:
                    # test_writer = csv.writer(test_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    fieldnames = ['final_status', 'Unit', 'Power_supply', 'Tube', 'Label', 'Bag', 'Bag1', 'Bag2',
                                  'Timestamp']
                    test_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                    test_writer.writerow(
                        {'final_status': 'NG', 'Unit': Unit, 'Power_supply': Power_supply, 'Tube': Tube,
                         'Label': Label, 'Bag': Bag, 'Bag1': Bag1, 'Bag2': Bag2, 'Timestamp': timestamp})

                publish.single("Power_supply", " ", hostname=hostname, port=port, auth=auth)
                publish.single("Tube", " ", hostname=hostname, port=port, auth=auth)
                publish.single("Filter", " ", hostname=hostname, port=port, auth=auth)
                publish.single("Label", " ", hostname=hostname, port=port, auth=auth)
                publish.single("Unit", " ", hostname=hostname, port=port, auth=auth)
                publish.single("Bag", " ", hostname=hostname, port=port, auth=auth)
                publish.single("Bag1", " ", hostname=hostname, port=port, auth=auth)
                publish.single("Bag2", " ", hostname=hostname, port=port, auth=auth)
                publish.single("final_status", "NG", hostname=hostname, port=port, auth=auth)
                publish.single("time", timestamp, hostname=hostname, port=port, auth=auth)
                Unit = 0
                Power_supply = 0
                Tube = 0
                Filter = 0
                Label = 0
                Bag = 0
                Bag1 = 0
                Bag2 = 0
                Flag_Bag = 0
                Flag_Bag1 = 0
                Flag_Bag2 = 0
                Flag_Unit = 0
                Flag_Power_supply = 0
                Flag_Tube = 0
                Flag_Filter = 0
                Flag_Label = 0
                Flag_final_status = 0
                time.sleep(3)
                publish.single("final_status", " ", hostname=hostname, port=port, auth=auth)
                publish.single("time", timestamp, hostname=hostname, port=port, auth=auth)
                print(timestamp)
                time.sleep(3)




        if list_4 == "r":
            Unit = 0
            Power_supply = 0
            Tube = 0
            Filter = 0
            Label = 0
            Bag = 0
            Bag1 = 0
            Bag2 = 0
            Flag_Bag = 0
            Flag_Bag1 = 0
            Flag_Bag2 = 0
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
            publish.single("Bag", " ", hostname=hostname, port=port, auth=auth)
            publish.single("Bag1", " ", hostname=hostname, port=port, auth=auth)
            publish.single("Bag2", " ", hostname=hostname, port=port, auth=auth)
            publish.single("final_status", " ", hostname=hostname, port=port, auth=auth)
            publish.single("time", timestamp, hostname=hostname, port=port, auth=auth)


        if list_4 == "c":
                Unit = 0
                Power_supply = 0
                Tube = 0
                Filter = 0
                Label = 0
                Bag = 0
                Bag1 = 0
                Bag2 = 0
                Flag_Bag = 0
                Flag_Bag1 = 0
                Flag_Bag2 = 0
                Flag_Unit = 0
                Flag_Power_supply = 0
                Flag_Tube = 0
                Flag_Filter = 0
                Flag_Label = 0
                Flag_final_status = 0

                if Unit == 1 & Power_supply == 1 & Tube == 1 & Filter == 1 & Label == 1 & Bag == 1 & Bag1 == 1 & Bag2 == 1:
                    with open(file_timestamp+'.csv', 'a') as csv_file:
                        # test_writer = csv.writer(test_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                        fieldnames = ['final_status', 'Unit', 'Power_supply', 'Tube', 'Label', 'Bag', 'Bag1', 'Bag2',
                                      'Timestamp']
                        test_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                        test_writer.writerow(
                            {'final_status': 'OK', 'Unit': Unit, 'Power_supply': Power_supply, 'Tube': Tube,
                             'Label': Label, 'Bag': Bag, 'Bag1': Bag1, 'Bag2': Bag2, 'Timestamp': timestamp})
                    publish.single("final_status", "OK", hostname=hostname, port=port, auth=auth)
                    print("OK")
                    publish.single("Power_supply", " ", hostname=hostname, port=port, auth=auth)
                    publish.single("Tube", " ", hostname=hostname, port=port, auth=auth)
                    publish.single("Filter", " ", hostname=hostname, port=port, auth=auth)
                    publish.single("Label", " ", hostname=hostname, port=port, auth=auth)
                    publish.single("Unit", " ", hostname=hostname, port=port, auth=auth)
                    publish.single("Bag", " ", hostname=hostname, port=port, auth=auth)
                    publish.single("Bag1", " ", hostname=hostname, port=port, auth=auth)
                    publish.single("Bag2", " ", hostname=hostname, port=port, auth=auth)
                    publish.single("final_status", "OK", hostname=hostname, port=port, auth=auth)
                    publish.single("time", timestamp, hostname=hostname, port=port, auth=auth)
                    Unit = 0
                    Power_supply = 0
                    Tube = 0
                    Filter = 0
                    Label = 0
                    Bag = 0
                    Bag1 = 0
                    Bag2 = 0
                    Flag_Bag = 0
                    Flag_Bag1 = 0
                    Flag_Bag2 = 0
                    Flag_Unit = 0
                    Flag_Power_supply = 0
                    Flag_Tube = 0
                    Flag_Filter = 0
                    Flag_Label = 0
                    Flag_final_status = 0
                    time.sleep(3)
                    publish.single("final_status", " ", hostname=hostname, port=port, auth=auth)
                    print(timestamp)
                else:
                    with open(file_timestamp+'.csv', 'a') as csv_file:
                        # test_writer = csv.writer(test_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                        fieldnames = ['final_status', 'Unit', 'Power_supply', 'Tube', 'Label', 'Bag', 'Bag1', 'Bag2',
                                      'Timestamp']
                        test_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                        test_writer.writerow(
                            {'final_status': 'NG', 'Unit': Unit, 'Power_supply': Power_supply, 'Tube': Tube,
                             'Label': Label, 'Bag': Bag, 'Bag1': Bag1, 'Bag2': Bag2, 'Timestamp': timestamp})
                    print("NG")
                    publish.single("Power_supply", " ", hostname=hostname, port=port, auth=auth)
                    publish.single("Tube", " ", hostname=hostname, port=port, auth=auth)
                    publish.single("Filter", " ", hostname=hostname, port=port, auth=auth)
                    publish.single("Label", " ", hostname=hostname, port=port, auth=auth)
                    publish.single("Unit", " ", hostname=hostname, port=port, auth=auth)
                    publish.single("Bag", " ", hostname=hostname, port=port, auth=auth)
                    publish.single("Bag1", " ", hostname=hostname, port=port, auth=auth)
                    publish.single("Bag2", " ", hostname=hostname, port=port, auth=auth)
                    publish.single("final_status", "NG", hostname=hostname, port=port, auth=auth)
                    publish.single("time", timestamp, hostname=hostname, port=port, auth=auth)
                    Unit = 0
                    Power_supply = 0
                    Tube = 0
                    Filter = 0
                    Label = 0
                    Bag = 0
                    Bag1 = 0
                    Bag2 = 0
                    Flag_Bag = 0
                    Flag_Bag1 = 0
                    Flag_Bag2 = 0
                    Flag_Unit = 0
                    Flag_Power_supply = 0
                    Flag_Tube = 0
                    Flag_Filter = 0
                    Flag_Label = 0
                    Flag_final_status = 0
                    time.sleep(3)
                    publish.single("final_status", " ", hostname=hostname, port=port, auth=auth)
                    publish.single("time", timestamp, hostname=hostname, port=port, auth=auth)
                    print(timestamp)
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
