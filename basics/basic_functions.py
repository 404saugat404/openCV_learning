#here we will learn to use basic functions that we use often in our project
import cv2 as cv

#read an img
img=cv.imread("/home/saugat/Desktop/openCV/Resources/Photos/park.jpg")
cv.imshow("park", img)

#converting to greystyle
grey_img=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("park", grey_img)

# Blur 
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Edge Cascade
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)

# Dilating the image
dilated = cv.dilate(canny, (7,7), iterations=3)
cv.imshow('Dilated', dilated)

# Eroding
eroded = cv.erode(dilated, (7,7), iterations=3)
cv.imshow('Eroded', eroded)

# Resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

#cropping
croped=img[220:300,40:400]
cv.imshow("cropped",croped)

cv.waitKey(0)

#try going through doc for other functions