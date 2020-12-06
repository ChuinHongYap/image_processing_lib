import numpy as np
import matplotlib.pyplot as plt
import PIL
from PIL import Image, ImageEnhance

SAVE_IMAGES = True

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

# plot images
plt.subplot(241),plt.imshow(img)
plt.title('Original', fontsize=10), plt.xticks([]), plt.yticks([])

plt.subplot(242),plt.imshow(img_gray, cmap="gray")
plt.title('Grayscale', fontsize=10), plt.xticks([]), plt.yticks([])

plt.subplot(243),plt.imshow(img_hflip)
plt.title('Flip Left-Right', fontsize=10), plt.xticks([]), plt.yticks([])

plt.subplot(244),plt.imshow(img_vflip)
plt.title('Flip Up-Down', fontsize=10), plt.xticks([]), plt.yticks([])

plt.subplot(245),plt.imshow(img_contrastLess)
plt.title('Contrast Down', fontsize=10), plt.xticks([]), plt.yticks([])

plt.subplot(246),plt.imshow(img_contrastMore)
plt.title('Contrast Up', fontsize=10), plt.xticks([]), plt.yticks([])

plt.subplot(247),plt.imshow(img_rotate1)
plt.title('Rotate CW', fontsize=10), plt.xticks([]), plt.yticks([])

plt.subplot(248),plt.imshow(img_rotate2)
plt.title('Rotate C-CW', fontsize=10), plt.xticks([]), plt.yticks([])

# save images for comparison
if SAVE_IMAGES:
    plt.savefig('imageAugmentation_comparison.png', dpi=300)

