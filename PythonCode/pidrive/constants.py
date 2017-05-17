"""
Raspberry Drive constants, contains:
    * GPIO pinout mapping for Motors and Sensors
    * Default PWM Frequencies
"""

# Drive Motor
DRIVE_MOTOR_PWM_OUT_PIN = 32  # PWM for drive motors
DRIVE_RELAY_BOARD_POWER_PIN = 40  # Pin that powers the relay board that controls the motors
DRIVE_MOTOR_PWM_FREQUENCY = 100  # PWM Frequency in Hz
DRIVE_MOTOR_DIRECTION = 18  # FWD/REV Relay control
# Steering Servo
SERVO_PWM_OUT_PIN = 33
SERVO_PWM_FREQUENCY = 50
# Sensors
FRONT_SENSOR_TRIGGER_PIN = 3
FRONT_SENSOR_ECHO_PIN = 5
LEFT_SENSOR_TRIGGER_PIN = 7
LEFT_SENSOR_ECHO_PIN = 8
RIGHT_SENSOR_TRIGGER_PIN = 10
RIGHT_SENSOR_ECHO_PIN = 11
REAR_SENSOR_TRIGGER_PIN = 12
REAR_SENSOR_ECHO_PIN = 13
