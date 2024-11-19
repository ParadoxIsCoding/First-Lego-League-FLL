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
robot.settings(700,500,400,200)
 
#garden flip
RG.run_time(-200,750,Stop.HOLD,wait=False)
robot.straight(1100)
RG.run_time(-250,2000,Stop.HOLD)
RG.run_time(250,700,Stop.HOLD)
robot.straight(-130,Stop.HOLD)
RG.run_time(250,500,Stop.HOLD)
 
#shark flip
robot.turn(-40)
robot.settings(800,500,400,200)
robot.straight(140,Stop.HOLD)
robot.drive(200,0)
wait(1000)
robot.stop()

#push coral flip thingy
robot.straight(-350)
robot.turn(-40)
robot.straight(440)
robot.straight(-200)
robot.turn(-60)
robot.straight(800)

