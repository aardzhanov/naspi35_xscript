#!/usr/bin/python3

import RPi.GPIO as IO
import time
import subprocess
import logging

servo = 18
logging.basicConfig(format='%(message)s', level=logging.DEBUG)
IO.setwarnings(False)
IO.setmode (IO.BCM)
IO.setup(servo,IO.OUT)
fan = IO.PWM(servo,2000)
fan.start(0)

def get_temp():
    output = subprocess.run(['cat', '/sys/class/thermal/thermal_zone0/temp'], capture_output=True)
    temp_str = output.stdout.decode()
    try:
        return float(temp_str)/1000
    except (IndexError, ValueError):
        raise RuntimeError('Could not get temperature')

while 1:
    temp = get_temp()                        # Get the current CPU temperature
    if temp > 60:                            # Check temperature threshhold, in degrees celcius
        fan.ChangeDutyCycle(100)             # Set fan duty based on temperature, 100 is max speed and 0 is min speed or off.
        logging.debug("Temp: %d, speed: 100", temp)
    elif temp > 50:
        fan.ChangeDutyCycle(90)
        logging.debug("Temp: %d, speed: 90", temp)
    elif temp > 40:
        fan.ChangeDutyCycle(85)
        logging.debug("Temp: %d, speed: 85", temp)
    elif temp > 30:
        fan.ChangeDutyCycle(70)
        logging.debug("Temp: %d, speed: 70", temp)
    elif temp > 25:
        fan.ChangeDutyCycle(60)
        logging.debug("Temp: %d, speed: 60", temp)
    else:
        fan.ChangeDutyCycle(0)
        logging.debug("Temp: %d, speed: 0", temp)
    time.sleep(5)                            # Sleep for 5 seconds
