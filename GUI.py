import RPi.GPIO as GPIO
from DistanceSensor2 import MeasureDistances, RefineDistances, MeanlDistance
from ServoMotor import TurnServo
from LaunchAngle import FindAngle
from LaunchAngle import FindDutyCycles
from Solenoid import OpenSolenoidValve
import tkinter as tk

#Create a window (GUI), title it, and set its dimensions using tkinter  
window = tk.Tk()
window.title("HIP Interface") 
window.geometry('350x200')

#Create GPIO setup (for all devices) button on GUI
gpioSetLbl = tk.Label(window, text="")
gpioSetLbl.grid(column=2, row =1)

#Create and place label that will display the distance from a target
distanceLbl = tk.Label(window, text="")
distanceLbl.grid(column=2, row =1)

#Create and place a label that will display and place the launch angle in degrees
angleLbl = tk.Label(window, text="")
angleLbl.grid(column=2, row =2)

#Create and place a label that will display whether or not the projectile has been fired
fireLbl = tk.Label(window, text="")
fireLbl.grid(column=2, row =4)

#Initializing of the global variables
finalDistance = 0
angleInDutyCycles = 0
launchDutyCycle = 0
usuableAngle = 0




#*****Set up GPIO for all hardware******#

#Choose BOARD (breadboard) as construction base for project
GPIO.setmode(GPIO.BOARD)

#Set the pin header 7 to be the trigger pin and pin 11 to be the echo pin (Distance Sensor)
PIN_TRIGGER = 7
PIN_ECHO = 11

#Sets pin 7 to be output pin and pin 11 to be input pin
GPIO.setup(PIN_TRIGGER, GPIO.OUT)
GPIO.setup(PIN_ECHO, GPIO.IN)

#Set pin 12 (for servo) as an output pin
GPIO.setup(12, GPIO.OUT)
servo = GPIO.PWM(12,50)
servo.start(0)

#Set pin 13 (for Solenoid) as an output pin
GPIO.setup(13, GPIO.OUT)




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
GetDistanceBtn.grid(column=1, row=1)

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