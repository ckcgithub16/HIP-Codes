import RPi.GPIO as GPIO
import time


def OpenSolenoidValve():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(13, GPIO.OUT)
    GPIO.output(13, GPIO.HIGH)
    time.sleep(2)
    GPIO.output(13, GPIO.LOW)
    time.sleep(2)
    GPIO.cleanup()