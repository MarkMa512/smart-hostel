# import relevant modules
import serial.tools.list_ports
from datetime import datetime
import sys

# initialize the serial port
ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()

# port attributes
# please find the corresponding port using find_ports.py, and store it
# in the following format in the file 'PORT_KEY':
# for macOS:
# /dev/cu.usbmodem1xxxxX
serialInst.baudrate = 115200
PORT_KEY = open("data_collection/desktop_client/PORT_KEY", 'r')
serialInst.port = PORT_KEY.read()
PORT_KEY.close()

# open the port
serialInst.open()

# create output cvs
output_csv_name = "data_collection/data/" + \
    datetime.now().strftime('%d%m%Y-%H') + "_data.csv"
create_csv = open(output_csv_name, 'w')
create_csv.close()

# read the data from the serial port
while True:
    try:
        if serialInst.inWaiting():
            output_csv = open(output_csv_name, 'a')
            packet = serialInst.readline()
            now_date = datetime.now().strftime('%d/%m/%Y')
            now_time = datetime.now().strftime('%H:%M:%S')
            line = (str(now_date) + "," + str(now_time) +
                    "," + packet.decode('utf'))
            output_csv.write(line)
            output_csv.close()
            # why we need to close on every reading is to ensure that the reading has been recorded.
    except KeyboardInterrupt:
        print("CAUGHT CTRL-C, exiting!")
        output_csv.close()
        serialInst.close()
        sys.exit(0)
