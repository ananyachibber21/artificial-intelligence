import cv2
import imutils

img = cv2.imread("C:\\Users\\DELL\\Desktop\\artificial-intelligence\\Computer Vision\\Python-logo.png")
resizeImg = imutils.resize(img,width=100)
cv2.imwrite("Resized_Image.png", resizeImg)