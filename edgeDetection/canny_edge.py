import cv2

cv2.namedWindow("image")

img = cv2.imread('osaka_castle.jpg')
img = cv2.resize(img, (600,600)) 

low = 100
high = 300

while (1):    
    canny = cv2.Canny(img,low,high)
    
    cv2.imshow("image", canny)
    
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

# save image
cv2.imwrite("canny_osaka_castle"+".jpg", canny)

cv2.destroyAllWindows()

#%%
from matplotlib import pyplot as plt

img = plt.imread('osaka_castle.jpg', cv2.IMREAD_COLOR)
plt.subplot(121),plt.imshow(img)
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(canny,cmap = 'gray')
plt.title('Canny Edge'), plt.xticks([]), plt.yticks([])
