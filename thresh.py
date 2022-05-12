import cv2

import matplotlib.pyplot as plt

foto=cv2.imread("D:/pyhton_opencv/1.jpg",0)

foto=cv2.resize(foto,(250,250))

#3 0 değiştiriniz thresh değeri için

thresh=cv2.adaptiveThreshold(foto,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,3,0)

thresh=cv2.resize(thresh,(250,250))

thresh2=cv2.adaptiveThreshold(foto,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,3,0)

thresh2=cv2.resize(thresh2,(250,250))

cv2.imshow("Orjinal Foto",foto)

cv2.imshow("Adaptive Thresh MEAN",thresh)

cv2.imshow("Adaptive Thresh GAUSSIAN",thresh2)


cv2.waitKey()
cv2.destroyAllWindows()












