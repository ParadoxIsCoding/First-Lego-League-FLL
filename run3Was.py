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
robot.settings(700,500,400,100)
 
 
#drop off octopus
wait(1000)
LG.run_time(-200,1000,Stop.BRAKE,wait=False)
robot.straight(750,Stop.HOLD)
robot.turn(-90,Stop.HOLD)
robot.straight(520,Stop.HOLD)
 
#line up for lift
robot.straight(-100,Stop.HOLD)
RG.run_angle(430,-1150,Stop.HOLD,wait=False)
robot.turn(40,Stop.HOLD)
robot.straight(135,Stop.HOLD)
robot.turn(-40,Stop.HOLD)
 
#anglar fish and sample
robot.straight(140,Stop.HOLD)
RG.run_time(800,1750,Stop.HOLD)
wait(2000)
robot.straight(-50,Stop.HOLD)
RG.run_angle(700,750,Stop.HOLD)
 
robot.straight(100,Stop.HOLD)
LG.run_time(100,1500,Stop.COAST,wait=False)
robot.straight(110,Stop.HOLD)
RG.run_time(-800,2000,Stop.HOLD)
robot.straight(70,Stop.HOLD)
LG.run_time(-200,1500,Stop.COAST,wait=False)
RG.run_time(800,1000,Stop.HOLD)
robot.straight(50,Stop.HOLD)
 
RG.run_time(-800,1500,Stop.HOLD)
wait(500)
RG.run_time(800,500)
RG.run_time(800,2500,Stop.HOLD,wait=False)
LG.run_time(-200,1000,Stop.COAST_SMART,wait=False)
robot.straight(100,Stop.HOLD)
robot.turn(-10,Stop.HOLD)
robot.straight(250,Stop.HOLD)
robot.turn(-45,Stop.HOLD)
LG.run_time(200,1500,Stop.COAST_SMART,wait=False)
robot.drive(700,0)
wait(2500)
 
#has context menu


#has context menutho

