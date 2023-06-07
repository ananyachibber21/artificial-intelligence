import cv2

img = cv2.imread("C:\\Users\\DELL\\Desktop\\artificial-intelligence\\Computer Vision\\Python-logo.png")
gaussianBlurImg = cv2.GaussianBlur(img,(25,25),0)
cv2.imwrite("Gaussian_Image.png", gaussianBlurImg)