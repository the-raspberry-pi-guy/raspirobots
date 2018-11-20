import gpiozero
import cwiid

robot = gpiozero.Robot(left=(17,18), right=(27,22))

print("Press and hold the 1+2 buttons on your Wiimote simultaneously")
wii = cwiid.Wiimote()
print("Connection established")
wii.rpt_mode = cwiid.RPT_BTN

while True:
	buttons = wii.state["buttons"]

	if (buttons & cwiid.BTN_LEFT):
		robot.left()
	if (buttons & cwiid.BTN_RIGHT):
		robot.right()
	if (buttons & cwiid.BTN_UP):
		robot.forward()
	if (buttons & cwiid.BTN_DOWN):
		robot.backward()
	if (buttons & cwiid.BTN_B):
		robot.stop()
