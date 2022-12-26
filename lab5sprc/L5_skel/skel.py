import paho.mqtt.client as mqtt
import time


#brokerHost="127.0.0.1" 
brokerHost="broker.hivemq.com"


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+ str(rc))

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

client = mqtt.Client()

print("Conecting to Broker..", brokerHost)
client.connect(brokerHost, 1883)

client.on_connect = on_connect
client.on_message = on_message


client.subscribe("sprc/chat/#")
client.loop_start()
while True:
	inp = input()
	client.publish("sprc/chat/StanSabina",inp)
# time.sleep(2)

client.loop_stop()
client.disconnect()

#DONE - Stan Sabina - 341C3