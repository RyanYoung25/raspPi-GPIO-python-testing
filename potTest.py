#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

def main():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(12, GPIO.OUT)
    GPIO.output(12, True)
    time.sleep(20)
    GPIO.output(12, False)
    GPIO.cleanup()

if __name__ == "__main__":
    main()    
