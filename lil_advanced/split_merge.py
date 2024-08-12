import cv2 as cv
import numpy as np

img=cv.imread("/home/saugat/Desktop/openCV/Resources/Photos/park.jpg")
cv.imshow("image",img)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow("blank",blank)

#lets try splitting color
b,g,r=cv.split(img)
# cv.imshow("blue",b)
# cv.imshow("gree image",g)
# cv.imshow("red",r)

#you can also merge the img
merge=cv.merge([b,g,r])
# cv.imshow("merged img",merge)

#you can also define the clearer color channels
blue=cv.merge([b,blank,blank])
green=cv.merge([blank,g,blank])
red=cv.merge([blank,blank,r])
cv.imshow("blue",blue)

cv.imshow("gree",green)

cv.imshow("r",red)
cv.waitKey(0)
