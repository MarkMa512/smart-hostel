from datetime import date, datetime
from flask import Flask
import influxdb_client
from influxdb_client import InfluxDBClient
import time
import os
import logging
import datetime
import json
from dotenv import load_dotenv
from flask_cors import CORS


load_dotenv()


bucket = os.getenv("BUCKET")
org = os.getenv("ORG")
token = os.getenv("TOKEN")
url=os.getenv("URL")

client = influxdb_client.InfluxDBClient(
    url=url,
    token=token,
    org=org,
    debug=True
)


app = Flask(__name__)
CORS(app)

# pull data from here
@app.route("/get-data")
def get_data():
    # query stored data that are added into influxdb 5seconds ago
    query = 'from (bucket: bucket_name) \
        |> range(start: -5s) \
    '
    params = {
        "bucket_name": bucket
    }
   
    tables = client.query_api().query(query=query, org=org, params=params)
    return tables.to_json(indent=5)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, use_reloader=False)