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
wait(500)
LG.run_time(-200,1000,Stop.BRAKE,wait=False)
robot.straight(750,Stop.HOLD)
robot.turn(-90,Stop.HOLD)
robot.straight(520,Stop.HOLD)
 
#line up for lift
robot.straight(-150,Stop.HOLD)
robot.turn(38,Stop.HOLD)
robot.straight(350,Stop.HOLD)
robot.straight(-150,Stop.HOLD)
robot.turn(-40)
#wait(2500)
#robot.straight(-100,Stop.HOLD)
 
#anglar fish and sample
robot.straight(220,Stop.HOLD)
LG.run_time(500,1500,Stop.COAST,wait=False)
robot.straight(120,Stop.HOLD)
#RG.run_time(-800,900,Stop.HOLD)
#robot.straight(70,Stop.HOLD)
LG.run_time(-200,1500,Stop.COAST,wait=False)
#RG.run_time(800,900,Stop.HOLD)
robot.straight(50,Stop.HOLD)
 
#RG.run_time(-800,800,Stop.HOLD)
#wait(500)
#RG.run_time(800,500)
#RG.run_time(800,2500,Stop.HOLD,wait=False)
LG.run_time(-200,1000,Stop.COAST_SMART,wait=False)
robot.straight(100,Stop.HOLD)
robot.turn(-10,Stop.HOLD)
robot.straight(250,Stop.HOLD)
robot.turn(-40,Stop.HOLD)
LG.run_time(200,1500,Stop.COAST_SMART,wait=False)
robot.drive(700,0)
wait(2500)

 

 
 