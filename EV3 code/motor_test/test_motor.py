#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
# Initialize the EV3 brick.
ev3 = EV3Brick()
# Initialize a motor at port B.
righ_wheel = Motor(Port.c)
left_wheel = Motor(Port.B)
wheels=DriveBase(left_wheel,right_wheel,wheel_diameter=24,axle_track=24)
# Play a sound.
ev3.speaker.beep()
# Run the motor up to 500 degrees per second. To a target angle of 90 degrees.
wheels.straight(100)
# Play another beep sound.
ev3.speaker.beep(1000, 500)
