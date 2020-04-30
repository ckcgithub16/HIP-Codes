import RPi.GPIO as GPIO
import time
import LaunchAngle
from GPIOset import *

#Function to turn a servo motor to the launch angle
def TurnServo(angleInDutyCycles):
    
    #Prints the duty cycle the servo will be set to 
    print("Code is RUNNING", angleInDutyCycles)

    #Assuming servo starts at 0 degree angle, increases the duty cycles by 1 until the duty cycle corresponding with the launch angle is reached
    #for dc in range(5,50): #I was able to turn the servo specific angles when I swapped angleInDutyCycles for a value between 5 and 10 duty cycles
    #servo.changeDutyCycle() takes duty cycles as a parameter
    
    servo.start(5)

    servo.ChangeDutyCycle(angleInDutyCycles)
    # servo.setPositionServo(12, 180)
    print("dc is", angleInDutyCycles)
    time.sleep(0.2)

    servo.stop()
    
    #Resets the pin states
    #GPIO.cleanup()
