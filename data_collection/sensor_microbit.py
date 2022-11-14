from microbit import *
import radio

# configure the raio
radio.config(group=200)
radio.on()

# configure the microphone

while True:
    sound_level = microphone.sound_level()
    light_level = display.read_light_level()
    radio.send(str(sound_level)+","+str(light_level))
    sleep(1000)
