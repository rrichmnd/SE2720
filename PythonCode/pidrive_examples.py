from PythonCode import pidrive

"""Using the Drive Motor"""
# Our current configuration has us operating both motors with a single output,
#  so any command given with the DriveMotor class will effect both motors simultaneously
# First you must instantiate the Drive Motor class:
drive_motor = pidrive.DriveMotor()
# You can set the speed from 0-100% of maximum using the set_speed method as shown below
drive_motor.set_speed(100)  # Setting the motor speed to max
# You can set the motor drive direction using the following methods:
drive_motor.set_forward()
drive_motor.set_reverse()


"""Using the Steering Servo"""
# Instantiate the SteeringServo class:
steering_servo = pidrive.SteeringServo()
# You can set the angle of the wheels between 0 and 180 degrees,
#  where 0 deg = Hard Left and 180 deg = Hard Right
steering_servo.set_angle(90)  # Setting wheels to center at 90 deg


"""Using the Range Finding Sensors"""
# The RangeFinder class will allow you to interact with all of the ultrasonic sensors.
# First you must instantiate the RangeFinder class:
sensors = pidrive.RangeFinders()
# You can then get distance data from any of the sensors by calling that sensors respective method:
# Each of the below methods returns a distance reading in centimeters (cm)
front_distance = sensors.get_front_distance()
rear_distance = sensors.get_rear_distance()
left_distance = sensors.get_left_distance()
right_distance = sensors.get_right_distance()

