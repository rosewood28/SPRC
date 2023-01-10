import paho.mqtt.client as mqtt
from influxdb import InfluxDBClient
import json
from datetime import datetime
import os

brokerHost = "mosquitto"

def log(content):
	if os.environ.get('DEBUG_DATA_FLOW') == 'true':
		prnt = datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " " + content
		print(prnt)

def on_connect(client, userdata, flags, rc):
	print("Connected with result code "+ str(rc))
	client.subscribe("#")

def on_message(client, userdata, msg):
	# Received a message
	log('Received a message by topic [' + msg.topic + ']')

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
		timestamp_string = payload.get('timestamp')
		log('Data timestamp is: ' + timestamp_string)
	else:
		timestmp = datetime.now()
		timestamp_string = timestmp.strftime("%Y-%m-%d %H:%M:%S.%f")
		log("Data timestamp is NOW")


	db_points = []
	for k, val in payload.items():
		if type(val) in [int, float]:
			
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

			log(location + '.' + station + '.' + k + ' ' + str(val))
			db_points.append(point)

	# Add entry in database 
	if db_points:
		userdata.write_points(db_points)
		

if __name__ == '__main__':
	
	# Connect to database to send the data searies extracted from mqtt messages
	db_client = InfluxDBClient(host='database', port=8086)

	# Create database if it doesn't exists
	db_list = db_client.get_list_database()

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
	client.connect(brokerHost, 1883, 60)

	client.on_connect = on_connect
	client.on_message = on_message

	client.loop_forever()
