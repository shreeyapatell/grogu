from math import sin, cos
from pylx16a.lx16a import *
import time
'''
Initial Position (servos 2, 5): 139
Initial Position (servos 3, 6): 144

'''
LX16A.initialize("/dev/cu.usbserial-10", 0.1)
SERVO1_MIN_ANGLE = 175
SERVO1_MAX_ANGLE = 240
SERVO1_ANGLE_RANGE = SERVO1_MAX_ANGLE - SERVO1_MIN_ANGLE

SERVO2_MIN_ANGLE = 55
SERVO2_MAX_ANGLE = 144
SERVO2_ANGLE_RANGE = SERVO2_MAX_ANGLE - SERVO2_MIN_ANGLE

SERVO3_MIN_ANGLE = 175
SERVO3_MAX_ANGLE = 240
SERVO3_ANGLE_RANGE = SERVO3_MAX_ANGLE - SERVO3_MIN_ANGLE

SERVO4_MIN_ANGLE = 55
SERVO4_MAX_ANGLE = 144
SERVO4_ANGLE_RANGE = SERVO4_MAX_ANGLE - SERVO4_MIN_ANGLE

try:
    servo1 = LX16A(2)
    servo2 = LX16A(3)
    servo3 = LX16A(5)
    servo4 = LX16A(6)
    #servo1.set_angle_limits(0, 240)
    servo2.set_angle_limits(0, 240)
    servo4.set_angle_limits(0, 240)
    

except ServoTimeoutError as e:
    print(f"Servo {e.id_} is not responding. Exiting...")
    quit()

t = 0
while True:
    #servo1.move(sin(t) * 60 + 60)
    #servo2.move(cos(t) * 60 + 60)

    angle1 = (sin(t) * 60 + 60) % SERVO1_ANGLE_RANGE + SERVO1_MIN_ANGLE
    servo1.move(angle1)

    angle2 = (cos(t) * 60 + 60) % SERVO2_ANGLE_RANGE + SERVO2_MIN_ANGLE
    servo2.move(angle2)

    angle3 = (sin(t) * 60 + 60) % SERVO3_ANGLE_RANGE + SERVO3_MIN_ANGLE
    servo3.move(angle3)

    angle4 = (cos(t) * 60 + 60) % SERVO4_ANGLE_RANGE + SERVO4_MIN_ANGLE
    servo4.move(angle4)

    time.sleep(0.1)
    t += 0.1
