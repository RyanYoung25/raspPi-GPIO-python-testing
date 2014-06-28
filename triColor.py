#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import random

def red():
    GPIO.output(7, True)
    time.sleep(.25)
    GPIO.output(7, False)
def green():
    GPIO.output(11, True)
    time.sleep(.25)
    GPIO.output(11, False)
def blue():
    GPIO.output(13, True)
    time.sleep(.25)
    GPIO.output(13, False)
def aqua(): 
    GPIO.output(11, True)
    GPIO.output(13, True)
    time.sleep(.25)
    GPIO.output(11, False)
    GPIO.output(13, False)
def purple():
    GPIO.output(7, True)
    GPIO.output(13, True)
    time.sleep(.25)
    GPIO.output(7, False)
    GPIO.output(13, False)
def IDontKnowRedAndGreen():
    GPIO.output(7, True)
    GPIO.output(11, True)
    time.sleep(.25)
    GPIO.output(7, False)
    GPIO.output(11, False)
def main():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(7, GPIO.OUT)
    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    for i in range(0, 2):
        GPIO.output(7, True)
        GPIO.output(11, True)
        GPIO.output(13, True)
        time.sleep(1)
        GPIO.output(7, False)
        GPIO.output(11, False)
        GPIO.output(13, False)
        time.sleep(1)
    for i in range(0, 50):
        red()
        green()
        blue()
        aqua()
        purple()
        IDontKnowRedAndGreen()

    GPIO.cleanup()

if __name__ == "__main__":
    main()    
