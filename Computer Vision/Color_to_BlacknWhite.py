import cv2
img = cv2.imread("C:\\Users\\DELL\\Desktop\\artificial-intelligence\\Computer Vision\\Python-logo.png") # Reading an color image
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # color to gray image
thresImg = cv2.threshold(grayImg,190,255,cv2.THRESH_BINARY)[1] # setting a threshold to gray scale Image
cv2.imwrite("Threshold_Img.png", thresImg) # saving the image
