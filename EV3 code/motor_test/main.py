#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
right_wheel = Motor(Port.C)
left_wheel = Motor(Port.B)
wheels=DriveBase(left_wheel,right_wheel,wheel_diameter=42,axle_track=20)
n = 1
d =500
gyro= GyroSensor(Port.S1)




# Write your program here.
while n>0:
    ev3.speaker.beep()
    gyro.reset_angle(0)
    while wheels.distance() >= d:
        correction =(0- gyro.angle())*3
        wheels.drive(300,correction)
    wheels.stop()
    left_wheel.brake()
    right_wheel.brake()
    ev3.speaker.beep()
    ev3.speaker.beep()
    gyro.reset_angle(0)
    while wheels.distance() >= (-1*d):
        correction =(0- gyro.angle())*3
        wheels.drive(-300,correction)
    wheels.stop()
    left_wheel.brake()
    right_wheel.brake()
    ev3.speaker.beep()
    n=n-1



