from microbit import *
import radio
radio.config(group=200)
radio.on()

while True:
    light_level = display.read_light_level()
    if pin0.read_digital():
        display.show(Image.DIAMOND_SMALL)
        output_string = "1,w,"+str(light_level)+",1"
        radio.send(output_string)
        print(output_string)
    else:
        display.clear()
        output_string = "1,w,"+str(light_level)+",0"
        radio.send(output_string)
        print(output_string)
    sleep(1000)
