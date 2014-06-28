#!/usr/bin/env python

import RPi.GPIO as GPIO
import time


def main():
    speed = 50
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(22, GPIO.OUT)
    pwm = GPIO.PWM(22, 50)
    pwm.start(speed)
    while True:
        speed = speed + 10
        if speed > 100:
            speed = 0
        pwm.ChangeDutyCycle(speed)
        time.sleep(1)
        

if __name__ == "__main__":
    main()
