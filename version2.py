#region VEXcode Generated Robot Configuration
from vex import *
import urandom
import math


# wait for rotation sensor to fully initialize
wait(30, MSEC)


# Make random actually random
def initializeRandomSeed():
    wait(100, MSEC)
    random = brain.battery.voltage(MV) + brain.battery.current(CurrentUnits.AMP) * 100 + brain.timer.system_high_res()
    urandom.seed(int(random))
      
# Set random seed 
initializeRandomSeed()


def play_vexcode_sound(sound_name):
    # Helper to make playing sounds from the V5 in VEXcode easier and
    # keeps the code cleaner by making it clear what is happening.
    print("VEXPlaySound:" + sound_name)
    wait(5, MSEC)

# add a small delay to make sure we don't print in the middle of the REPL header
wait(200, MSEC)
# clear the console to make sure we don't have the REPL in the console
print("\033[2J")

#endregion VEXcode Generated Robot Configuration

brain=Brain()
controller=Controller()

motor_1 = Motor(PORT1)
motor_2 = Motor(PORT2)

# Tank drive control loop
while True:
    axis2 = controller.axis2.position()  # -100..100
    
    axis1 = controller.axis1.position()  # -100..100
    
    left_speed = axis2 + axis1   # Forward/back + left/right
    right_speed = axis2 - axis1  # Forward/back - left/right
    
    # Apply deadband and control left motor
    if abs(left_speed) < 5:
        motor_1.stop()
    else:
        motor_1.spin(FORWARD, left_speed, PERCENT)
        
    # Apply deadband and control right motor
    if abs(right_speed) < 5:
        motor_2.stop()
    else:
        motor_2.spin(FORWARD, right_speed, PERCENT)
    
