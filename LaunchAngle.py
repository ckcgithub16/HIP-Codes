import math
import DistanceSensor2
from GPIOset import *
import sys
import RPi.GPIO as GPIO

#Function to calculate the launch angle in degrees based on distance from the target
def FindAngle(finalDist):
    finalDist = finalDist / 100
    angle = (1/2) * (math.asin((9.8 * finalDist)/36.976))
    print("angle", angle)

    #Convert the variable "angle" from radians to degress  
    degrees = angle * (180 / math.pi)
    print("degrees1", degrees)
    return degrees

#!/usr/bin/python

# first command line argument is input angle in degrees
# angleInput = float(sys.argv[1])



## Old Function to convert angle into duty cycles ##
"""
def FindDutyCycles(angleInput):

    # Set angleInDutyCycles to the duty cycles of the launch angle; 2dc is the servo lower limit. 11.80 is about the upper limit.
    angleInDutyCycles = (((((angleInput/180) + 1) / 20)) * 100)

    angleInDutyCycles = float(angleInDutyCycles)
    return angleInDutyCycles
"""


def GetDutyCycleFromAngle(angleInput):
    #angle is in degrees
    pulseWidthMS = pulseMinMS + (angleInput / 180.0) * (pulseMaxMS - pulseMinMS)
    angleInDutyCycles = (pulseWidthMS / periodMS) * 100.0
    return angleInDutyCycles
if (pulseMaxMS > periodMS):
    print ("Invalid combination of PWM frequency and max. pulse width")
    exit()
