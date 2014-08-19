#!/usr/bin/env python

import RPi.GPIO as GPIO

isOn = False

def switchOn(channel):
    global isOn
    print "Switch is on"
    isOn = True

def switchOff(channel):
    global isOn
    print "Switch is off"
    isOn = False

def main():
    global isOn
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(11, GPIO.OUT)
    GPIO.add_event_detect(7, GPIO.RISING, callback=switchOn, bouncetime=300) 
    GPIO.add_event_detect(13, GPIO.RISING, callback=switchOff, bouncetime=300) 
    while True:
        if isOn:
            GPIO.output(11, True)
        else:
            GPIO.output(11, False)

 

if __name__ == "__main__":
    main()
