from gpiozero import MotionSensor
import os

pir = Motionsensor(4)
while True:
    if pir.motion_detected:
        mypic()
        mytweet()
        #print("something detected")
