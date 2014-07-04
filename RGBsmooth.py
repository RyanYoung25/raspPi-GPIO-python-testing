#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import math

def main():
    rs = 10
    gs = 70
    bs = 10
    ri = 1
    gi = 1
    bi = 1
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
    for i in range(0, 10000):
  
        rs = rs + ri 
        gs = gs + gi
        bs = bs + bi
        
        if rs > 100:
            rs = 100
            ri = -1
        if gs > 100:
            gs = 100
            gi = -1
        if bs > 100:
            bs = 100
            bi = -1

        if rs < 0:
            rs = 0
            ri = 1
        if gs < 0:
            gs = 0
            gi = 1
        if bs < 0:
            bs = 0
            bi = 1

        red.ChangeDutyCycle(rs)
        green.ChangeDutyCycle(gs)
        blue.ChangeDutyCycle(bs)
        time.sleep(.01)       

    red.stop()
    green.stop()
    blue.stop()
    GPIO.cleanup() 

if __name__ == "__main__":
    main()
