from servo import *
import RPi.GPIO as GPIO
import time

# Pin definitions
servopin1 = 11
servopin2 = 13
buttonpin = 10

# GPIO setup
GPIO.setmode(GPIO.BOARD)
GPIO.setup(buttonpin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Initialize motors
flipper, wheel = initialize_motors(servopin1, servopin2)

# Define duty cycle limits and increment
# Adjust these based on your servo's specifications (common servos use approx. 2.5-12.5 for 0-180°)
min_duty = 2.5  
max_duty = 12.5  
angle_increment = 1.0  # amount to increment per button press
current_wheel_duty = min_duty  # starting duty cycle

def move_wheel_by(increment):
    global current_wheel_duty
    # Compute the new duty cycle
    new_duty = current_wheel_duty + increment
    # Clamp the value within the allowed range
    if new_duty > max_duty:
        new_duty = max_duty
    elif new_duty < min_duty:
        new_duty = min_duty
    print(f"Moving wheel from {current_wheel_duty} to {new_duty}")
    wheel.ChangeDutyCycle(new_duty)
    # Optionally, you might want to pause briefly to allow the servo to move
    time.sleep(0.5)
    current_wheel_duty = new_duty

# For button edge detection
prev_button_state = GPIO.LOW

try:
    while True:
        # Read the current button state
        button_state = GPIO.input(buttonpin)
        # Check for a rising edge: currently HIGH and previously LOW
        if button_state == GPIO.HIGH and prev_button_state == GPIO.LOW:
            print("Button pressed. Activating servo...")
            move_wheel_by(angle_increment)
            # Debounce delay
            time.sleep(0.2)
        prev_button_state = button_state
        time.sleep(0.1)

except KeyboardInterrupt:
    print("Cleaning up servos and GPIO...")
    servo_cleanup(wheel, flipper)