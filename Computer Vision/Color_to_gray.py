import cv2
img = cv2.imread("C:\\Users\\DELL\\Desktop\\artificial-intelligence\\Computer Vision\\Python-logo.png") # Reading an color image
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # color to gray image
cv2.imwrite("Gray_image.png",grayImg) # write and save the gray image 
cv2.imshow("Color",img) # Displaying the color image
cv2.imshow("Gray",grayImg) # Displaying the gray image
cv2.waitKey(0)
cv2.destroyAllWindows()