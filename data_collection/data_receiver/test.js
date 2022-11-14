var serialport = require("serialport").SerialPort;

serialport.list().then(function (ports) {
  ports.forEach(function(port) {
    //please look at 'path'
    console.log(port);
  });
});