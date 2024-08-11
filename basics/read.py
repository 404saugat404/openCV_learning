import cv2 as cv
# #opening image
# img=cv.imread("/home/saugat/Desktop/openCV/Resources/Photos/cat_large.jpg")
# cv.imshow("cat",img)

# cv.waitKey(0)

#opening videos

capture=cv.VideoCapture("/home/saugat/Desktop/openCV/Resources/Videos/dog.mp4")

while True:
    isTrue,frame=capture.read()
    cv.imshow("video",frame)

    if cv.waitKey(20) & 0xff==ord("d"):
        break

capture.release()
cv.destroyAllWindows()
