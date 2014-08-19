#!/usr/bin/env python
from RGB import RGBLED
import time
#Author: Ryan
#Randomly change colors on three RGB leds. 

def main():
    led1 = RGBLED(22, 24, 26)
    led2 = RGBLED(11, 13, 15)
    led3 = RGBLED(19, 21, 23)
    leds = [led1, led2, led3]
    for led in leds:
        led.redOn()
        time.sleep(1)
        led.redOff()
        led.greenOn()
        time.sleep(1)
        led.greenOff()
        led.blueOn()
        time.sleep(1)
        led.blueOff()

    led1.cleanUp()

if __name__ == "__main__":
    main()
