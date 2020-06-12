import math
import DistanceSensor2
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

#Function to convert angle into duty cycles
def FindDutyCycles(angleInput):

    # Set angleInDutyCycles to the duty cycles of the launch angle
    angleInDutyCycles = 11.5 #(((((angleInput/180) + 1) / 20)) * 100)

    angleInDutyCycles = float(angleInDutyCycles)
    return angleInDutyCycles
