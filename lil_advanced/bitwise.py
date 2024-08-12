import cv2 as cv
import numpy as np

blank=np.zeros((800,800),dtype="uint8")
# cv.imshow("bl",blank)

rect=cv.rectangle(blank.copy(),(30,30),(700,600),255,-1)
# cv.imshow("rectr",rect)

circ=cv.circle(blank.copy(),(400,400),290,244,-1)
# cv.imshow("cricle",circ)

#now lets try bitwise operater
bitwise_and=cv.bitwise_and(rect,circ)
cv.imshow("and",bitwise_and)

bitwise_or=cv.bitwise_or(rect,circ)
cv.imshow("or",bitwise_or)


# bitwise XOR --> non-intersecting regions
bitwise_xor = cv.bitwise_xor(rect,circ)
cv.imshow('Bitwise XOR', bitwise_xor)

# bitwise NOT
bitwise_not = cv.bitwise_not(circ)
cv.imshow('Circle NOT', bitwise_not)
cv.waitKey(0)


