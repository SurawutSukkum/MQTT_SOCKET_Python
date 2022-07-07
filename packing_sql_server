import paho.mqtt.publish as publish
import paho.mqtt.subscribe as subscribe

import socket
import time
from datetime import datetime
import json

import csv
import os.path
from pathlib import Path

import os
import webbrowser
import subprocess
''''''
import logging
import pyodbc

print("start")
# current date and time
now = datetime.now()
timestamp = datetime.fromtimestamp(datetime.timestamp(now))
timestamp = timestamp.strftime("%Y-%m-%d-%H%M%S")
logging.basicConfig(filename= timestamp +'.log', filemode='w', format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

logging.warning('This will get logged to a file')
logging.warning("start")


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
# current date and time




print("waiting for connection")
logging.warning("waiting for connection")

#proc = subprocess.Popen('node-red',shell=True, stdin=subprocess.PIPE,stdout=subprocess.PIPE)




while True:
    #subprocess.call('C:\\Windows\\System32\\cmd.exe')
    #subprocess.call('cmd node-red')
    #webbrowser.open_new('http://127.0.0.1/')
    print("node-red open")

    Unit_timeout = 0
    Bag1_timeout = 0
    Label_timeout = 0
    Tube_timeout = 0
    Filter_timeout = 0
    Power_supply_timeout = 0

    Flag_Unit_cnt = 0
    Flag_Bag_cnt = 0
    Flag_Bag1_cnt = 0
    Flag_Bag2_cnt = 0
    Flag_Label_cnt = 0
    Flag_Tube_cnt = 0
    Flag_Filter_cnt = 0
    Flag_Power_supply_cnt = 0

    Unit_file = 0
    Power_supply_file = 0
    Tube_file = 0
    Filter_file = 0
    Label_file = 0
    Bag_file = 0
    Bag1_file = 0
    Bag2_file = 0

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
    publish.single("Power_supply", " ", hostname=hostname, port=port, auth=auth)
    publish.single("Tube", " ", hostname=hostname, port=port, auth=auth)
    publish.single("Filter", " ", hostname=hostname, port=port, auth=auth)
    publish.single("Label", " ", hostname=hostname, port=port, auth=auth)
    publish.single("Unit", " ", hostname=hostname, port=port, auth=auth)
    publish.single("Bag", " ", hostname=hostname, port=port, auth=auth)
    publish.single("Bag1", " ", hostname=hostname, port=port, auth=auth)
    publish.single("Bag2", " ", hostname=hostname, port=port, auth=auth)
    publish.single("final_status", " ", hostname=hostname, port=port, auth=auth)
    publish.single("time", "", hostname=hostname, port=port, auth=auth)



    while True:
        # connection, client_address = s.accept()
        # data = connection.recv(1024)
        # if data:

        # current date and time
        now = datetime.now()

        timestamp = datetime.fromtimestamp(datetime.timestamp(now))
        timestamp = timestamp.strftime("%d%m%Y%H%M%S")

        file_timestamp = datetime.fromtimestamp(datetime.timestamp(now))
        file_timestamp = file_timestamp.strftime("%d%m%Y")
        path_to_file = file_timestamp+'.csv'
        path = Path(path_to_file)
        Serial_No = str(timestamp)
        #print(timestamp)

        if path.is_file() == False:
            with open(file_timestamp + '.csv', 'w') as csv_file:
                fieldnames = ['final_status', 'Unit', 'Unit_msg', 'Power_supply', 'Power_supply_msg', 'Tube',
                              'Tube_msg', 'Label', 'Label_msg', 'Filter', 'Filter_msg', 'Bag', 'Bag_msg', 'Bag1', 'Bag1_msg', 'Bag2',
                              'Bag2_msg',
                              'Timestamp']
                test_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                test_writer.writeheader()
                print("Create new file" + file_timestamp + '.csv')
                logging.warning("Create new file" + file_timestamp + '.csv')



        msg4 = subscribe.simple("countS", hostname=hostname, port=port, auth=auth)
        # print(" %s " % ( msg4.payload.decode("utf-8")))
        text = msg4.payload.decode("utf-8")
        #print(text)
        # json string

        # parse json file
        pythonObj = json.loads(text)
        #print(type(pythonObj))
        list_4 = pythonObj['DeepDetect']['obj_count_str']

        if Flag_Unit_cnt > 0:
            print("timeout unit ",Unit_timeout)
            logging.warning("timeout unit ")
            Unit_timeout = Unit_timeout+1
            if Unit_timeout > 100:
                Unit_timeout = 0
                Flag_Unit_cnt = 0
                publish.single("rst_obj_unit", " ", hostname=hostname, port=port, auth=auth)

        #check time out
        if Power_supply == 1:
            print("timeout Power Supply ",Power_supply_timeout)
            logging.warning("timeout Power Supply ")
            Power_supply_timeout = Power_supply_timeout+1
            if Power_supply_timeout > 2000:
                Power_supply = 0
                Power_supply_timeout = 0
                Flag_Power_supply = 0
                Flag_Power_supply_cnt = 0
                #Send to Node-red
                publish.single("Power_supply", " ", hostname=hostname, port=port, auth=auth)
                publish.single("rst_obj_Power_supply", " ", hostname=hostname, port=port, auth=auth)

        #check time out
        if Tube == 1:
            print("timeout Tube ", Tube_timeout)
            logging.warning("timeout Tube ")
            Tube_timeout = Tube_timeout+1
            if Tube_timeout > 2000:
                Tube = 0
                Tube_timeout = 0
                Flag_Tube = 0
                Flag_Tube_cnt = 0
                #Send to Node-red
                publish.single("Tube", " ", hostname=hostname, port=port, auth=auth)
                publish.single("rst_obj_Tube", " ", hostname=hostname, port=port, auth=auth)

        #check time out
        if Filter == 1:
            print("timeout Filter ", Filter_timeout)
            logging.warning("timeout Filter ")
            Filter_timeout = Filter_timeout+1
            if Filter_timeout > 2000:
                Filter = 0
                Filter_timeout = 0
                Flag_Filter = 0
                Flag_Filter_cnt = 0
                #Send to Node-red
                publish.single("Filter", " ", hostname=hostname, port=port, auth=auth)
                publish.single("rst_obj_Filter", " ", hostname=hostname, port=port, auth=auth)

        #check time out
        if Label == 1:
            print("timeout Label ", Label_timeout)
            logging.warning("timeout Label ")
            Label_timeout = Label_timeout+1
            if Label_timeout > 2000:
                Label = 0
                Label_timeout = 0
                Flag_Label = 0
                Flag_Label_cnt = 0
                # Send to Node-red
                publish.single("Label", " ", hostname=hostname, port=port, auth=auth)
                publish.single("rst_obj_Label", " ", hostname=hostname, port=port, auth=auth)

        #check time outZ
        if Bag1 == 1:
            print("timeout Bag1 ", Bag1_timeout)
            logging.warning("timeout Bag1 ")
            Bag1_timeout = Bag1_timeout+1
            if Bag1_timeout > 2000:
                Bag1 = 0
                Bag1_timeout = 0
                Flag_Bag1 = 0
                Flag_Bag1_cnt = 0
                # Send to Node-red
                publish.single("Bag1", " ", hostname=hostname, port=port, auth=auth)
                publish.single("rst_obj_Bag1", " ", hostname=hostname, port=port, auth=auth)

        if list_4.find("PowerSupply") >= 0:
            print("PowerSupply",Flag_Power_supply_cnt)
            logging.warning("PowerSupply ")

            if Flag_Power_supply_cnt < 0:
                Flag_Power_supply_cnt = Flag_Power_supply_cnt + 1
            elif Flag_Power_supply == 0 :
                Flag_Power_supply_cnt=0
                Flag_Power_supply = 1
                Power_supply = 1
                # Send to Node-red
                publish.single("Power_supply", "OK", hostname=hostname, port=port, auth=auth)
                Power_supply_file = pythonObj['ImageCapture']['file_name']
                print(Power_supply_file)
                # Send to C#
                publish.single("object", "Power_supply", hostname=hostname, port=port, auth=auth)
                publish.single("image_file", Power_supply_file, hostname=hostname, port=port, auth=auth)

        if list_4.find("Tube") >= 0:
            print("Tube",Flag_Tube_cnt)
            logging.warning("Tube ")
            if Flag_Tube_cnt < 0:
                Flag_Tube_cnt = Flag_Tube_cnt + 1
            elif Flag_Tube== 0 :
                Flag_Tube_cnt = 0
                Flag_Tube = 1
                Tube = 1
                # Send to Node-red
                publish.single("Tube", "OK", hostname=hostname, port=port, auth=auth)
                Tube_file = pythonObj['ImageCapture']['file_name']
                print(Tube_file)
                # Send to C#
                publish.single("object", "Tube", hostname=hostname, port=port, auth=auth)
                publish.single("image_file", Tube_file, hostname=hostname, port=port, auth=auth)

        if list_4.find("Filter") >= 0:
            print("Filter",Flag_Filter_cnt)
            logging.warning("Filter ")
            if Flag_Filter_cnt < 0:
                Flag_Filter_cnt = Flag_Filter_cnt + 1
            elif Flag_Filter== 0 :
                Flag_Filter_cnt = 0
                Flag_Filter = 1
                Filter = 1
                # Send to Node-red
                publish.single("Filter", "OK", hostname=hostname, port=port, auth=auth)
                Filter_file= pythonObj['ImageCapture']['file_name']
                print(Filter_file)
                # Send to C#
                publish.single("object", "Filter", hostname=hostname, port=port, auth=auth)
                publish.single("image_file", Filter_file, hostname=hostname, port=port, auth=auth)

        if list_4.find("Label") >= 0:
            print("Label",Flag_Label_cnt)
            logging.warning("Label ")
            publish.single("Label", "OK", hostname=hostname, port=port, auth=auth)
            if Flag_Label_cnt < 1:
                Flag_Label_cnt = Flag_Unit_cnt + 1
            elif Flag_Label == 0 :
                Flag_Label_cnt=0
                Flag_Label = 1
                Label = 1
                # Send to Node-red
                publish.single("Label", "OK", hostname=hostname, port=port, auth=auth)
                Label_file= pythonObj['ImageCapture']['file_name']
                print(Label_file)
                # Send to C#
                publish.single("object", "Label", hostname=hostname, port=port, auth=auth)
                publish.single("image_file", Label_file, hostname=hostname, port=port, auth=auth)

        if list_4.find("Unit") >= 0:
            print("Unit",Flag_Unit_cnt)
            logging.warning("Unit ")
            if Flag_Unit_cnt <= 1:
                Flag_Unit_cnt = Flag_Unit_cnt + 1
            elif Flag_Unit == 0 :
                Flag_Unit_cnt=0
                Flag_Unit = 1
                Unit = 1
                # Send to Node-red
                publish.single("Unit", "OK", hostname=hostname, port=port, auth=auth)
                Unit_file = pythonObj['ImageCapture']['file_name']
                print(Unit_file)
                # Send to C#
                publish.single("object", "Unit", hostname=hostname, port=port, auth=auth)
                publish.single("image_file", Unit_file, hostname=hostname, port=port, auth=auth)

        if list_4.find("Bag1") >= 0:
            print("Bag1",Flag_Bag1_cnt)
            logging.warning("Bag1 ")
            if Flag_Bag1 == 0 :
                Flag_Bag1 = 1
                Bag1 = 1
                # Send to Node-red
                publish.single("Bag1", "OK", hostname=hostname, port=port, auth=auth)
                Bag1_file = pythonObj['ImageCapture']['file_name']
                print(Bag1_file)
                # Send to C#
                publish.single("object", "Bag1", hostname=hostname, port=port, auth=auth)
                publish.single("image_file", Bag1_file, hostname=hostname, port=port, auth=auth)

        if Unit == 1:
            if Power_supply == 1 & Tube == 1 & Filter == 1 & Label == 1 & Bag1 == 1 :
                publish.single("final_status", "OK", hostname=hostname, port=port, auth=auth)
                publish.single("time", timestamp, hostname=hostname, port=port, auth=auth)
                with open(file_timestamp+'.csv', 'a') as csv_file:
                    # test_writer = csv.writer(test_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    fieldnames = ['final_status', 'Unit', 'Unit_msg', 'Power_supply', 'Power_supply_msg', 'Tube',
                                  'Tube_msg', 'Label', 'Label_msg', 'Filter', 'Filter_msg', 'Bag', 'Bag_msg', 'Bag1',
                                  'Bag1_msg', 'Bag2',
                                  'Bag2_msg',
                                  'Timestamp']
                    test_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                    test_writer.writerow(
                        {'final_status': 'OK', 'Unit': Unit,'Unit_msg':Unit_file, 'Power_supply': Power_supply,'Power_supply_msg':Power_supply_file, 'Tube': Tube,'Tube_msg':Tube_file,
                         'Label': Label, 'Label_msg':Label_file,'Filter': Filter, 'Filter_msg':Filter_file, 'Bag': Bag, 'Bag_msg':Bag_file, 'Bag1': Bag1,'Bag1_msg': Bag1_file, 'Bag2': Bag2,'Bag2_msg':Bag2_file, 'Timestamp': timestamp})




                    cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                                          "Server='';"
                                          "Database='';"
                                          "UID='';"
                                          "PWD=''!;")
                    cursor = cnxn.cursor()
                    logging.warning("Connect to SQL")
                    print("Connect to SQL")
                    logging.warning("Update OK ")
                    final_status = "OK"
                    # current date and time
                    now_sql = datetime.now()
                    timestamp_sql = datetime.fromtimestamp(datetime.timestamp(now_sql))
                    timestamp_sql = timestamp_sql.strftime("%Y-%m-%d %H:%M:%S")
                    print(timestamp_sql)
                    logging.warning('timestamp: ' + timestamp_sql)
                    count = cursor.execute("""INSERT INTO 'table name' (Serial_No, Final_status, Unit, Unit_msg, Power_supply, Power_supply_msg, Tube, Tube_msg, Label,
                            Label_msg, Filter, Filter_msg, Bag, Bag_msg, Bag1, Bag1_msg, Bag2, Bag2_msg,Timestamp) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"""
                                           , Serial_No, final_status, Unit, Unit_file, Power_supply, Power_supply_file,
                                           Tube, Tube_file, Label, Label_file, Filter, Filter_file, Bag, Bag_file, Bag1,
                                           Bag1_file, Bag2, Bag2_file, timestamp_sql).rowcount

                    cnxn.commit()
                    logging.warning('SQL save complete')
                    logging.warning('Rows inserted: ' + str(count))
                    print('Rows inserted: ' + str(count))

                Unit_timeout = 0
                Bag1_timeout = 0
                Label_timeout = 0
                Tube_timeout = 0
                Filter_timeout = 0
                Power_supply_timeout = 0

                Flag_Unit_cnt = 0
                Flag_Bag_cnt = 0
                Flag_Bag1_cnt = 0
                Flag_Bag2_cnt = 0
                Flag_Label_cnt = 0
                Flag_Tube_cnt = 0
                Flag_Filter_cnt = 0
                Flag_Power_supply_cnt = 0

                Last_file_name = 0
                Unit_file = 0
                Power_supply_file = 0
                Tube_file = 0
                Filter_file = 0
                Label_file = 0
                Bag_file = 0
                Bag1_file = 0
                Bag2_file = 0

                Unit = 0
                Power_supply = 0
                Tube = 0
                Filter = 0
                Label = 0
                Bag = 0
                Bag1 = 0
                Bag2 = 0

                Unit_msg = 0
                Tube_msg = 0
                Filter_msg = 0
                Label_msg = 0
                Power_supply_msg = 0
                Bag_msg = 0
                Bag1_msg = 0
                Bag2_msg = 0

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
                    fieldnames = ['final_status', 'Unit', 'Unit_msg', 'Power_supply', 'Power_supply_msg', 'Tube',
                                  'Tube_msg', 'Label', 'Label_msg', 'Filter', 'Filter_msg', 'Bag', 'Bag_msg', 'Bag1',
                                  'Bag1_msg', 'Bag2',
                                  'Bag2_msg',
                                  'Timestamp']
                    test_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                    test_writer.writerow(
                        {'final_status': 'NG', 'Unit': Unit,'Unit_msg':Unit_file, 'Power_supply': Power_supply,'Power_supply_msg':Power_supply_file, 'Tube': Tube,'Tube_msg':Tube_file,
                         'Label': Label, 'Label_msg':Label_file,'Filter': Filter, 'Filter_msg':Filter_file, 'Bag': Bag, 'Bag_msg':Bag_file, 'Bag1': Bag1,'Bag1_msg': Bag1_file, 'Bag2': Bag2,'Bag2_msg':Bag2_file, 'Timestamp': timestamp})
                    logging.warning("Update NG ")
                    cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                                          "Server='';"
                                          "Database='';"
                                          "UID='';"
                                          "PWD=''!;")
                    cursor = cnxn.cursor()
                    logging.warning("Connect to SQL")
                    print("Connect to SQL")
                    final_status = "NG"

                    # current date and time
                    now_sql = datetime.now()
                    timestamp_sql = datetime.fromtimestamp(datetime.timestamp(now_sql))
                    timestamp_sql = timestamp_sql.strftime("%Y-%m-%d %H:%M:%S")
                    print(timestamp_sql)
                    logging.warning('timestamp: ' + timestamp_sql)
                    count = cursor.execute("""INSERT INTO 'table name' (Serial_No, Final_status, Unit, Unit_msg, Power_supply, Power_supply_msg, Tube, Tube_msg, Label,
                            Label_msg, Filter, Filter_msg, Bag, Bag_msg, Bag1, Bag1_msg, Bag2, Bag2_msg,Timestamp) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"""
                                           , Serial_No, final_status, Unit, Unit_file, Power_supply, Power_supply_file,
                                           Tube, Tube_file, Label, Label_file, Filter, Filter_file, Bag, Bag_file, Bag1,
                                           Bag1_file, Bag2, Bag2_file, timestamp_sql).rowcount

                    cnxn.commit()
                    logging.warning('SQL save complete')
                    logging.warning('Rows inserted: ' + str(count))
                    print('Rows inserted: ' + str(count))

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

                Unit_timeout = 0
                Bag1_timeout = 0
                Label_timeout = 0
                Tube_timeout = 0
                Filter_timeout = 0
                Power_supply_timeout = 0

                Flag_Unit_cnt = 0
                Flag_Bag_cnt = 0
                Flag_Bag1_cnt = 0
                Flag_Bag2_cnt = 0
                Flag_Label_cnt = 0
                Flag_Tube_cnt = 0
                Flag_Filter_cnt = 0
                Flag_Power_supply_cnt = 0

                Last_file_name = 0
                Unit_file = 0
                Power_supply_file = 0
                Tube_file = 0
                Filter_file = 0
                Label_file = 0
                Bag_file = 0
                Bag1_file = 0
                Bag2_file = 0

                Unit = 0
                Power_supply = 0
                Tube = 0
                Filter = 0
                Label = 0
                Bag = 0
                Bag1 = 0
                Bag2 = 0

                Unit_msg = 0
                Tube_msg = 0
                Filter_msg = 0
                Label_msg = 0
                Power_supply_msg = 0
                Bag_msg = 0
                Bag1_msg = 0
                Bag2_msg = 0

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
