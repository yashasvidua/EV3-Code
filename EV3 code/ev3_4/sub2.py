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
wheels = DriveBase(left_wheel,right_wheel,wheel_diameter=55,axle_track=20)


wheels.turn(800)
wheels.stop
ev3.speaker.beep()
wheels.straight(280)
wheels.stop()
ev3.speaker.beep()
wheels.turn(-415)
wheels.stop
ev3.speaker.beep()
wheels.straight(2438.4)
wheels.stop()
ev3.speaker.beep()
wheels.turn(-415)
wheels.stop
ev3.speaker.beep()
wheels.straight(280)
wheels.stop()
ev3.speaker.beep()