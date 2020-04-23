import math
import DistanceSensor2
import RPi.GPIO as GPIO


def FindAngle(finalDistance):
    angle = (1/2) * (math.asin((9.8 * finalDistance)/179.8603))
    degrees = angle * (180 / math.pi)
    if (degrees > 45):
        degrees = 45
    return degrees

def FindDutyCycles(usuableAngle):
    angleInDutyCycles = ((((usuableAngle/180) + 1) / 20) + 7) #DELETE THE + 7
    angleInDutyCycles = int(angleInDutyCycles)
    return angleInDutyCycles


# usuableAngle = FindAngle(DistanceSensor2.finalDistance)
