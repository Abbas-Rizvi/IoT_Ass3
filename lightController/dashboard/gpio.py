# gpio_control/gpio_controller.py
import RPi.GPIO as GPIO
import time

class GPIOController:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)

        # GPIO pins
        self.led_pin = 26
        self.ldr_pin = 16

        # Set up GPIO pins
        GPIO.setup(self.led_pin, GPIO.OUT)
        GPIO.setup(self.ldr_pin, GPIO.IN)

        # Initialize variables
        self.mode = 'manual'
        self.ldr_threshold = 500

        # Set the initial LED state
        self.turn_off_led()

    def set_led_state(self, state):
        GPIO.output(self.led_pin, state)

    def turn_on_led(self):
        self.set_led_state(GPIO.HIGH)

    def turn_off_led(self):
        self.set_led_state(GPIO.LOW)

    def toggle_mode(self):
        self.mode = 'auto' if self.mode == 'manual' else 'manual'
        if self.mode == 'auto':
            self.auto_mode()

    def auto_mode(self):
        while self.mode == 'auto':
            ldr_value = GPIO.input(self.ldr_pin)
            if ldr_value > self.ldr_threshold:
                self.turn_on_led()
            else:
                self.turn_off_led()
            time.sleep(1)

# Create an instance of the GPIOController
gpio_controller = GPIOController()
