import cv2 as cv
import matplotlib.pyplot as plt
img=cv.imread("/home/saugat/Desktop/openCV/Resources/Photos/park.jpg")
cv.imshow("img",img)

#by default, the opencv reads the img in bgr format
#lets try plotting the img in matplotlib
plt.imshow(img)
plt.show()


#lets reverse color channel and see the output
rgb=cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow("rgb img",rgb)

#lets try some other colorchannels
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# BGR to L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

#note: you cant convert the any color channel to any color channel, first you must convet it to bgr in cv

cv.waitKey(0)



