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
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Axis
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
 
hub = PrimeHub()
 
#Setting up the robot drive motors
left_motor = Motor(Port.F,Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.E)
LA = Motor(Port.A)
RA = Motor(Port.C)
 
#Setting up the robot attachment motors
 
#Setting up the colour sensors
 
#Setting up the DriveBase
robot = DriveBase(left_motor,right_motor,wheel_diameter=62.4,axle_track=104)
robot.use_gyro(True)
 
 
#Setting up the speed of the robot
robot.settings(800,400,400,100)
 
hub.speaker.beep(500,100)
 
#feed whale
robot.straight(810,Stop.HOLD)
robot.turn(40,Stop.HOLD)
robot.straight(50,Stop.HOLD)
robot.drive(140,0)
wait(1300)
robot.stop()
RA.run_time(-100,700)
wait(200)
RA.run_time(100,700)
#sonar reveal
robot.straight(-280,Stop.HOLD)
robot.turn(-55,Stop.HOLD)
robot.drive(200,0)
wait(700)
robot.stop()
LA.run_time(250,1500,Stop.HOLD)
 
robot.settings(800,600,600,300)
#turn back
robot.straight(-200)
robot.turn(-15)
robot.drive(-700,0)
wait(2000)
 
 