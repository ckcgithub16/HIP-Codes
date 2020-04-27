import RPi.GPIO as GPIO
import time

#Function to open the solenoid valve
def OpenSolenoidValve():

    #Set the pin state of pin 13 to high to open the solenoid
    GPIO.output(13, GPIO.HIGH)

    time.sleep(1)

    #Set the pin state of pin 13 to low
    GPIO.output(13, GPIO.LOW)

    time.sleep(1)

    #Reset the pin states of all pins
    GPIO.cleanup()