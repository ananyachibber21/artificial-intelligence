import cv2
img = cv2.imread("C:\\Users\\DELL\\Desktop\\artificial-intelligence\\Computer Vision\\Python-logo.png") # Step 1 - Reading an image from the directory
cv2.imwrite("New-logo.png",img) # Step 2 - Save the image in a new file
cv2.imshow("New Python Logo",img) # Step 3 - Displaying the image
cv2.waitKey(0)
cv2.destroyAllWindows()