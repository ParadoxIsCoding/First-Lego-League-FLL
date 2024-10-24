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
 

robot.straight(650)
robot.turn(-53)
robot.straight(300)
LG.run_time(250,600,Stop.HOLD)
robot.settings(1000,1000)
robot.straight(-200)
robot.settings(700,300)
robot.turn(53)
robot.straight(-500)


