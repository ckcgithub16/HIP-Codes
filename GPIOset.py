import RPi.GPIO as GPIO


#*****Set up GPIO for all hardware******#

#Choose BOARD (breadboard) as construction base for project
GPIO.setmode(GPIO.BOARD)

#Set the pin header 7 to be the trigger pin and pin 11 to be the echo pin (Distance Sensor)
PIN_TRIGGER = 7
PIN_ECHO = 11

#Sets pin 7 to be output pin and pin 11 to be input pin
GPIO.setup(PIN_TRIGGER, GPIO.OUT)
GPIO.setup(PIN_ECHO, GPIO.IN)

#Set pin 12 (for servo) as an output pin
GPIO.setup(12, GPIO.OUT)
servo = GPIO.PWM(12,50)
servo.start(0)

#Set pin 13 (for Solenoid) as an output pin
GPIO.setup(13, GPIO.OUT)