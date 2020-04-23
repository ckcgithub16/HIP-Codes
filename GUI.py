from DistanceSensor2 import MeasureDistances, RefineDistances, MeanlDistance
from ServoMotor import TurnServo
from hip import FindAngle
from hip import FindDutyCycles
from Solenoid import OpenSolenoidValve
import tkinter as tk

window = tk.Tk()
window.title("HIP Interface") 
window.geometry('350x200')

distanceLbl = tk.Label(window, text="")
distanceLbl.grid(column=2, row =0)

angleLbl = tk.Label(window, text="")
angleLbl.grid(column=2, row =1)

fireLbl = tk.Label(window, text="")
fireLbl.grid(column=2, row =3)

finalDistance = 0
angleInDutyCycles = 0
launchDutyCycle = 0
usuableAngle = 0


def ClearLabels():
    distanceLbl.configure(text="")
    angleLbl.configure(text="")
    fireLbl.configure(text="")

def PrintDistance():
    ClearLabels()
    listDistances = MeasureDistances()
    updatedDistances = RefineDistances(listDistances)
    finalDistance = MeanlDistance(updatedDistances)
    distanceLbl.configure(text=str(finalDistance))

GetDistanceBtn = tk.Button(window, text="Get Distance", command=PrintDistance)
GetDistanceBtn.grid(column=1, row=0)

def PrintAngle():
    launchAngle = FindAngle(finalDistance)
    launchDutyCycle = FindDutyCycles(launchAngle)
    angleLbl.configure(text=str(launchAngle))
    print("duty cycle", launchDutyCycle)

GetAngleBtn = tk.Button(window, text="Find Angle", command=PrintAngle)
GetAngleBtn.grid(column=1, row=1)

def MoveServo():
    angleInDutyCycles = launchDutyCycle
    TurnServo(angleInDutyCycles) #Delete the + 10

MoveServoBtn = tk.Button(window, text="Turn Servo", command=MoveServo)
MoveServoBtn.grid(column=1, row=2)

def Fire():
    OpenSolenoidValve()
    fireLbl.configure(text="Fired")
    

FireBtn = tk.Button(window, text="Fire", command=Fire)
FireBtn.grid(column=1, row=3)


window.mainloop()