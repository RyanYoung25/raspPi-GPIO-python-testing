#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import math

def main():
    rs = 50
    gs = 50
    bs = 50
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(7, GPIO.OUT)
    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    red = GPIO.PWM(7, 100)
    green = GPIO.PWM(11, 100)
    blue = GPIO.PWM(13, 100)
    red.start(rs)
    green.start(gs)
    blue.start(bs)
    for i in range(0, 100):
        x = i 
        rs = 50 * (1.0 + math.sin(x + 0.0))
        gs = 50 * (1.0 + math.sin(.5*x + 1))
        bs = 50 * (1.0 + math.sin(x + 3))
 
        red.ChangeDutyCycle(rs)
        green.ChangeDutyCycle(gs)
        blue.ChangeDutyCycle(bs)
        time.sleep(.5)       
    red.stop()
    green.stop()
    blue.stop()
    GPIO.cleanup() 

if __name__ == "__main__":
    main()
