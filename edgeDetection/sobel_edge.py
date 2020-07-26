import cv2
import numpy as np

'''
Laplacian and Sobel edge detection
'''

cv2.namedWindow("image", cv2.WINDOW_AUTOSIZE)
ddepth = cv2.CV_64F
kernel_size = 3

img = cv2.imread('osaka_castle.jpg', cv2.IMREAD_COLOR)
img = cv2.resize(img, (300,300)) 

# converting to gray scale
if len(img.shape) == 3:
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# remove noise
img = cv2.GaussianBlur(img,(3,3),0)

# convolute with proper kernels
laplacian = cv2.Laplacian(img,ddepth)
sobelx = cv2.Sobel(img,ddepth,1,0,ksize=kernel_size)  # x
sobely = cv2.Sobel(img,ddepth,0,1,ksize=kernel_size)  # y

while (1):
    
    img_concate_1=np.concatenate((img,laplacian),axis=1)
    img_concate_2=np.concatenate((sobelx,sobely),axis=1)
    img_concate=np.concatenate((img_concate_1,img_concate_2),axis=0)
    
    cv2.imshow("image", img_concate)
    
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cv2.imwrite("laplacian_osaka_castle"+".jpg", laplacian)
cv2.imwrite("sobelx_osaka_castle"+".jpg", sobelx)
cv2.imwrite("sobely_osaka_castle"+".jpg", sobely)

cv2.destroyAllWindows()

#%%
from matplotlib import pyplot as plt

img = plt.imread('osaka_castle.jpg', cv2.IMREAD_COLOR)
plt.subplot(221),plt.imshow(img)
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(222),plt.imshow(laplacian,cmap = 'gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(223),plt.imshow(sobelx,cmap = 'gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(224),plt.imshow(sobely,cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])

plt.show()