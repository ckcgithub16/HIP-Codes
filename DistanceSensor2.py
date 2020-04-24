#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import statistics
import numpy as np

#Function to measure the distance to a target 20 times and compiles the distances into a list
def MeasureDistances():
    listDistances = []
    
    #Collect 20 distances using a list
    for n in range(20):
        try:

            #Choose BOARD (breadboard) as construction base for project 
            GPIO.setmode(GPIO.BOARD)

            #Set the pin header 7 to be the trigger pin and pin 11 to be the echo pin
            PIN_TRIGGER = 7
            PIN_ECHO = 11

            #Sets pin 7 to be output pin and pin 11 to be input pin
            GPIO.setup(PIN_TRIGGER, GPIO.OUT)
            GPIO.setup(PIN_ECHO, GPIO.IN)

            #Set pin 11 state to low
            GPIO.output(PIN_TRIGGER, GPIO.LOW)

            time.sleep(0.5)

            #Send ultrasonic signal out by setting the pin state of pin 7 to high
            GPIO.output(PIN_TRIGGER, GPIO.HIGH)

            time.sleep(0.00001)

            #Set the pin state of pin 7 to low
            GPIO.output(PIN_TRIGGER, GPIO.LOW)

            while GPIO.input(PIN_ECHO)==0:
                    pulse_start_time = time.time()
            while GPIO.input(PIN_ECHO)==1:
                    pulse_end_time = time.time()

            #Calculate the distances
            pulse_duration = pulse_end_time - pulse_start_time
            distance = round(pulse_duration * 17150, 2)

            #Add the distances to a list
            listDistances.append(distance)

        finally:
            #Resets pins to their original state
            GPIO.cleanup()

    return listDistances

# MeasureDistances()

#Function to calculate the z-scores (the number of standard deviations a data point is from the mean its data set) of the distances
def zscore(myData):
    newData = []
    mu = np.mean(myData)
    stdv = np.std(myData)

    #Calculate z-score for each distance and add the z-score to newData
    for value in myData:
        zscoredVal = (value - mu)/stdv
        newData.append(zscoredVal)

    return newData

#Function to eliminate extremely high and low distance values
def RefineDistances(listDistances):
    newData = zscore(listDistances)
    revisedDistances = []

    #Change listDistances and revisedDistances from lists into arrays
    np.asarray(listDistances).astype(float)
    np.asarray(revisedDistances).astype(float)

    #Prints the z-scores of the distances to the Raspberry Pi terminal
    print("NewData", newData)

    #Prints the number of distances collected-- should be 20 every time
    print("List Distancecs", len(listDistances))

    #Adds distances less than 2 standard deviations away from the mean of distances to the list revisedDistances
    for i in range(len(listDistances)):
        if (abs(newData[i]) <= 2.0000):
            revisedDistances.append(listDistances[i])
    return revisedDistances

#Function to average the new set of distances to detemine a final distance
def MeanlDistance(listDistances):
    return np.mean(listDistances)