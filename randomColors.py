#!/usr/bin/env python
from RGB import RGBLED
import time
import random
#Author: Ryan
#Randomly change colors on the RGB led. Same pin out as the rest of the RGB led
#projects

def main():
    led = RGBLED()
    led.startPWM(100, 0)
    for i in range(0, 100):
        led.redDutyCycle(random.randint(0, 100))
        led.greenDutyCycle(random.randint(0, 100))
        led.blueDutyCycle(random.randint(0, 100))
        time.sleep(.15)
    led.stopPWM()
    led.cleanUp()

if __name__ == "__main__":
    main()
