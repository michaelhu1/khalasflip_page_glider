import RPi.GPIO as GPIO
from time import sleep


def initialize_motors(servo1, servo2):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(servo1,GPIO.OUT)  
    flipper = GPIO.PWM(servo1, 50)    
    GPIO.setup(servo2,GPIO.OUT)  
    wheel = GPIO.PWM(servo2, 50)     
    wheel.start(0)
    flipper.start(0)    
    sleep(1)  
    return flipper, wheel 
    
def turn_flipper(flipper):
    print("spinning flipper")
    flipper.ChangeDutyCycle(7.5)  

def turn_wheel(wheel):
    print("spinning wheel")
    wheel.ChangeDutyCycle(6.5) 

def motoroff(wheel, flipper):
    print("motors off")
    wheel.ChangeDutyCycle(0)
    flipper.ChangeDutyCycle(0) 

def servo_cleanup(wheel, flipper):
    wheel.stop()   
    flipper.stop()             
    GPIO.cleanup()        

def turn_page(wheel, flipper):
    print("button pressed")
    turn_wheel(wheel)
    sleep(0.75)
    motoroff(wheel,flipper)
    turn_flipper(flipper)
    sleep(1.1)
    motoroff(wheel,flipper)