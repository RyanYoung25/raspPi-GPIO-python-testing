#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import math

def main():
    speed = 50
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(22, GPIO.OUT)
    pwm = GPIO.PWM(22, 50)
    pwm.start(speed)
    for i in range(0, 1000):
        x = i 
        speed = 50 * (1.0 + math.sin(x + .05))
        print speed
        pwm.ChangeDutyCycle(speed)
        time.sleep(.05)       
        

if __name__ == "__main__":
    main()
