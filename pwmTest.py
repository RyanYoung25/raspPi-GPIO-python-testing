#!/usr/bin/env python

import RPi.GPIO as GPIO
import time


def main():
    speed = 50
    inc = 1
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(22, GPIO.OUT)
    pwm = GPIO.PWM(22, 7500)
    pwm.start(speed)
    while True:
        speed = speed + inc
        if speed > 100:
            speed = 100
            inc = -1
        if speed < 0:
            speed = 0
            inc = 1
        pwm.ChangeDutyCycle(speed)
        time.sleep(1)
        

if __name__ == "__main__":
    main()
