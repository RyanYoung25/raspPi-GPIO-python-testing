#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import random

theMap = {1:7, 2:11, 3:13, 4:15, 5:12}
theList = [1, 2, 3, 4, 5]
isSorted = False

def display():
    for i in range(0, 5):
        GPIO.output(theMap[theList[i]], True)
        time.sleep(1)
    for i in range(1, 6):
        GPIO.output(theMap[i], False)

def check():
    global isSorted
    print theList
    isSorted = True
    for i in range(1, 5):
        if(theList[i - 1] > theList[i]):
            isSorted = False

def sort():
    random.shuffle(theList)
    check()
    display()


def main():
    global isSorted
    random.shuffle(theList)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(7, GPIO.OUT)
    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    GPIO.setup(15, GPIO.OUT)
    GPIO.setup(12, GPIO.OUT)
    
    for i in range(1, 5):
        GPIO.output(theMap[i], False)
    
    while( not isSorted):
        sort()
    GPIO.cleanup()

if __name__ == "__main__":
    main()    
