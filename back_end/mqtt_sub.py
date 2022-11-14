from time import time
import paho.mqtt.client as mqtt
import json
import ast
import datetime
import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS, WritePrecision
import os
from dotenv import load_dotenv

load_dotenv()

bucket = os.getenv("BUCKET")
org = os.getenv("ORG")
token = os.getenv("TOKEN")
url=os.getenv("URL")

influx_client = influxdb_client.InfluxDBClient(
    url=url,
    token=token,
    org=org,
    precision=WritePrecision.S,
    debug=True
)

write_api = influx_client.write_api(write_options=SYNCHRONOUS)


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("cs462-g-02/+")


def on_disconnect(client, userdata, rc):
    print("Disconnect result code " + str(rc))


def send_door_data(payload):
    dict_payload = payload
    if isinstance(payload, dict) == False:
        dict_payload = ast.literal_eval(json.dumps(payload.decode()))
        dict_payload = ast.literal_eval(dict_payload)
        dict_payload["room"] = "room" + str(dict_payload["room"])

    if "timestamp" not in dict_payload:
        d = datetime.datetime.utcnow()
        date = d.isoformat("T") + "Z"
    
    write_api = influx_client.write_api(write_options=SYNCHRONOUS)

    point = influxdb_client.Point(dict_payload["room"]) \
            .tag("location", dict_payload["location"]) \
            .field("sound_level", int(dict_payload["sound_level"])) \
            .field("light_level", int(dict_payload["light_level"])) \
            .field("people_count", int(dict_payload["people_count"])) \
            .field("door_locking", int(dict_payload["door_locking"])) \
            .field("dist_str_in", int(dict_payload["dist_str_in"])) \
            .field("dist_str_out", int(dict_payload["dist_str_out"])) \
            .time(time=date)

    write_api.write(bucket=bucket, org=org, record=point)

def send_win_data(payload):
    dict_payload = payload
    if isinstance(payload, dict) == False:
        dict_payload = ast.literal_eval(json.dumps(payload.decode()))
        dict_payload = ast.literal_eval(dict_payload)
        dict_payload["room"] = "room" + str(dict_payload["room"])

    if "timestamp" not in dict_payload:
        d = datetime.datetime.utcnow()
        date = d.isoformat("T") + "Z"
    
    write_api = influx_client.write_api(write_options=SYNCHRONOUS)

    point = influxdb_client.Point(dict_payload["room"]) \
            .tag("location", dict_payload["location"]) \
            .field("light_level", int(dict_payload["light_level"])) \
            .field("movement", int(dict_payload["movement"])) \
            .time(time=date)

    write_api.write(bucket=bucket, org=org, record=point)

def on_message(client, userdata, message):
    if message.topic == "cs462-g-02/door":
        send_door_data(message.payload)
    elif message.topic == "cs462-g-02/window":
        send_win_data(message.payload)



client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
# connect to hivemq online
# client.connect("broker.mqttdashboard.com", 1883, 60)
client.connect("localhost", 1883, 60)
client.loop_forever(retry_first_connection=True)

