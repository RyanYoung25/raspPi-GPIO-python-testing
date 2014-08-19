#!/usr/bin/env python

from RGB import RGBLED
import time
import math
#author Ryan
#Make the three LEDs go through colors passing on to the next

def main():
    red=0
    green=25
    blue=50
    dred=5
    dgreen=5
    dblue=5
    #make the map for the leds
    ledMap = {}
    led1 = RGBLED(22, 24, 26)
    led2 = RGBLED(11, 13, 15)
    led3 = RGBLED(19, 21, 23)
    #map the leds to their (R, G, B) duty cycle values
    ledMap[led1]=(0,0,0)
    ledMap[led2]=(0,0,0)
    ledMap[led3]=(0,0,0)
    #start led pwm
    led1.startPWM(100, 0)
    led2.startPWM(100, 0)
    led3.startPWM(100, 0)

    for i in range(0, 10000):
        color1 = (red, green, blue)
        color2 = ledMap[led1]
        color3 = ledMap[led2]
        #set all of the duty cycles
        led1.redDutyCycle(color1[0])
        led2.redDutyCycle(color2[0])
        led3.redDutyCycle(color3[0])
        led1.greenDutyCycle(color1[1])
        led2.greenDutyCycle(color2[1])
        led3.greenDutyCycle(color3[1])
        led1.blueDutyCycle(color1[2])
        led2.blueDutyCycle(color2[2])
        led3.blueDutyCycle(color3[2])
        #Update the map with the new colors
        ledMap[led1]=color1
        ledMap[led2]=color2
        ledMap[led3]=color3
        #delay
        time.sleep(.25)

        red = 50* (1.0 + math.sin(2*i +.05))
        green = 50* (1.0 + math.sin(.5*i +1.75))
        blue = 50* (1.0 + math.sin(4*i +.25))

    led1.stopPWM()
    led2.stopPWM()
    led3.stopPWM()
    led1.cleanUp()

if __name__ == "__main__":
    main()
