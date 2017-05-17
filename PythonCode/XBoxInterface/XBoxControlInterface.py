#using the XboxController.py module developed by Martin O'Hanlon
#interfacing this with the pidrive module developed by Dan Holland

from PythonCode import pidrive
from PythonCode.XBoxInterface.XboxControllerMaster import XboxInterface
from enum import Enum

driveMotor = pidrive.DriveMotor()
steerServo = pidrive.SteeringServo()

xboxControl.start()
controlScheme = ControlType.TriggerLeft #default

#Default controls will be triggers for spped and F/R direction control, Right = FWD, Left = REV
#Left Joystick X axis for steering.

#********************************************************************************************
#mainCallback
#An event listener for all button events from xboxControl
#controlId = button, trigger or lever that is sending the signal
#value = scaled valued from xboxControl
#
#Not currently used as buttons we intend to use have dedicated call back
#could be used in the future for limited button usage. 
#********************************************************************************************
def mainCallback(controlId, value):
	#do nothing at this point, can be used in the future.
	#All buttons without dedicated event handlers are listed below. 
	if controlId == xboxControl.XboxControls.A:
		pass #this button has no function at this time
	elif controlId == xboxControl.XboxControls.B:	
		pass #this button has no function at this time
	elif controlId == xboxControl.XboxControls.X:
		pass #this button has no function at this time
	elif controlId == xboxControl.XboxControls.Y:
		pass #this button has no function at this time
	elif controlId == xboxControl.XboxControls.LB:
		pass #this button has no function at this time
	elif controlId == xboxControl.XboxControls.RB:
		pass #this button has no function at this time
	elif controlId == xboxControl.XboxControls.BACK:
		pass #this button has no function at this time
	elif controlId == xboxControl.XboxControls.START:
		pass #this button has no function at this time
	elif controlId == xboxControl.XboxControls.LEFTTHUMB:
		pass #this button has no function at this time
	elif controlId == xboxControl.XobxControls.RIGHTTHUMB:
		pass #this button has no function at this time
	else:
		if controlId != xboxControl.XboxControls.XBOX or controlId != xboxControl.XboxControls.RTRIGGER \
		or controlId != xboxControl.XboxControls.LTRIGGER or controlId != xboxControl.XboxControls.LTHUMBX \
		or controlId != xboxControl.XboxControls.LTHUMBY or controlId != xboxControl.XboxConttrols.RTHUMBX \
		or controlId != xboxControl.XboxControls.RTHUMBY:
			print ("Unknown button press.")
 
#********************************************************************************************
#xboxButtonCallback
#An event listener dedicated to the xbox button
#value = 0 or 1 indicating if button was pressed. 
#
#Pressing the xbox button will stop the use of XBox controller. 
#********************************************************************************************
def xboxButtonCallback(value):
	if value == 1:
	   xboxControl.stop()
	
#********************************************************************************************
#rightTriggerCallback
#An event listener dedicated to the right trigger input
#This function is only useable if the trigger input is configured as analog and not a button
#value = 0 - 100 value to be used for speed control of drive motor
#
#Trigger value will act like an accelerator in a vehicle.
#********************************************************************************************
def rightTriggerCallback(value):
	if controlScheme == ControlType.Triggerleft or controlScheme == ControlType.TriggerRight:
		#FWD Control
		while value != 0:
			driveMotor.set_forward()
			driveMotor.set_speed(value)

#*********************************************************************************************
#leftTriggerCallback
#An event listener dedicated to the left trigger input
#This function is only useable if the trigger input is configured as analog and not a button
#value = 0 - 100 value to be used for speed control of drive motor
#
#Trigger value will act like an accelerator in a vehicle.
#*********************************************************************************************		
def leftTriggerCallback(value):
	if controlScheme == ControlType.Triggerleft or controlScheme == ControlType.TriggerRight:
		#REV Control
		while value != 0:
			driveMotor.set_reverse()
			driveMotor.set_speed(value)
	
