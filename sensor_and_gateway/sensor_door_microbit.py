from microbit import *
from machine import time_pulse_us
import radio

# configure the raio
radio.config(group=200)
radio.on()


# set up the sonar
# Reference: https://firialabs.com/blogs/lab-notes/ultrasonic-distance-sensor-with-python-and-the-micro-bit

sonar_in_trig = pin15
sonar_in_echo = pin16
sonar_in_trig.write_digital(0)
sonar_in_echo.read_digital()

sonar_out_trig = pin12
sonar_out_echo = pin13

sonar_out_trig.write_digital(0)
sonar_out_echo.read_digital()

people_count = 3
queue = []


def in_out(status):
    if (status == "I"):
        global people_count
        people_count += 1
        print("people_count + 1")
    else:
        global people_count
        people_count -= 1
        print("people_count - 1")


while True:
    # noise detection
    sound_level = microphone.sound_level()
    # light detection
    light_level = display.read_light_level()

    # door locking status: megnetic sensor on the door
    door_locking = pin0.read_digital()

    # people counting status: ultrasonic ranger
    sonar_in_trig.write_digital(1)
    sonar_in_trig.write_digital(0)

    micros_in = time_pulse_us(sonar_in_echo, 1)
    t_echo_in = micros_in / 1000000

    dist_cm_in = (t_echo_in / 2) * 34300

    dist_str_in = str(int(dist_cm_in))

    sonar_out_trig.write_digital(1)
    sonar_out_trig.write_digital(0)

    micros_out = time_pulse_us(sonar_out_echo, 1)
    t_echo_out = micros_out / 1000000

    dist_cm_out = (t_echo_out / 2) * 34300
    dist_str_out = str(int(dist_cm_out))

    if door_locking == 0:
        if (dist_cm_out < 15 and dist_cm_in >= 15):
            queue.append("I")
            sleep(1000)
            in_out(queue.pop())

        if (dist_cm_in < 15 and dist_cm_out >= 15):
            queue.append("O")
            sleep(1000)
            in_out(queue.pop())

    output_string = "1,d,"+str(light_level)+","+str(sound_level) + \
        ","+str(door_locking)+","+dist_str_in+"," + \
        dist_str_out+","+str(people_count)

    radio.send(output_string)
    sleep(1000)
