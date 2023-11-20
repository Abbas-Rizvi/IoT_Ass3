# gpio_control/gpio_controller.py
import RPi.GPIO as GPIO
import time

# Initialize GPIO
GPIO.setmode(GPIO.BCM)

# GPIO pins
led_pin = 26
ldr_pin = 16

# Set up GPIO pins
GPIO.setup(led_pin, GPIO.OUT)
GPIO.setup(ldr_pin, GPIO.IN)

# Initialize variables
mode = 'manual'
ldr_threshold = 500

# Set the initial LED state
GPIO.output(led_pin, GPIO.HIGH)

def set_led_state(state):
    GPIO.output(led_pin, state)

def turn_on_led():
    set_led_state(GPIO.HIGH)

def turn_off_led():
    set_led_state(GPIO.LOW)

def toggle_mode():
    global mode
    mode = 'auto' if mode == 'manual' else 'manual'
    if mode == 'auto':
        auto_mode()

def auto_mode():
    while True:  # Changed to a continuous loop
        ldr_value = GPIO.input(ldr_pin)
        if ldr_value > ldr_threshold:
            turn_on_led()
        else:
            turn_off_led()
        time.sleep(1)