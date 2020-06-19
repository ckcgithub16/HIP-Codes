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

#Set Servo Frequency, Pulse WIdth, & Duty Cycles
freqPWM = 50.0 # PWM frequency in Hertz, should match PWM initialization
dutyCycleMin = 2.0 # duty cycle in percent for 0-degree servo position
dutyCycleMax = 11.8 # duty cycle in percent for 180-degree servo position

# periodMS is the PWM period in milliseconds
periodMS = (1.0 / freqPWM) * 1000.0
print("periodMS", periodMS)

# pulse width in milliseconds for 0-degree servo position
pulseMinMS = (dutyCycleMin / 100.0) * periodMS
print("pulseMinMS", pulseMinMS)

# pulse width in milliseconds for 180-degree servo position
pulseMaxMS = (dutyCycleMax / 100.0) * periodMS
print("pulseMaxMS", pulseMaxMS)

#Set pin 13 (for Solenoid) as an output pin
GPIO.setup(13, GPIO.OUT)

