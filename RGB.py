#!/usr/bin/env python
import RPi.GPIO as GPIO

class RGBLED:
    def __init__(self, red=7, green=11, blue=13):
        #Create a RGBLED object with default pins 1, 11, 13
        self.r = red
        self.g = green
        self.b = blue

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.r, GPIO.OUT)
        GPIO.setup(self.g, GPIO.OUT)
        GPIO.setup(self.b, GPIO.OUT)

    def startPWM(self, freq=100, startCycle=20):
        #Create PWM objects for each led and start 
        # pwm on at the frequency specified and the 
        # initial duty cycle, startCycle
        self.rpwm = GPIO.PWM(self.r, freq)
        self.gpwm = GPIO.PWM(self.g, freq)
        self.bpwm = GPIO.PWM(self.b, freq)
        self.rpwm.start(startCycle)
        self.gpwm.start(startCycle)
        self.bpwm.start(startCycle)


    def redOn(self):
        GPIO.output(self.r, True)

    def redOff(self):
        GPIO.output(self.r, False)

    def blueOn(self):
        GPIO.output(self.b, True)

    def blueOff(self):
        GPIO.output(self.b, False)

    def greenOn(self):
        GPIO.output(self.g, True)

    def greenOff(self):
        GPIO.output(self.g, False)

    def stopPWM(self):
        #Stop all of the pwm objects
        self.rpwm.stop()
        self.gpwm.stop()
        self.bpwm.stop()

    def redDutyCycle(self, value):
        self.rpwm.ChangeDutyCycle(value)

    def greenDutyCycle(self, value):
        self.gpwm.ChangeDutyCycle(value)

    def blueDutyCycle(self, value):
        self.bpwm.ChangeDutyCycle(value)
        
    def cleanUp(self):
        #clean up after using the pins
        GPIO.cleanup()
