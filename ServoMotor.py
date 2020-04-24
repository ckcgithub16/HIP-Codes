import RPi.GPIO as GPIO
import time as time
import LaunchAngle

#Function to turn a servo motor to the launch angle
def TurnServo(angleInDutyCycles):
    
    #Choose BOARD (breadboard) as construction base for project 
    GPIO.setmode(GPIO.BOARD)

    #Set pin 12 as an output pin
    GPIO.setup(12, GPIO.OUT)
    
    servo = GPIO.PWM(12,500)
    servo.start(0)

    #Prints the duty cycle the servo will be set to 
    print("Code is RUNNING", angleInDutyCycles)

    #Assuming servo starts at 0 degree angle, increases the duty cycles by 1 until the duty cycle corresponding with the launch angle is reached
    for dc in range(5,angleInDutyCycles,1): #I was able to turn the servo specific angles when I swapped angleInDutyCycles for a value between 5 and 10 duty cycles
        #servo.changeDutyCycle() takes duty cycles as a parameter
        servo.ChangeDutyCycle(dc)
        time.sleep(0.2)

    #Stop servo once at desired duty cycle/angle
    servo.stop()
    
    #Resets the pin states
    GPIO.cleanup()
