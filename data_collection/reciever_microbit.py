from microbit import *
import radio

# configure the raio
radio.config(group=200)

radio.on()
while True:
    message = radio.receive()
    if message:
        print(message)
