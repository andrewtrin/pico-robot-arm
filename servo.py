# servo.py

import machine

class Servo:
    # A class to control a standard SG90 servo motor.

    def __init__(self, pin):
        self.pwm = machine.PWM(machine.Pin(pin))
        self.pwm.freq(50)
        self._MIN_DUTY = 1350  # The pulse width for 0 degrees
        self._MAX_DUTY = 8200  # The pulse width for 180 degrees

    def _angle_to_duty(self, angle):
        # A private helper method to convert an angle into a duty value.
        # This maps the angle range (0-180) to the duty range.
        return int(self._MIN_DUTY + (self._MAX_DUTY - self._MIN_DUTY) * (angle / 180))

    def move_to_angle(self, angle):
        # Moves the servo to a specific angle between 0 and 180.
        if 0 <= angle <= 180:
            duty = self._angle_to_duty(angle)
            self.pwm.duty_u16(duty)
        else:
            print("Error: Angle must be between 0 and 180.")

    def deinit(self):
        # Turns the servo off to save power and prevent jitter.
        self.pwm.deinit()