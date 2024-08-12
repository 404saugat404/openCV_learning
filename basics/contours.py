import cv2 as cv
import numpy as np

#countours are similar to edges but not edges exactly, do more research on what countours are

img=cv.imread("/home/saugat/Desktop/openCV/Resources/Photos/cats.jpg")
cv.imshow("cats", img)

blank_page=np.zeros(img.shape,dtype="uint8")
cv.imshow("blank",blank_page)


gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray cats" , gray)

blur=cv.GaussianBlur(gray,(5,5), cv.BORDER_DEFAULT)
cv.imshow("blured img", blur)

#now lets try finding countours
canny_img=cv.Canny(blur,125,175)
cv.imshow("canny", canny_img)

countours,hiearchies=cv.findContours(canny_img,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
print(f'no. of countours : {len(countours)}')

#we can also draw
cv.drawContours(blank_page, countours, -1, (0,0,255), 1)
cv.imshow('Contours Drawn', blank_page)

cv.waitKey(0)