import RPi.GPIO as GPIO
import time as time
import hip

def TurnServo(usuableAngle):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.OUT)
    
    servo = GPIO.PWM(18,500)
    servo.start(0)

    try:
        for dc in range(50,usuableAngle,2):
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