#*********************************************************************************************
#leftJoystickXCallback
#An event listener dedicated to the left Joystick X axis input
#value = -100 - 100 value scaled from xboxControl
#
#Value is converted percentage input that is then applied to the 90 degree range output 
#to the steering servo. 
#0 - 100 is from 90 to 180 degrees for right turn
#-100 - 0 is from 0 to 90 degrees for left turn
#*********************************************************************************************
def leftJoystickXCallback(value):
	if controlScheme == ControlType.TriggerLeft or controlScheme == ControlType.RightSpeed or controlScheme == ControlType.LeftAll:
	   #Left Joystick X Value
		while value != 0:
			if value < 0:
				scale = value/100 * -1
				steerCmd = 90 * scale
				steerServo.set_angle(90 - steerCmd)
			else:
				scale = value/100
				steerCmd = 90 * scale
				steerServo.set_angle(90 + steerCmd)
		
	

#********* BELOW FUNCTIONS FOR POSSIBLE FUTURE USE WITH DIFFERENT CONTROL SCHEMES ***********
"""
#*********************************************************************************************
#leftJoystickYCallback
#An event listener dedicated to the left Joystick Y axis input
#value = -100 - 100 value scaled from xboxControl
#
#Value is used for speed control, negative value is reverse, positive is forward
#*********************************************************************************************
def leftJoystickYCallback(value):
	if controlScheme == ControlType.LeftSpeed or controlScheme == ControlType.LeftAll:
		while value != 0:
			if value is > 0: 
				driveMotor.set_forward()
				driveMotor.set_speed(value)
			else:
				driveMotor.set_direction()
				driveMotor.set_speed(value)
	
#*********************************************************************************************
#leftJoystickXCallback
#An event listener dedicated to the left Joystick X axis input
#value = -100 - 100 value scaled from xboxControl
#
#Value is converted percentage input that is then applied to the 90 degree range output 
#to the steering servo. 
#0 - 100 is from 90 to 180 degrees for right turn
#-100 - 0 is from 0 to 90 degrees for left turn
#*********************************************************************************************
def rightJoystickXCallback(value):
	if controlScheme == ControlType.TriggerRight or controlScheme == ControlType.LeftSpeed or controlScheme == ControlType.RightAll:
		while value != 0:
			if value is < 0:
				scale = value/100 * -1
				steerCmd = 90 * scale
				steerServo.set_angle(90 - steerCmd)
			else:
				scale = value/100
				steerCmd = 90 * scale
				steerServo.set_angle(90 + steerCmd)
	
#*********************************************************************************************
#rightJoystickYCallback
#An event listener dedicated to the right Joystick Y axis input
#value = -100 - 100 value scaled from xboxControl
#
#Value is used for speed control, negative value is reverse, positive is forward
#*********************************************************************************************
def rightJoystickYCallback(value):
	if controlScheme == ControlType.RightSpeed or controlScheme == ControlType.RightAll:
		while value != 0:
			if value is > 0: 
				driveMotor.set_forward()
				driveMotor.set_speed(value)
			else:
				driveMotor.set_direction()
				driveMotor.set_speed(value)
"""	

#ControlType is an Enumeration class that can be used for future control schemes if they're implemented.
class ControlType(Enum):
	TriggerLeft = 1
	TriggerRight = 2
	RightSpeed = 3
	LeftSpeed = 4
	RightAll = 5
	LeftAll = 6
	
xboxControl = XboxController.XboxController(
	controllerCallBack = mainCallBack, 
	joystickNo = 1, #one joystick for steering
	deadzone = 0.1, #may need to be adjusted in testing
	scale = 100, #scale analog signals will use - x to x
	invertYAxis = True) #Y axis is init as -1 being up.
	
#Setup individual call backs for buttons we will be using, can be expanded later as needed
xboxControl.setupControlCallback(xboxControl.XboxControls.XBOX, xboxButtonCallback)
xboxControl.setupControlCallBack(xboxControl.XboxControls.RTRIGGER, rightTriggerCallback)
xboxControl.setupControlCallBack(xboxControl.XboxControls.LTRIGGER, leftTriggerCallback)
xboxControl.setupControlCallBack(xboxControl.XboxControls.LTHUMBX, leftJoystickXCallback)
xboxControl.setupControlCallBack(xboxControl.XboxControls.LTHUMBY, leftJoystickYCallback)
xboxControl.setupControlCallBack(xboxControl.XboxControls.RTHUMBX, rightJoystickXCallback)
xboxControl.setupControlCallBack(xboxControl.XboxControls.RTHUMBY, rightJoystickYCallback)
