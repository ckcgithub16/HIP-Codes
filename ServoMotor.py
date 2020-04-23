import RPi.GPIO as GPIO
import time as time
import hip

def TurnServo(angleInDutyCycles):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(12, GPIO.OUT)
    
    servo = GPIO.PWM(12,500)
    servo.start(0)

    try:
        for dc in range(5.0,angleInDutyCycles,1.0): 
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