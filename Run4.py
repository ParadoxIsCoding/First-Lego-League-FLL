from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
 
hub = PrimeHub()
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
 
#garden flip
RG.run_time(-200,750,Stop.HOLD,wait=False)
robot.straight(1050)
RG.run_time(-250,2000,Stop.HOLD)
RG.run_time(250,750,Stop.HOLD)
robot.straight(-110,Stop.HOLD)
 
#shark flip
robot.turn(-51)
robot.straight(155,Stop.HOLD)
robot.drive(200,0)
wait(1000)
robot.stop()
robot.straight(-300)
robot.turn(-90)
robot.straight(800)
 
#fhtlkd
#robot.turn(100)
#robot.straight(200)