from servo import*
import multiprocessing
import time

servopin1 = 11
servopin2 = 13

wheel, flipper = initialize_motors(servopin1, servopin2)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
    if GPIO.input(10) == GPIO.HIGH:
        print("Activating servos...")
        turn_page(wheel, flipper)
    time.sleep(0.1)
    