import cv2 as cv

def rescale_resol(frame, scale=0.75):
    height=int(frame.shape[0]*scale)

    width=int(frame.shape[1]*scale)

    dimension=(width,height)

    return cv.resize(frame,dimension , interpolation=cv.INTER_AREA)



img=cv.imread("/home/saugat/Desktop/openCV/Resources/Photos/cat_large.jpg")
cv.imshow("cat",img)


capture=cv.VideoCapture("/home/saugat/Desktop/openCV/Resources/Videos/dog.mp4")

while True:
    isTrue,frame=capture.read()
    resized_video=rescale_resol(frame)
    resized_img=rescale_resol(img)
    cv.imshow("video",frame)
    cv.imshow("resized",resized_video)
    cv.imshow("rescaled img", resized_img)

    if cv.waitKey(20) & 0xff==ord("d"):
        break

capture.release()
cv.destroyAllWindows()

#now lets rescale image



