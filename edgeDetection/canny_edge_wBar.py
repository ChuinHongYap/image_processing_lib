import cv2
import numpy as np

def nothing(x):
    "print(x)"

cv2.namedWindow("image")
cv2.createTrackbar("low", "image", 0, 500, nothing)
cv2.createTrackbar("high", "image", 0, 500, nothing)

switch = 'OFF/Save'
cv2.createTrackbar(switch, "image", 0, 1, nothing)

img = cv2.imread('osaka_castle.jpg',0)
img = cv2.resize(img, (600,600))

while (1):
    # trackbar update position
    low = cv2.getTrackbarPos("low", "image")
    high = cv2.getTrackbarPos("high", "image")
    
    s = cv2.getTrackbarPos(switch, "image")
    
    edges = cv2.Canny(img,low,high)
    
    img_concate_Hori=np.concatenate((img,edges),axis=1)
    
    cv2.imshow("image", img_concate_Hori)
    
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

if s == 1:
    cv2.imwrite("canny_osaka_castle_2"+".jpg", edges)

cv2.destroyAllWindows()
