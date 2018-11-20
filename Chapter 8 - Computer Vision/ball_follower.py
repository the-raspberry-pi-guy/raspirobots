from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2
import numpy as np
import gpiozero

camera = PiCamera()
image_width = 640
image_height = 480
camera.resolution = (image_width, image_height)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(image_width, image_height))
center_image_x = image_width / 2
center_image_y = image_height / 2
minimum_area = 250
maximum_area = 100000

robot = gpiozero.Robot(left=(17,18), right=(27,22))
forward_speed = 0.3
turn_speed = 0.25

HUE_VAL = 28

lower_color = np.array([HUE_VAL-10,100,100])
upper_color = np.array([HUE_VAL+10, 255, 255])

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	image = frame.array

	hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

	color_mask = cv2.inRange(hsv, lower_color, upper_color)

	image2, countours, hierarchy = cv2.findContours(color_mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

	object_area = 0
	object_x = 0
	object_y = 0

	for contour in countours:
		x, y, width, height = cv2.boundingRect(contour)
		found_area = width * height
		center_x = x + (width / 2)
		center_y = y + (height / 2)
		if object_area < found_area:
			object_area = found_area
			object_x = center_x
			object_y = center_y
	if object_area > 0:
		ball_location = [object_area, object_x, object_y]
	else:
		ball_location = None

	if ball_location:
		if (ball_location[0] > minimum_area) and (ball_location[0] < maximum_area):
			if ball_location[1] > (center_image_x + (image_width/3)):
				robot.right(turn_speed)
				print("Turning right")
			elif ball_location[1] < (center_image_x - (image_width/3)):
				robot.left(turn_speed)
				print("Turning left")
			else:
				robot.forward(forward_speed)
				print("Forward")
		elif (ball_location[0] < minimum_area):
			robot.left(turn_speed)
			print("Target isn't large enough, searching")
		else:
			robot.stop()
			print("Target large enough, stopping")
	else:
		robot.left(turn_speed)
		print("Target not found, searching")

	rawCapture.truncate(0)
