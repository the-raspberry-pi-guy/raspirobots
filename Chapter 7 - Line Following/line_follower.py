import gpiozero

SPEED = 0.25

robot = gpiozero.Robot(left=(17,18), right=(27,22))

left = gpiozero.DigitalInputDevice(9)
right = gpiozero.DigitalInputDevice(11)

while True:
	if (left.is_active == True) and (right.is_active == True):
		robot.forward(SPEED)
	elif (left.is_active == False) and (right.is_active == True):
		robot.right(SPEED)
	elif (left.is_active == True) and (right.is_active == False):
		robot.left(SPEED)
	else:
		robot.stop()
