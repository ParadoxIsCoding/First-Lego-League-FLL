from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
 
hub = PrimeHub()
 
left_motor = Motor(Port.F, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.E)
RG = Motor(Port.C)
LG = Motor(Port.A)
 
 
robot = DriveBase(left_motor,right_motor,62.4,104)
robot.use_gyro(True)
robot.settings(700,300,400,200)



robot.straight(750)
robot.turn(-90)
robot.straight(520)

robot.straight(-100)
RG.run_angle(700,-1200,Stop.HOLD,wait=False)
robot.turn(40)
robot.straight(100)
robot.turn(-40)


robot.straight(150)
RG.run_angle(700,600,Stop.HOLD)
robot.straight(-50)
RG.run_angle(700,700,Stop.HOLD)
robot.straight(210)
LG.run_time(200,500)
RG.run_time(-800,2000)
robot.straight(50)


