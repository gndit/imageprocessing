#import cv2
#img=cv2.imread("/root/photos/dog.jpg")
#cv2.imshow("original",img)
#cv2.waitKey(0)

#gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#cv2.imshow("Gray scale image",gray_img)
#cv2.waitKey(0)

#cv2.detroyAllWindos()

import cv2
img=cv2.imread("/root/photos/dog.jpg")
cv2.imshow("image",img)
cv2.waitKey(0)
imgg = cv2.transpose(img,None)
cv2.imshow("new pic",imgg)
cv2.waitKey()
nnew = cv2.cvtColor(img, 3, None,cv2.COLOR_BGR2GRAY)
cv2.waitKey()

cv2.detroyAllWindos()