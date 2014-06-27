#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import random

values = [7, 11, 13, 15, 12]

def main():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(7, GPIO.OUT)
    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    GPIO.setup(15, GPIO.OUT)
    GPIO.setup(12, GPIO.OUT)
    for i in range(0, 2):
        GPIO.output(7, True)
        GPIO.output(11, True)
        GPIO.output(13, True)
        GPIO.output(15, True)
        GPIO.output(12, True)
        time.sleep(1)
        GPIO.output(7, False)
        GPIO.output(11, False)
        GPIO.output(13, False)
        GPIO.output(15, False)
        GPIO.output(12, False)
        time.sleep(1)

    for i in range(0, 10):
        pin = random.choice(values)
        GPIO.output(pin, True)
        time.sleep(1)
        GPIO.output(pin, False)
        time.sleep(1)

    GPIO.cleanup()

if __name__ == "__main__":
    main()    
