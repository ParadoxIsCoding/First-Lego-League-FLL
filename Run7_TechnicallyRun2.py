from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

left_motor = Motor(Port.F,Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.E)
LA = Motor(Port.A)
RA = Motor(Port.C)

robot = DriveBase(left_motor,right_motor,62.4,104)
robot.use_gyro(True)
robot.settings(404,200,400,200)

#Pushing artifical habitat up
robot.straight(650)
#Pulling back top and releasing beam
robot.straight(-100)

#Returning home
robot.turn(-10)
robot.straight(-600)





