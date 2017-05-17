"""
Motor Control API

"""

import RPi.GPIO as GPIO
from PythonCode.pidrive.constants import *

# Setting GPIO to use Board Pin Numbering
GPIO.setmode(GPIO.BOARD)


class _DCMotor:

    """Generic Motor Control"""

    def __init__(self, pwm_pin, direction_pin, pwm_freq):
        self._pwm_pin = pwm_pin
        self._direction_pin = direction_pin
        self._pwm_freq = pwm_freq
        # Setting up PWM pin used for setting motor speed, initialising to off.
        GPIO.setup(self._pwm_pin, GPIO.OUT, initial=GPIO.LOW)
        # Setting up forward/reverse pin where ON = forward and OFF = reverse, initializing to forward.
        GPIO.setup(self._direction_pin, GPIO.OUT, initial=GPIO.HIGH)
        self._motor_pwm = GPIO.PWM(self._pwm_pin, self._pwm_freq)  # object for PWM output
        self._motor_pwm.start(0)  # Starting PWM with a duty cycle of 0 = motor stopped.

    def _set_pwm_freq(self, freq):
        """Set the frequency of the PWM output in Hz

        :param freq: The desired PWM frequency in Hz
        """
        self._pwm_freq = freq
        self._motor_pwm.ChangeFrequency(self._pwm_freq)

    def set_speed(self, speed):
        """Set motor speed on a scale from 0-100% of maximum speed

        :param speed: Percentage of full motor speed, accepts values from 0-100.
        """
        new_speed = speed
        # scale speedControl 0-100% ???
        if new_speed <= 0:
            self.stop()
        else:
            if new_speed > 100:
                new_speed = 100
            self._motor_pwm.ChangeDutyCycle(new_speed)

    def stop(self):
        """Stop all motor movement"""
        self._motor_pwm.changeDutyCycle(0)
        # self.motor_pwm.stop()  # stops the PWM output, would need to start back up again

    def set_forward(self):
        """Set the motor polarity for forward movement"""
        GPIO.output(self._direction_pin, 1)  # controls relay board to switch between NO/NC contacts

    def set_reverse(self):
        """Set the motor polarity for reverse movement"""
        GPIO.output(self._direction_pin, 0)  # controls relay board to switch between NO/NC contacts


class DriveMotor(_DCMotor):

    """Provides Controls for the Drive Motors On the Raspberry Drive"""

    def __init__(self):
        # Initializing relay board power pin and powering on. This must remain on for the board to function.
        GPIO.setup(DRIVE_RELAY_BOARD_POWER_PIN, GPIO.OUT, initial=GPIO.HIGH)
        super().__init__(pwm_pin=DRIVE_MOTOR_PWM_OUT_PIN,
                         direction_pin=DRIVE_MOTOR_DIRECTION,
                         pwm_freq=DRIVE_MOTOR_PWM_FREQUENCY)