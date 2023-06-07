# import the opencv library
import cv2

# initialize camera
vid = cv2.VideoCapture(0)

while(True): # infinite loop
	
	# Reading the frame from camera
	_, img = vid.read()

	# Show the frame
	cv2.imshow('VideoStream', img)
	
	key = cv2.waitKey(1) & 0xFF # Record the key press
	if key == ord('q'): # if the pressed key is q
		break # break the while loop

# After the loop release the camera
vid.release()
# Every opened output window will be closed
cv2.destroyAllWindows()
