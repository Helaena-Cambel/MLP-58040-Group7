import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('panda.jpg')

blur = cv.GaussianBlur(img,(7,55),10)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])

plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()

