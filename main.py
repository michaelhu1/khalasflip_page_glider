from servo import*
import multiprocessing
import time

def handle_command(command):
    if command == "next":
        print("Activating servos...")
        # Replace this with actual servo control code
        # Example: servo_controller.turn_page()

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
        recognize_process.terminate()
        recognize_process.join()