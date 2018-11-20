import gpiozero

button = gpiozero.Button(17)

while True:
	if button.is_pressed:
		print("Button is pressed!")
	else:
		print("Button is not pressed!")
