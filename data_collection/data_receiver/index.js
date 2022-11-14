var SerialPort = require("serialport").SerialPort;
var Readline = require("@serialport/parser-readline").ReadlineParser;
const mqtt = require('mqtt')
const client = mqtt.connect('mqtt://localhost', {port:1883, 
            keepalive:80, 
            reconnectPeriod:1000, 
            will:{
                topic: "Node/Death",
                payload: "node disconnected",
                qos: 2
            }});

client.on('reconnect', function(){
    console.log("Attempting to reconnect");
});

client.on('connect', function(){
    console.log("Connected to broker");
});

var port = new SerialPort({
    path: 'COM9',
    baudRate: 9600,
    autoOpen: true
}, function(error){
    if (error) {
        console.log('Error: ', error.message);
      }
});

const parser = new Readline({ delimiter: '\r\n' });
port.pipe(parser);

port.open(() => {
    console.log("Port open");
});

port.on('error', (e) => {
    console.log(e);
});
parser.on('data', (data) => {
    console.log('Received Data: ' + data.toString());
    if(client.connected){
        client.publish("Device Data", data.toString(), function(error){
            console.log("Client is disconnecting " + error);
        });
    }
});

console.log("Waiting for info")


