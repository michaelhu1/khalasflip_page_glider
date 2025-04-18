from servo import*
from recognition import*
import multiprocessing
import time
import sys
import RPi.GPIO as GPIO

#set pin numbers
servopin1 = 11
servopin2 = 12
buttonpin = 10

wheel, flipper = initialize_motors(servopin1, servopin2)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(buttonpin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def handle_command(command):
    if command == "next":
        print("Activating servos...")
        turn_page(wheel, flipper)
    if command == "stop":
        print("Exiting...")
        sys.exit()

if __name__ == "__main__":
    command_queue = multiprocessing.Queue()

    # Start recognize.py as a separate process\
    recognize_process = multiprocessing.Process(target=start_listening, args=(command_queue,))
    recognize_process.start()

    try:
        while True:
            if not command_queue.empty():
                command = command_queue.get()
                handle_command(command)
            time.sleep(0.1)  # Prevent CPU overuse
            if GPIO.input(buttonpin) == GPIO.HIGH:
                print("Button pressed, turning page...")
                turn_page(wheel, flipper)
    except KeyboardInterrupt:
        print("Shutting down...")
        servo_cleanup(servopin1, servopin2)
        recognize_process.terminate()
        recognize_process.join()