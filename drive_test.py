from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

left_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.D)



robot = DriveBase(left_motor,right_motor,56,112)
robot.use_gyro(True)

robot.straight(700)
robot.turn(45)
robot.straight(180)
robot.straight(-75)
robot.turn(-55)
robot.straight(-700)