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
    return flipper, wheel 
    
def turn_page(wheel, flipper):
    wheel.ChangeDutyCycle(12)     
    sleep(1)                 
    flipper.ChangeDutyCycle(12)    
    sleep(1)

def servo_cleanup(wheel, flipper):

    # Clean up everything
    wheel.stop()   
    flipper.stop()             
    GPIO.cleanup()        