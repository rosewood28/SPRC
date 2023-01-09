import paho.mqtt.client as mqtt
from datetime import datetime
import random
from time import sleep
import json

brokerHost="127.0.0.1"

topics = ["UPB/RPI_1", "UPB/RPI_2", "SWS/T_1", "SWS/T_2"]

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+ str(rc))

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

def gen_msg(topic):
	msg = {}

	if int(topic[-1]) == 1:
		# msg["topic"] = topic
		msg["BAT"] = random.choice(list(range(60, 100)))
		msg["HUMID"] = random.choice(list(range(30, 80)))
		msg["TMP"] = random.choice(list(range(3, 28)))
		msg["status"] = "OK"
	else:
		# msg["topic"] = topic
		msg["TMP"] = random.choice(list(range(3, 28)))
		msg["timestamp"] = str(datetime.now())
	
	return msg


if __name__ == '__main__':
    client = mqtt.Client()

    print("Conecting to Broker..", brokerHost)
    client.connect(brokerHost, 1883)

    client.on_connect = on_connect
    client.on_message = on_message

    client.subscribe("#")

    client.loop_start()
    
    while True:
        topic = topics[random.choice(range(4))]
        json_msg = json.dumps(gen_msg(topic))
        
        client.publish(topic, json_msg)
        sleep(random.choice(range(5)))

    client.loop_stop()
    client.disconnect()