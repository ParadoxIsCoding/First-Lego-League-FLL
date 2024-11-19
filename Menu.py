from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from pybricks.tools import hub_menu
 
# Make a menu to choose a letter. You can also use numbers.
selected = hub_menu("1", "2", "3", "4","5","6")
 
# Based on the selection, run a program.
if selected == "1":
    import Run1
elif selected == "2":
    import Run2
elif selected == "3":
    import Run3
elif selected == "4":
    import Run4
elif selected == "5":
    import Run5
elif selected == "6":
    import Run6