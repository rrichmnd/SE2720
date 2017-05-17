import RPi.GPIO as GPIO
import xbox #xbox drivers need to be downloaded

#Variable to pin mapping
driveMotorPWMOut = 32
steerMotorPWMOut = 33
driveMotorDirection = 18
FrontSensorOut = 3
FrontSensorIn = 5
LeftSensorOut = 7
LeftSensorIn = 8
RightSensorOut = 10
RightSensorIn = 11
RearSensorOut = 12
RearSensorIn = 13

PWM_Frequency = 100 #0-100hz value, can be varied if needed
CenterSteerVal = 50 #0-100 value, to be changed once center is found with servo motor
FullLeftSteerVal = 0 #0-100 value, to be changed once full left is found with servo motor
FullRightSteerVal = 100 #0-100 value, to be changed once full right is found with servo motor

#initialize joystick
joystick = xbox.Joystick()

L_X_Axis = joystick.leftX()
L_Y_Axis = joystick.leftY()
R_X_Axis = joystick.rightX()
R_Y_Axis = joystick.rightY()
buttonA = joystick.A()
buttonB = joystick.B()
buttonX = joystick.X()
buttonY = joystick.Y()
L_Trigger = joystick.leftTrigger()
R_Trigger = joystick.rightTrigger()
buttonBack = joystick.back()
buttonStart = joystick.start()
buttonLeft = joystick.leftBumper()
buttonRight = joystick.rightBumper()
buttonL_Stick = joystick.leftThumbstick()
buttonR_Stick = joystick.rightThumbstick()



#GPIO using board numbering
GPIO.setmode(GPIO.BOARD)

#GPIO Signal setup
#OUTPUTS
GPIO.setup(FrontSensorOut, GPIO.OUT) #FRONT SENSOR TRIGGER
GPIO.setup(LeftSensorOut, GPIO.OUT) #LEFT SENSOR TRIGGER
GPIO.setup(RightSensorOut, GPIO.OUT) #RIGHT SENSOR TRIGGER
GPIO.setup(RearSensorOut, GPIO.OUT) #REAR SENSOR TRIGGER
GPIO.setup(driveMotorDirection, GPIO.OUT) #FWD/REV Relay control, on = FWD, off = REV
GPIO.setup(driveMotorPWMOut, GPIO.OUT) #PWM motor command for drive motor
GPIO.setup(steerMotorPWMOut, GPIO.OUT) #PWM command for steering Servo

#INPUTS
GPIO.setup(FrontSensorIn, GPIO.IN) #FRONT SENSOR RETURN
GPIO.setup(LeftSensorIn, GPIO.IN) #LEFT SENSOR RETURN
GPIO.setup(RightSensorIn, GPIO.IN) #RIGHT SENSOR RETURN
GPIO.setup(RearSensorIn, GPIO.IN) #REAR SENSOR RETURN

motor = GPIO.PWM(driveMotorPWMOut, PWM_Frequency) #object for PWM output
steer = GPIO.PWM(steerMotorPWMOut, PWM_Frequency) #object for PWM output

steer.start(CenterSteerVal)


#driveForward()
#controls the relay board to swith polarity of the motor output
#relay ON = forward, OFF = reverse
#uses controlMotorSpeed() to control the PWM output based on the speedControl input to the function
def driveForward(inputSignal)	
	GPIO.output(driveMotorDirection, 1)#controls relay board to switch between NO/NC contacts
	controlMotorSpeed(speedControl)

#driveReverse()
#controls the relay board to swith polarity of the motor output
#relay ON = forward, OFF = reverse
#uses controlMotorSpeed() to control the PWM output based on the speedControl input to the function	
def driveReverse(inputSignal)
	GPIO.output(driveMotorDirection, 0)#controls relay board to switch between NO/NC contacts
	controlMotorSpeed(speedControl)
	
#controlMotorSpeed()
#takes a scaled 0-100 input (speedControl)
#changes the PWM output duty cycle in a 1:1 ratio from the speedControl input
#additional scaling and acceleration control to be added later, basic setup initially. 
def controlMotorSpeed(speedControl)
	#scale speedControl 0-100%
	motor.start(0) #start PWM output at 0%
	while speedControl != 0:
		motor.changeDutyCycle(speedControl) #sets the duty cycle equal to the speedControl input which should be scaled 0-100
	
	if speedControl = 0:
		motor.stop() #stops the PWM output
		
def controlSteering(steerControl)
	#1.0 ms = 0 degree (Left)
	#1.5 ms = 90 degree (Center)
	#2.0 ms = 180 degree (Right)
	#steerControl scaled 0-100 input
	
	steerRange = FullRightSteerValue - FullLeftSteerValue #determine actual steering value range
	
	steerValue = FullLeftSteerValue + steerRange * (steerControl/100)
	
	steer.changeDutyCycle(steerValue)
		
	
		
	
	
		

