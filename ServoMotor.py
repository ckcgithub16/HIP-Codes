import RPi.GPIO as GPIO
import time as time
import hip

def TurnServo(angleInDutyCycles):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(12, GPIO.OUT)
    
    servo = GPIO.PWM(12,500)
    servo.start(0)

    print("Code is RUNNING", angleInDutyCycles)

    for dc in range(5,angleInDutyCycles,1): #I was able to turn the servo specific angles when I swapped angleInDutyCycles for a float between 5.0 and 10.0 duty cycles
        servo.ChangeDutyCycle(dc)
        time.sleep(0.2)

    servo.stop()
    GPIO.cleanup()

"""
 for dc in range(100,45,-5)
        servo.ChangeDutyCycle(dc)
        time.sleep(0.5)
"""