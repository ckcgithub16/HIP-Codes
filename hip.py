import math
import DistanceSensor2
import RPi.GPIO as GPIO


def FindAngle(finalDistance):
    angle = (1/2) * (math.asin((9.8 * finalDistance)/179.8603))
    degrees = angle * (180 / math.pi)
    if (degrees > 45):
        degrees = 45
    return degrees

# usuableAngle = FindAngle(DistanceSensor2.finalDistance)
