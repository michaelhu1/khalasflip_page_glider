from servo import *
import RPi.GPIO as GPIO
import time

servopin1 = 11
servopin2 = 13
buttonpin = 10

GPIO.setmode(GPIO.BOARD)
GPIO.setup(buttonpin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

flipper, wheel = initialize_motors(servopin1, servopin2)

try:
    while True:
        if GPIO.input(10) == GPIO.HIGH:
            print("button pressed")
            turn_wheel(wheel)
            time.sleep(0.75)
            motoroff(wheel,flipper)
            turn_flipper(flipper)
            time.sleep(1.1)
            motoroff(wheel,flipper)
        time.sleep(0.5)
        


except KeyboardInterrupt:
    print("Cleaning up servos and GPIO...")
    servo_cleanup(wheel, flipper)