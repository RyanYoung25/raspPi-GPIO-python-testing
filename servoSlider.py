#!/usr/bin/env python
from Tkinter import *
import RPi.GPIO as GPIO
import threading 
import time
#@author Ryan
#Trying to use some global variables
#probably a much better way of doing this but it works
servo = None
master = None
done = False


#Make a thread class that handles all of the GPIO stuff
#It relies on the red green blue global variables to be the sliders
#very tightly coupled...oh well
class ControlThread (threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(16, GPIO.OUT)
        self.s = GPIO.PWM(16, 50)
        self.s.start(0)

    def run(self):
        global green
        global done
        #change the duty cycle based off of what the slider says
        while not done:
            self.s.ChangeDutyCycle(servo.get())
            time.sleep(.01)
       
        #all done so let's clean up our mess
        self.s.stop()
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
    global servo
    global master
    thread = ControlThread()
    master = Tk()
    master.title("Servo slider")
    master.protocol('WM_DELETE_WINDOW', cleanUp)
    master.minsize(250, 200)
    sl = Label(master, text="Servo")
    sl.pack()
    servo = Scale(master, from_=0, to=12.5, orient=HORIZONTAL, length=200)
    servo.pack()
    thread.start()
    mainloop()


if __name__ == "__main__":
    main()
