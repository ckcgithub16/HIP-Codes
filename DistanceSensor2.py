#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import statistics
import numpy as np


def MeasureDistances():
    listDistances = []
    for n in range(10):
        try:
            GPIO.setmode(GPIO.BOARD)

            PIN_TRIGGER = 7
            PIN_ECHO = 11

            GPIO.setup(PIN_TRIGGER, GPIO.OUT)
            GPIO.setup(PIN_ECHO, GPIO.IN)

            GPIO.output(PIN_TRIGGER, GPIO.LOW)

            time.sleep(0.5)

            GPIO.output(PIN_TRIGGER, GPIO.HIGH)

            time.sleep(0.00001)

            GPIO.output(PIN_TRIGGER, GPIO.LOW)

            while GPIO.input(PIN_ECHO)==0:
                    pulse_start_time = time.time()
            while GPIO.input(PIN_ECHO)==1:
                    pulse_end_time = time.time()

            pulse_duration = pulse_end_time - pulse_start_time
            distance = round(pulse_duration * 17150, 2)
            listDistances.append(distance)

        finally:
            GPIO.cleanup()
    return listDistances

# MeasureDistances()

"""
def RefineDistances(listDistances): 
    np.asarray(listDistances).astype(float)
    newDistances = []
    zscoreArray = stats.zscore(listDistances)
    for i in range(len(listDistances)):
        if (zscoreArray[i] <= 2.0000):
            newDistances.append(listDistances[i])
    return newDistances
"""

newData = []

def zscore(myData): #Needs fixing
	mu = np.mean(myData)
	stdv = np.std(myData)

	for value in myData:
		zscoredVal = (value - mu)/stdv
		newData.append(zscoredVal)

	return newData 

def RefineDistances(listDistances):
    revisedDistances = []
    np.asarray(listDistances).astype(float)
    np.asarray(revisedDistances).astype(float)
    for i in range(len(listDistances)):
        if (abs(newData[i]) <= 2.0000):
            revisedDistances.append(listDistances[i])
    return revisedDistances

# updatedDistances = RefineDistances(listDistances)

def MeanlDistance(listDistances):
    return np.mean(listDistances)

# finalDistance = MeanlDistance(listDistances)
