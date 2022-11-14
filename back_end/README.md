# Back End Application

## Installation Guide
1. Install the required dependencies: 
```
pip install -r requirement.txt
```
or 

```
pip install influxdb-client 
pip install paho-mqtt 
```

2. Download influxdb
https://portal.influxdata.com/downloads/
- platform: windows binaries
- use powershell to run the download
- unzip the file 
- under the file run command: `./influxd` after you have navigate to the folder containing influxd.exe
- open `localhost:8086` in your browser
- sign up an account (make sure you put organisation as "local")
- generate API token -> all access api token
- bucket: iot_test8 (create bucket, and name it as iot_test8)
- org: local
- put your token into environmental file '.env' in the mqtt_sub folder, you should have something like this:
    ```
    BUCKET=iot_test8
    ORG=local
    TOKEN= [input your api token here]
    URL=http://localhost:8086
    ```

3. Download [Mosquito](https://mosquitto.org/download/) (for testing)
- in terminal w/admin rights: 
    ```
    net start mosquitto
    ```

4. flask run in seperate terminals
```
python app.py
```
```
python mqtt_sub.py 
```

5. [MQTT Explorer](http://mqtt-explorer.com/)
Use the mqtt explorer to do publish mock data
- host name change to localhost, connect 
- publish the following data as dummy data:
    - topic: `cs462-g-02/window`
    - json:
    ```
        {
            "room" : "1",
            "location" : "window",
            "light_level": 1,
            "movement" : 3
        }
    ```

    - topic: `cs462-g-02/door`
    - json:
    ```
        {
            "room" : "1",
            "location": "door",
            "light_level": 1,
            "sound_level": 2,
            "movement": 3,
            "people_count": 3,
            "door_locking": 1,
            "dist_str_in": 4,
            "dist_str_out": 2
        }
    ```

6. get json
visit `localhost:5000/get-data` on your browser, it should return a json list 



