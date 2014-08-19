#!/usr/bin/env python
from RGB import RGBLED
import time
import random
#Author: Ryan
#Randomly change colors on three RGB leds. 

def main():
    led1 = RGBLED(22, 24, 26)
    led2 = RGBLED(11, 13, 15)
    led3 = RGBLED(19, 21, 23)
    led1.startPWM(100, 0)
    led2.startPWM(100, 0)
    led3.startPWM(100, 0)
    for i in range(0, 200):
        led1.redDutyCycle(random.randint(0, 100))
        led1.greenDutyCycle(random.randint(0, 100))
        led1.blueDutyCycle(random.randint(0, 100))

        led2.redDutyCycle(random.randint(0, 100))
        led2.greenDutyCycle(random.randint(0, 100))
        led2.blueDutyCycle(random.randint(0, 100))
        
        led3.redDutyCycle(random.randint(0, 100))
        led3.greenDutyCycle(random.randint(0, 100))
        led3.blueDutyCycle(random.randint(0, 100))
        time.sleep(2.5)
    led1.stopPWM()
    led2.stopPWM()
    led3.stopPWM()
    led1.cleanUp()

if __name__ == "__main__":
    main()
