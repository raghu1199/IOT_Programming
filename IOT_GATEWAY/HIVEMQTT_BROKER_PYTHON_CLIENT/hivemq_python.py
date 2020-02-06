#!/usr/bin/env python3
import mysql.connector
import paho.mqtt.client as paho
import json
from datetime import datetime
import time

mydb = mysql.connector.connect(host='localhost', user='root', password='159159', database="test_area1")
cursor = mydb.cursor()
cursor.execute("show tables")
for i in cursor:
    print(i)


def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))


def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
    print("type of incoming msg without conversion:", type(msg.payload))
    m_decode = str(msg.payload.decode("utf-8")).replace("'", '"""')
    m_in = json.loads(m_decode)
    print(type(m_in))
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
    print(d8, d9, d10, d11, d12, d13,d14,d15,d16,d17,d18)
    print(d1,d2,d3,d4,d5,d6,d7,d8)
    cursor.execute("use test_area1")
    # sql="INSERT INTO test(dt,data1,data2,data3,data4,data5,data6,data7) VALUES(%s,%s,%s,%s,%s,%s,%s,%s) "
    sql = "INSERT INTO raw_data(dt, data1, data2, data3, data4, data5, data6, data7, data8, data9, data10, data11, data12, "\
          "data13, data14,data15, data16, data17, data18, data19, data20) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, " \
          "%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s) "
    val = (dt1, d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12, d13, d14, d15, d16, d17, d18, d19, d20)
    cursor.execute(sql,val)
    print("success:")
    mydb.commit()


client = paho.Client()
client.on_subscribe = on_subscribe
client.on_message = on_message
client.connect("broker.hivemq.com", 1883)
client.subscribe("test/1", qos=2)

client.loop_forever()
