import numpy as np
import matplotlib.pyplot as plt
import PIL
from PIL import Image, ImageEnhance


img = Image.open('osaka_castle.jpg')

# grayscale
img_gray = img.convert('L')

# flip image
img_hflip = np.fliplr(img)
img_vflip = np.flipud(img)

# change contrast
img_en = ImageEnhance.Contrast(img)
img_contrastLess = img_en.enhance(0.5)
img_contrastMore = img_en.enhance(1.5)

# image rotation
img_rotate1 = img.rotate(-10, resample=0, expand=0, center=None, translate=None, fillcolor=None)
img_rotate2 = img.rotate(10, resample=0, expand=0, center=None, translate=None, fillcolor=None)

plt.figure(figsize=(8,4))

# plot images
plt.subplot(2,4,1),plt.imshow(img)
plt.title('Original'), plt.xticks([]), plt.yticks([])

plt.subplot(2,4,2),plt.imshow(img_gray, cmap="gray")
plt.title('Grayscale'), plt.xticks([]), plt.yticks([])

plt.subplot(2,4,3),plt.imshow(img_hflip)
plt.title('Flip Left-Right'), plt.xticks([]), plt.yticks([])

plt.subplot(2,4,4),plt.imshow(img_vflip)
plt.title('Flip Up-Down'), plt.xticks([]), plt.yticks([])

plt.subplot(2,4,5),plt.imshow(img_contrastLess)
plt.title('Contrast Down'), plt.xticks([]), plt.yticks([])

plt.subplot(2,4,6),plt.imshow(img_contrastMore)
plt.title('Contrast Up'), plt.xticks([]), plt.yticks([])

plt.subplot(2,4,7),plt.imshow(img_rotate1)
plt.title('Rotate CW'), plt.xticks([]), plt.yticks([])

plt.subplot(2,4,8),plt.imshow(img_rotate2)
plt.title('Rotate C-CW'), plt.xticks([]), plt.yticks([])
