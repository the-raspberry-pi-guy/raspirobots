import gpiozero
import time

TRIG = 23
ECHO = 24

trigger = gpiozero.OutputDevice(TRIG)
echo = gpiozero.DigitalInputDevice(ECHO)

trigger.on()
time.sleep(0.00001)
trigger.off()

while echo.is_active == False:
	pulse_start = time.time()

while echo.is_active == True:
	pulse_end = time.time()

pulse_duration = pulse_end - pulse_start

distance = 34300 * (pulse_duration/2)

round_distance = round(distance,2)

print("Distance: ", round_distance)
