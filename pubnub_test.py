#!/usr/bin/python
import sys, json
#import Adafruit_DHT
import paho.mqtt.client as mqtt
import time
import ssl
import logging
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
client = mqtt.Client(client_id="pub-c-25bcc1ed-d89a-473f-9246-e7c2b6e9abfa/sub-c-a6a2a8fa-1621-11e9-9cda-0ee81137d4bc/clientid1")
#allow time to connect to io.adafruit
time.sleep(5)
client.on_connect = on_connect
#client.on_disconnect = on_disconnect
#client.enable_logger()
#client.username_pw_set(username="dvhs_makerspace", password="6661ef63f9954314b99249cebf9d1d4f")
#client.tls_set_context()
#client.tls_set("/etc/ssl/certs/ca-certificates.crt")
#, tls_version=ssl.PROTOCOL_TLSv1_2)
try:
    print("Connecting")
    client.connect("mqtt.pndsn.com", 1883, 60)
except Exception as err:
    print("Could not connect" + str(err))
    exit(2)
#print("Starting loop")
#client.loop_start()


def publish(payloadVal):
    while True:
        time.sleep(2)
        if (connected):
            try:
                print("Publishing")
                client.publish( 'fire_detection',  "hello")
                break
              #  client.publish( 'dvhs_makerspace/feeds/hydro-humidity', payload=str(humidity))
              #  time.sleep(120)
            except Exception as e:
                print("Error publishing:" + str(e))
        else:
            print("Not yet connected")

client.publish( "fire_detection",  "FIRE DETECTED")
time.sleep(4)