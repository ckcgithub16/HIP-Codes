import RPi.GPIO as GPIO
import time as time
import hip

def TurnServo(angleInDutyCycles):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(12, GPIO.OUT)
    
    servo = GPIO.PWM(12,500)
    servo.start(0)

    try:
        for dc in range(5,15,1): # angleInDutyCycles needs to be put back instead of 10
            servo.ChangeDutyCycle(dc)
            time.sleep(0.2)
    except KeyboardInterrupt:
        pass
    servo.stop()
    GPIO.cleanup()

"""
 for dc in range(100,45,-5)
        servo.ChangeDutyCycle(dc)
        time.sleep(0.5)
"""