#!/usr/bin/python
import sys
#import Adafruit_DHT
import paho.mqtt.client as mqtt
import time
import ssl
import logging
import os
from email.mime.text import MIMEText
from datetime import date
import smtplib
#from mail import mail

connected= False
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    global connected
    print("Connected with result code "+str(rc))
    connected = True

def on_disconnect(client, userdata, flags, rc):
    print("Disconnected with result code "+str(rc))

#logging.basicConfig()
client = mqtt.Client(client_id="pub-c-25bcc1ed-d89a-473f-9246-e7c2b6e9abfa/sub-c-a6a2a8fa-1621-11e9-9cda-0ee81137d4bc/clientid2")
#allow time to connect to io.adafruit
time.sleep(5)
#client.on_connect = on_connect
#client.on_disconnect = on_disconnect
#client.enable_logger()
#client.username_pw_set(username="dvhs_makerspace", password="6661ef63f9954314b99249cebf9d1d4f")
#client.tls_set_context()
#client.tls_set("/etc/ssl/certs/ca-certificates.crt")
#, tls_version=ssl.PROTOCOL_TLSv1_2)
try:
    print("Connecting")

    client.connect("mqtt.pndsn.com", 1883, 60)
    time.sleep(5)
except Exception as err:
    print("Could not connect" + str(err))
    exit(2)
print("Starting loop")
#client.loop_start()



#import paho.mqtt.client as mqtt
 
#publish_key = "pub-c-25bcc1ed-d89a-473f-9246-e7c2b6e9abfa"
#subscribe_key = "sub-c-a6a2a8fa-1621-11e9-9cda-0ee81137d4bc"
#client_id = "clientid2"
 
# The callback for when a PUBLISH message is received from the server.


def on_message(client, userdata, msg):
    print(str(msg.payload)[1::])
    try:
    	os.system('python mail_test.py')
    	cmd = 'afplay firestation_alarm.wav'
    	os.system(cmd)
	    
    except:
        print("error")
 
#client = mqtt.Client(client_id=publish_key + "/" + subscribe_key + "/" + client_id)
#client.connect("mqtt.pndsn.com", 1883, 60)

#def receive():
#	while True:
#		time.sleep(2)
#		if (connected):
#			
#		else:
#			print("Not yet connected")
client.on_message = on_message
client.subscribe("fire_detection")
#receive()
client.loop_forever()