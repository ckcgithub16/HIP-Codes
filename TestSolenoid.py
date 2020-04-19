import RPi.GPIO as GPIO
import time

def OpenSolenoidValve():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(4, GPIO.OUT)
    GPIO.output(4, GPIO.HIGH)
    time.sleep(2)
    GPIO.output(4, GPIO.LOW)
    time.sleep(2)
    GPIO.cleanup()