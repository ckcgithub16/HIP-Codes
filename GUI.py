import RPi.GPIO as GPIO
from DistanceSensor2 import MeasureDistances, RefineDistances, MeanlDistance
from ServoMotor import TurnServo
from LaunchAngle import FindAngle
from LaunchAngle import FindDutyCycles
from Solenoid import OpenSolenoidValve
import tkinter as tk
from GPIOset import *

#Create a window (GUI), title it, and set its dimensions using tkinter  
window = tk.Tk()
window.title("HIP Interface") 
window.geometry('350x200')

#Create and place label that will display the distance from a target
distanceLbl = tk.Label(window, text="")
distanceLbl.grid(column=2, row =0)

#Create and place a label that will display and place the launch angle in degrees
angleLbl = tk.Label(window, text="")
angleLbl.grid(column=2, row =1)

#Create and place a label that will display whether or not the projectile has been fired
fireLbl = tk.Label(window, text="")
fireLbl.grid(column=2, row =3)

#Initializing of the global variables
finalDistance = 0
angleInDutyCycles = 0
launchDutyCycle = 0
usuableAngle = 0

#Function to clear all displayed values
def ClearLabels():
    distanceLbl.configure(text="")
    angleLbl.configure(text="")
    fireLbl.configure(text="")


#Function to print the determined distance on the GUI
def PrintDistance():
    ClearLabels()

    #Determine and set the final distance to finalDistance
    listDistances = MeasureDistances()
    updatedDistances = RefineDistances(listDistances)
    finalDistance = MeanlDistance(updatedDistances)
    
    #Display the final distance from the target on the GUI
    distanceLbl.configure(text=str(finalDistance))

#Establish and place the GetDistance button. When it is clicked, run PrintDistance()
GetDistanceBtn = tk.Button(window, text="Get Distance", command=PrintDistance)
GetDistanceBtn.grid(column=1, row=0)

#Function to print the launch angle on the GUI
def PrintAngle():
    launchAngle = FindAngle(finalDistance)
    launchDutyCycle = FindDutyCycles(launchAngle)
    
    angleLbl.configure(text=str(launchAngle))
    
    #Print the duty cycles to the Raspberry Pi terminal
    print("duty cycle", launchDutyCycle)

#Establish and place the GetAngle button. When it is clicked, run PrintAngle()
GetAngleBtn = tk.Button(window, text="Find Angle", command=PrintAngle)
GetAngleBtn.grid(column=1, row=1)

#Function to move the servo
def MoveServo():
    launchAngle = FindAngle(finalDistance)
    launchDutyCycle = FindDutyCycles(launchAngle)
    print("launch angle is", launchAngle, "DUTY CYCLES are", launchDutyCycle)
    TurnServo(launchDutyCycle)

    #Stop servo once at desired duty cycle/angle
    servo.stop()

#Establish and place the MoveServo button. When it is clicked, run MoveServo()
MoveServoBtn = tk.Button(window, text="Turn Servo", command=MoveServo)
MoveServoBtn.grid(column=1, row=3)

#Function to fire the solenoid
def Fire():
    OpenSolenoidValve()
    fireLbl.configure(text="Fired")
    
#Establish and place the Fire button. When it is clicked, run Fire()
FireBtn = tk.Button(window, text="Fire", command=Fire)
FireBtn.grid(column=1, row=4)

#Create infinite loop so GUI does not close unexpectedly
window.mainloop()
servo.changeDutyCycles(5)
GPIO.cleanup()