import gpiozero
import cwiid

robot = gpiozero.Robot(left=(17,18), right=(27,22))

print("Press and hold the 1+2 buttons on your Wiimote simultaneously")
wii = cwiid.Wiimote()
print("Connection established")
wii.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_ACC

while True:
	x = (wii.state["acc"][cwiid.X] - 95) - 25
	y = (wii.state["acc"][cwiid.Y] - 95) - 25

	if x < -25:
		x = -25
	if y < -25:
		y = -25
	if x > 25:
		x = 25
	if y > 25:
		y = 25

	forward_value = (float(x)/50)*2
	turn_value = (float(y)/50)*2

	if (turn_value < 0.3) and (turn_value > -0.3):
		robot.value = (forward_value, forward_value)
	else:
		robot.value = (-turn_value, turn_value)


