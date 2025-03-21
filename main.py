from servo import*
import multiprocessing
import time

servopin1 = 11
servopin2 = 12

wheel, flipper = initialize_motors(servopin1, servopin2)

def handle_command(command):
    if command == "next":
        print("Activating servos...")
        turn_page(wheel, flipper)

if __name__ == "__main__":
    command_queue = multiprocessing.Queue()

    # Start recognize.py as a separate process
    recognize_process = multiprocessing.Process(target=start_listening, args=(command_queue,))
    recognize_process.start()

    try:
        while True:
            if not command_queue.empty():
                command = command_queue.get()
                handle_command(command)
            time.sleep(0.1)  # Prevent CPU overuse
    except KeyboardInterrupt:
        print("Shutting down...")
        servo_cleanup(servopin1, servopin2)
        recognize_process.terminate()
        recognize_process.join()