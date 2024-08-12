import cv2 as cv
import numpy as np

img=cv.imread("/home/saugat/Desktop/openCV/Resources/Photos/cats 2.jpg")
cv.imshow("img",img)
blank=np.zeros(img.shape[:2],dtype="uint8")
cv.imshow("blank",blank)


#now lets perform masking
masked=cv.circle(blank.copy(),(img.shape[1]//2,img.shape[0]//2),100,255,-1)
cv.imshow("mask",masked)

masked_img=cv.bitwise_and(img,img,mask=masked)
cv.imshow("masked img",masked_img)
cv.waitKey(0)