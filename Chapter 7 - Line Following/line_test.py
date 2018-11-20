import gpiozero
import time

line_sensor = gpiozero.DigitalInputDevice(9)

while True:
	if line_sensor.is_active == False:
		print("Line detected")
	else:
		print("No line detected")

	time.sleep(0.2)
