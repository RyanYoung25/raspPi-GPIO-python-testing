#!/usr/bin/env python
from Tkinter import *
import RPi.GPIO as GPIO
import threading 
import time
#@author Ryan
#Trying to use some global variables
#probably a much better way of doing this but it works
red = None
green = None
blue = None
master = None
done = False


#Make a thread class that handles all of the GPIO stuff
#It relies on the red green blue global variables to be the sliders
#very tightly coupled...oh well
class ControlThread (threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(7, GPIO.OUT)
        GPIO.setup(11, GPIO.OUT)
        GPIO.setup(13, GPIO.OUT)
        self.r = GPIO.PWM(7, 100)
        self.g = GPIO.PWM(11, 100)
        self.b = GPIO.PWM(13, 100)
        self.r.start(0)
        self.g.start(0)
        self.b.start(0)

    def run(self):
        global red
        global green
        global blue
        global done
        #change the duty cycle based off of what the slider says
        while not done:
            self.r.ChangeDutyCycle(red.get())
            self.g.ChangeDutyCycle(green.get())
            self.b.ChangeDutyCycle(blue.get())
            time.sleep(.01)
       
        #all done so let's clean up our mess
        self.r.stop()
        self.g.stop()
        self.b.stop()
        GPIO.cleanup()
#called when you press the x on the gui. Cleans everything up.
def cleanUp():
    global done
    global master
    done = True
    master.destroy()

#Makes a gpio thread and a Tk window then puts three scales on it
#nothing too crazy but getting it to run on your system may be a pain
#because the GPIO stuff needs root and X forwarding doesn't like root
#copy the last line of the command: xauth list
#into a file /root/.Xauthority (make one if you need to)
#then run the command: xauth add (what ever that last line was)
def main():
    global red
    global green
    global blue
    global master
    thread = ControlThread()
    master = Tk()
    master.title("RGB sliders")
    master.protocol('WM_DELETE_WINDOW', cleanUp)
    master.minsize(250, 200)
    rl = Label(master, text="Red")
    rl.pack()
    red = Scale(master, from_=0, to=100, orient=HORIZONTAL, length=200)
    red.pack()
    gl = Label(master, text="Green")
    gl.pack()
    green = Scale(master, from_=0, to=100, orient=HORIZONTAL, length=200)
    green.pack()
    bl = Label(master, text="Blue")
    bl.pack()
    blue = Scale(master, from_=0, to=100, orient=HORIZONTAL, length=200)
    blue.pack()
    thread.start()
    mainloop()


if __name__ == "__main__":
    main()
