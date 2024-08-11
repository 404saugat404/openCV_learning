import cv2 as cv
import numpy as np

blank=np.zeros((1000,1000,3),dtype="uint8")
cv.imshow("blank",blank)

#paint the img with certain color
blank[100:300,500:800]=(0,255,0)
cv.imshow("colored",blank)

# or you can use builtin functions
blank1=np.zeros((1000,1000,3),dtype="uint8")
cv.rectangle(blank1,(100,100),(700,800),(0,255,0),thickness=5) #try writing cv.filled insted of integer in thicknss
cv.imshow("rectriangle", blank1)


#now lets draw a circle
cv.circle(blank1,(500,500),200,(0,0,255),thickness=cv.FILLED)
cv.imshow("circle",blank1)

#you can draw line using cv.line too, try it yourself

#you can also put text by using cv.puttext
cv.putText(blank1 , "hello everyone, im saugat", (0,300),20,cv.FONT_HERSHEY_COMPLEX,(0,0,255),2)
cv.imshow("text",blank1)
cv.waitKey(0)