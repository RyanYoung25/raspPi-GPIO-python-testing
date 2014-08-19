#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

def main():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(16, GPIO.OUT)
    servo = GPIO.PWM(16, 50) #pin 16 at 50 hz, 20ms 
    pos = 1    #the duty cycle, position
    posInc = 1 #position increment
    servo.start(pos)

    for i in range(100):
        pos = pos + posInc
        if pos > 10:
            pos = 10
            posInc = -posInc
        if pos < 2:
            pos = 2
            posInc = -posInc
        servo.ChangeDutyCycle(pos)
        time.sleep(.05)
    servo.ChangeDutyCycle(6)    
    time.sleep(1)
    servo.stop()
    GPIO.cleanup()

if __name__ == "__main__":
    main()

