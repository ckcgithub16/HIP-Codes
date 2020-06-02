import math
import DistanceSensor2
import RPi.GPIO as GPIO

#Function to calculate the launch angle in degrees based on distance from the target
def FindAngle(finalDist):
    finalDist = finalDist / 1000
    angle = (1/2) * (math.asin((9.8 * finalDist)/36.976))
    
    #Convert the variable "angle" from radians to degress  
    degrees = angle * (180 / math.pi)
    
    #Sets any angle greater than 45 degrees to 45 degrees b/se 45 degrees results in max distance
    if (degrees > 45):
        degrees = 45
    return degrees

#Function to convert angle into duty cycles
def FindDutyCycles(angleInput):

    # I added 7 to the formula to test the servo's movement b/se the distances I measured corresponded to duty cycles of 0
    angleInDutyCycles = (((((angleInput/180) + 1) / 20)) * 100) 

    # Set variable type of angleInDutyCycles to integer b/se the range() function in ServoMotor.py only takes integer parameters 
    # angleInDutyCycles = int(angleInDutyCycles)
    angleInDutyCycles = float(angleInDutyCycles)
    return angleInDutyCycles
