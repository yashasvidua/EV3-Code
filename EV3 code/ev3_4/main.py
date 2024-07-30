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
right_wheel = Motor(Port.B)
left_wheel = Motor(Port.C)
wheels=DriveBase(left_wheel,right_wheel,wheel_diameter=42,axle_track=20)
GSPK = 2.5
Speed = 250
d=500
gyro= GyroSensor(Port.S2)
wd = wheels.distance()
# Write your program here.
ev3.speaker.beep()
gyro.reset_angle(0)
wheels.reset()
if d>0
    while wd <= d:
        correction =(0- gyro.angle())*GSPK
        wheels.drive(speed,correction)
    wheels.stop()
    ev3.speaker.beep()
else:
    while wd <= d:
        correction =(0- gyro.angle())*GSPK
        wheels.drive(-speed,correction)
    wheels.stop()
    ev3.speaker.beep()


