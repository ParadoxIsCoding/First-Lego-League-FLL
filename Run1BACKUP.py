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
 
hub.speaker.beep(500,100)

#collection 1 
robot.straight(300,Stop.HOLD)
robot.turn(-40,Stop.HOLD)
robot.straight(150,Stop.HOLD)
robot.straight(-55,Stop.HOLD)
#Boat flip
robot.turn(80,Stop.HOLD)
RG.run_time(-300,800)
robot.straight(60,Stop.HOLD)
RG.run_time(300,3500,Stop.HOLD)
robot.straight(-80,Stop.HOLD)
RG.run_time(-600,600,Stop.HOLD)
RG.run_time(400,500,Stop.HOLD)
#collection 2
robot.turn(-45,Stop.HOLD)
robot.straight(400,Stop.HOLD)
robot.straight(-50,Stop.HOLD)  
robot.turn(54,Stop.HOLD)
robot.straight(150,Stop.HOLD)
robot.straight(-230,Stop.HOLD)
#octopus collection + turn back
robot.turn(-40,Stop.HOLD)
robot.straight(-300,Stop.HOLD)
robot.turn(-50,Stop.HOLD)
robot.straight(125,Stop.HOLD)
robot.straight(-500,Stop.HOLD)
