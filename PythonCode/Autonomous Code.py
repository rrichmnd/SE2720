from PythonCode import pidrive
from random import randint


def MoveForward():
    #Insert Code for car to move forward
    drive_motor.set_forward()
    steering_servo.set_angle(90)
    drive_motor.set_speed(100)
def TurnLeft():
    #Insert Code for car to turn left
    Stop()
    drive_motor.set_forward()
    steering_servo.set_angle(45)
    drive_motor.set_speed(100)
def TurnRight():
    #Insert Code for car to turn right
    Stop()
    drive_motor.set_forward()
    steering_servo.set_angle(135)
    drive_motor.set_speed(100)
def Backup():
    #Insert Code for car to move backwards
    #Should also be able to turn car to the left or right
    drive_motor.set_reverse()
    drive_motor.set_speed(100)
def Stop():
    drive_motor.set_speed(0)

drive_motor = pidrive.DriveMotor()
sensors = pidrive.RangeFinders()
steering_servo = pidrive.SteeringServo()
steering_servo.set_angle(90)

Sensor_Front = sensors.get_front_distance()
Sensor_Back  = sensors.get_rear_distance()
Sensor_Left  = sensors.get_left_distance()
Sensor_Right = sensors.get_right_distance()

Object_Detected = True

# An object 10cm away will not be driven towards
Detected_Distance = 10;
Front = False;
Back  = False;
Left  = False;
Right = False;

if Sensor_Front > Detected_Distance:
    Front = Object_Detected
if Sensor_Back > Detected_Distance:
    Back = Object_Detected
if Sensor_Left > Detected_Distance:
    Left = Object_Detected
if Sensor_Right > Detected_Distance:
    Right = Object_Detected

if (Front and Back and Left and Right):
    Stop()
elif (Front and Back and Left):
    Stop()
elif (Front and Back and Right):
    Stop()
elif (Front and Left and Right):
    #Backup
    Backup()
elif (Back and Left and Right):
    #Move Forward
    MoveForward()
elif (Front and Back):
    Stop()
elif (Left and Right):
    #Move Forward
    MoveForward()
elif (Front and Right):
    #Turn Left
    TurnLeft()
elif (Front and Left):
    #Turn Right
    TurnRight()
elif (Back and (Left or Right)):
    #Move Forward
    MoveForward()
elif Front:
    #Turn Left or Right
    choice  = randint(0,1)
    if choice == 0
        TurnLeft()
    else:
        TurnRight()
else:
    #Move Forward
    MoveForward()
