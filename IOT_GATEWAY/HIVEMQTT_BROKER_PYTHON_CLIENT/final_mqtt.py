#!/usr/bin/env python3
import mysql.connector
import paho.mqtt.client as paho
import json
from datetime import datetime
import time

mydb = mysql.connector.connect(host='103.212.121.63', user='lotusenterprises_modbus', password='HP3vB;Pu{iM#',database="lotusenterprises_modbus")
cursor1 = mydb.cursor()
cursor1.execute("show tables")
print("if no any table showing ...remote database connection error")
for i in cursor1:
    print(i)
print("Tables showing of remote database ...so connection is ok ")


def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))


def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
    print("MQTT BROKER CONNECTED..")
    mydb1 = mysql.connector.connect(host='103.212.121.63', user='lotusenterprises_modbus', password='HP3vB;Pu{iM#',database="lotusenterprises_modbus")
    cursor = mydb1.cursor()
    cursor.execute("show tables")
    print("if no any table showing ...remote database connection error")
    for i in cursor:
        print(i)
    print("Tables showing of remote database ...so connection is ok ")

    print("type of incoming msg without conversion:", type(msg.payload))
    m_decode = str(msg.payload.decode("utf-8")).replace("'", '"""')
    print("m_decode:", m_decode, " ", "type:", type(m_decode))
    m_in = json.loads(m_decode)
    now=datetime.now()
    dt2=now.strftime("%Y-%m-%d %H:%M:%S'")
    print(type(m_in))
    print(m_in)
    ts = m_in["ts"]
    dt = datetime.fromtimestamp(ts)
    dt1 = dt.strftime('%Y-%m-%d %H:%M:%S')
    print("dt1:", dt1)
    d1 = m_in["1"]["data"][0]
    d2 = m_in["1"]["data"][1]
    d3 = m_in["1"]["data"][2]
    d4 = m_in["1"]["data"][3]
    d5 = m_in["1"]["data"][4]
    d6 = m_in["1"]["data"][5]
    d7 = m_in["1"]["data"][6]
    d8 = m_in["1"]["data"][7]
    d9 = m_in["1"]["data"][8]
    d10 = m_in["1"]["data"][9]
    d11 = m_in["1"]["data"][10]
    d12 = m_in["1"]["data"][11]
    d13 = m_in["1"]["data"][12]
    d14 = m_in["1"]["data"][13]
    d15 = m_in["1"]["data"][14]
    d16 = m_in["1"]["data"][15]
    d17 = m_in["1"]["data"][16]
    d18 = m_in["1"]["data"][17]
    d19 = m_in["1"]["data"][18]
    d20 = m_in["1"]["data"][19]
    print("data sample collected:",d1, d2, d3, d4, d5, d6, d7, d8)
    print("still not dumped into database...")
    sql = "INSERT INTO MQTT_Raw_data(DateTime,Data1, Data2, Data3, Data4, Data5, Data6, Data7, Data8 ,Data9, Data10, " \
          "Data11, Data12, Data13, Data14,Data15) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, " \
                 "%s, %s, %s, %s, %s, %s, %s) "
    val = (dt1,d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12, d13, d14, d15)
    cursor.execute(sql,val)
    mydb1.commit()
    print("data dumped into datebase SUCCESS! pls check your database:")


print("msg topic :test/1 database table: MQTT_raw_data")
client = paho.Client()
client.on_subscribe = on_subscribe
client.on_message = on_message
client.connect("3.12.225.17", 1883)
client.subscribe("/STATUS/869244041774385/", qos=2)

client.loop_forever()

                                                                                                   
                                                                                                                            1,0-1         Top

