"""
Servo Control API

"""

import RPi.GPIO as GPIO
from PythonCode.pidrive.constants import *

# Setting GPIO to use Board Pin Numbering
GPIO.setmode(GPIO.BOARD)


class _ServoMotor:

    """Generic Servo Control"""

    def __init__(self, pwm_pin):
        self._pwm_pin = pwm_pin
        self._pwm_freq = SERVO_PWM_FREQUENCY  # Frequency of the PWM output
        self._servo_pwm = GPIO.PWM(self._pwm_pin, self._pwm_freq)
        self._servo_pwm.start(7.5)  # Initialize to 90 deg angle (wheels facing forward)

        # Servo min max duty cycles
        self._dc_min = 2
        self._dc_max = 12

    def set_angle(self, angle):
        """Set the angle of the servo motor to input angle in degrees

        :param angle: Desired servo angle in degrees (0-180)
        """
        new_angle = angle

        # Declaring conversion constants
        angle_min = 0
        angle_max = 180
        angle_range = angle_max - angle_min
        dc_range = self._dc_max - self._dc_min

        # Enforcing angle range
        if new_angle > angle_max:
            new_angle = angle_max
        elif new_angle < angle_min:
            new_angle = angle_min

        # Scaling input angle to an appropriate duty cycle
        duty_cycle = ((dc_range / angle_range) * (new_angle - angle_min)) + self._dc_min

        self._servo_pwm.changeDutyCycle(duty_cycle)


class SteeringServo(_ServoMotor):

    """Provides Controls for the Servo Motor Used to Steer the Car"""

    def __init__(self):
        super().__init__(pwm_pin=SERVO_PWM_OUT_PIN)
