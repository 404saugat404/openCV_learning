import cv2 as cv
import numpy as np

img=cv.imread("/home/saugat/Desktop/openCV/Resources/Photos/park.jpg")
cv.imshow("park", img)

#translation
def translation(img, x , y):
    transMat=np.float32([[1,0,x],
                         [0,1,y]])
    dimension=(img.shape[0], img.shape[1])

    return cv.warpAffine(img,transMat,dimension)

transated_img=translation(img,100,100)
cv.imshow("translated img", transated_img)


def rotation(img, angle, rot_point=None):
    (hegiht,width)=img.shape[:2]

    if rot_point is None:
        rot_point=(width//2,hegiht//2)

    
    rot_mat=cv.getRotationMatrix2D(rot_point,angle,0.1)

    dimension=(width, hegiht)
    return cv.warpAffine(img, rot_mat, dimension)

rotated_img=rotation(img,4)
cv.imshow("rotated img", rotated_img)


#resizing
resized_img=cv.resize(img,(400,400),interpolation=cv.INTER_CUBIC)
cv.imshow("resized_img",resized_img)

#flipping
fliped_img=cv.flip(img,0)
cv.imshow("flipped image",fliped_img)

#cropping
cropped_img=img[100:400,400:500]
cv.imshow("cropped image",cropped_img)

cv.waitKey(0)