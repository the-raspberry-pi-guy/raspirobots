import cwiid
import time

print("Press and hold the 1+2 buttons on your Wiimote simultaneously")
wii = cwiid.Wiimote()
print("Connection established")
wii.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_ACC

while True:
	print(wii.state['acc'])
	time.sleep(0.01)
