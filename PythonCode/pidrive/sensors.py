"""
Ultrasonic Sensor API

"""

import time
from PythonCode.pidrive.constants import *
import RPi.GPIO as GPIO

# Setting GPIO to use Board Pin Numbering
GPIO.setmode(GPIO.BOARD)


class _UltrasonicRangeFinder:

    """Generic class for interacting with an Ultrasonic Range Sensor"""

    def __init__(self, sensor_echo_pin, sensor_trigger_pin):
        self._sensor_echo_pin = sensor_echo_pin
        self._sensor_trigger_pin = sensor_trigger_pin
        GPIO.setup(self._sensor_echo_pin, GPIO.IN)
        GPIO.setup(self._sensor_trigger_pin, GPIO.OUT, initial=GPIO.LOW)

    def get_distance(self):
        """Get Distance Reading From UltraSonic Sensor in Centimeters (cm)

        :returns: Distance to target in cm
        """
        pulse_start = 0
        pulse_end = 0
        time_elapsed = 0
        distance = 0

        # Trigger pulse from sensor
        GPIO.output(self._sensor_trigger_pin, GPIO.HIGH)
        time.sleep(.00001)  # wait 0.01 ms
        GPIO.output(self._sensor_trigger_pin, GPIO.LOW)

        # Get leading edge of return pulse
        while GPIO.input(self._sensor_echo_pin) == GPIO.LOW:
            pulse_start = time.time()
        # Get trailing edge of return pulse
        while GPIO.input(self._sensor_echo_pin) == GPIO.HIGH:
            pulse_end = time.time()

        # Calculate time elapsed between when signal was sent and received
        time_elapsed = pulse_end - pulse_start
        # Distance = Time * Speed (Sonic speed = 34300cm/s)
        # Must also divide by 2 in order to account for travel time to and from the target.
        distance = (time_elapsed * 34300) / 2

        return distance


class _FrontSensor(_UltrasonicRangeFinder):

    """Ultrasonic range sensor facing out the front of the car"""

    def __init__(self):
        super().__init__(sensor_echo_pin=FRONT_SENSOR_ECHO_PIN,
                         sensor_trigger_pin=FRONT_SENSOR_TRIGGER_PIN)


class _RearSensor(_UltrasonicRangeFinder):

    """Ultrasonic range sensor facing out the rear of the car"""

    def __init__(self):
        super().__init__(sensor_echo_pin=REAR_SENSOR_ECHO_PIN,
                         sensor_trigger_pin=REAR_SENSOR_TRIGGER_PIN)


class _LeftSensor(_UltrasonicRangeFinder):

    """Ultrasonic range sensor facing out the left side of the car"""

    def __init__(self):
        super().__init__(sensor_echo_pin=LEFT_SENSOR_ECHO_PIN,
                         sensor_trigger_pin=LEFT_SENSOR_TRIGGER_PIN)


class _RightSensor(_UltrasonicRangeFinder):

    """Ultrasonic range sensor facing out the right side of the car"""

    def __init__(self):
        super().__init__(sensor_echo_pin=RIGHT_SENSOR_ECHO_PIN,
                         sensor_trigger_pin=RIGHT_SENSOR_TRIGGER_PIN)


class RangeFinders:

    """This class grants access to all of the pi-drives range finding sensors"""

    def __init__(self):
        self._front_sensor = _FrontSensor()
        self._rear_sensor = _RearSensor()
        self._left_sensor = _LeftSensor()
        self._right_sensor = _RightSensor()

    def get_front_distance(self):
        return self._front_sensor.get_distance()

    def get_rear_distance(self):
        return self._rear_sensor.get_distance()

    def get_left_distance(self):
        return self._left_sensor.get_distance()

    def get_right_distance(self):
        return self._right_sensor.get_distance()


