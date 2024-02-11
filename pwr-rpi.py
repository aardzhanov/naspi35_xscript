#!/usr/bin/python3

import RPi.GPIO as GPIO
from time import sleep,time
import subprocess
import logging

GPIO.setmode (GPIO.BCM)
GPIO.setup(17, GPIO.OUT, initial=GPIO.HIGH) #BOOT
GPIO.setup(4, GPIO.IN) #SHUTDOWN
detected = False

while True:
    sleep(0.1)
    state = GPIO.input(4)
    if state and not detected:
        #print('GPIO4 = HIGH')
        detected = True
        pulseStart=time()
        while GPIO.input(4):
            sleep(0.02)
            if (time()-pulseStart) >= 3:
                logging.debug('Shutdown')
                subprocess.run(["systemctl", "poweroff"])
                exit(0)
    elif detected:
        #print('DETECTED')
        if (time()-pulseStart) >= 1:
            logging.debug('Reboot')
            subprocess.run(["systemctl", "reboot"])
            exit(0)
