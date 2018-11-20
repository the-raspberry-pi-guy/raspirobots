import gpiozero
import cwiid
import time
from rpi_ws281x import *

robot = gpiozero.Robot(left=(17,18), right=(27,22))

print("Press and hold the 1+2 buttons on your Wiimote simultaneously")
wii = cwiid.Wiimote()
print("Connection established")
wii.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_ACC

LED_COUNT      = 8
LED_PIN        = 10
LED_FREQ_HZ    = 800000
LED_DMA        = 10
LED_BRIGHTNESS = 150
LED_INVERT     = False
LED_CHANNEL    = 0
LED_STRIP      = ws.WS2811_STRIP_GRB

strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
strip.begin()

def colorWipe(strip, color, wait_ms=50):
	"""Wipe color across display a pixel at a time."""
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, color)
		strip.show()
		time.sleep(wait_ms/1000.0)

while True:
	buttons = wii.state["buttons"]
	if (buttons & cwiid.BTN_PLUS):
		colorWipe(strip, Color(255, 0, 0))  # Red wipe
	if (buttons & cwiid.BTN_HOME):
                colorWipe(strip, Color(0, 255, 0))  # Blue wipe
	if (buttons & cwiid.BTN_MINUS):
                colorWipe(strip, Color(0, 0, 255))  # Green wipe
	if (buttons & cwiid.BTN_B):
		colorWipe(strip, Color(0, 0, 0)) # Blank

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


