import paho.mqtt.client as mqtt
from influxdb import InfluxDBClient
import re
import json
from datetime import datetime

brokerHost = "mosquitto"

def on_connect(client, userdata, flags, rc):
	print("Connected with result code "+ str(rc))
	client.subscribe("#")

def on_message(client, userdata, msg):
	print(msg.topic+" "+str(msg.payload))
	# Received a message

	# If the message is incorrect, is ignored
	if msg.topic.count("/") != 1:
		return

	# Get location, station and payload from message
	aux_topic = msg.topic.split("/")
	location = aux_topic[0]
	station = aux_topic[1]

	payload = json.loads(msg.payload.decode())

	# Construct database entry
	if 'timestamp' in payload.keys():
		#transform received string in datetime object
		payload_string = payload.get('timestamp')
		timestmp = datetime.strptime(payload_string, "%Y-%m-%d %H:%M:%S.%f")
	else:
		timestmp = datetime.now()

	timestamp_string = timestmp.strftime("%Y-%m-%d %H:%M:%S.%f")

	db_points = []
	for k, val in payload.items():
		if type(val) in [int, float]:
			# add entry in database 
			point = {
				"measurement": station + '.' + k,
				"tags": {
					"location": location,
					"station": station
				},
				"fields": {
					"value": val
				},
				"timestamp": timestamp_string
			}

			db_points.append(point)

	if db_points:
		userdata.write_points(db_points)
		

if __name__ == '__main__':
	# Connect to database to send the data searies extracted from mqtt messages
	db_client = InfluxDBClient(host='database', port=8086)

	# Create database if it doesn't exists
	db_list = db_client.get_list_database()
	print(db_list)
	found = False
	for db in db_list:
		if db['name'] == 'tema3_db':
			found = True

	if not found:
		print("create db")
		db_client.create_database('tema3_db')

	db_client.switch_database("tema3_db")

	# Connect to mqtt broker to receive messages with measurements
	client = mqtt.Client(userdata=db_client)

	print("Conecting to Broker..", brokerHost)
	client.connect(brokerHost, 1883)

	client.on_connect = on_connect
	client.on_message = on_message

	client.loop_forever()
