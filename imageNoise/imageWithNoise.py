import numpy as np
import matplotlib.pyplot as plt
import cv2

img = plt.imread(r"osaka_castle.jpg")
img = cv2.resize(img, (256,256), interpolation = cv2.INTER_AREA)    # resize to 256x256 pixels
img = img/255.  # rescale pixel values to 0 and 1

# Gaussian Noise
def addGaussianNoise(img, noise_factor = 0.5):
    factor = noise_factor * np.random.normal(0, 1, size=img.shape)
    img_noisy = img + factor
    img_noisy = np.clip(img_noisy, 0 , 1)
    return img_noisy

# Poisson Noise
def addPoissonNoise(img, noise_factor = 1):
    factor = noise_factor * np.random.poisson(img)
    img_noisy = img + factor
    img_noisy = np.clip(img_noisy, 0 , 1)
    return img_noisy

plt.figure(figsize=(12,8))

plt.subplot(2,2,1)
plt.imshow(img), plt.xticks([]), plt.yticks([]), plt.title("Original")
plt.subplot(2,2,2)
plt.imshow(addPoissonNoise(img)), plt.xticks([]), plt.yticks([]), plt.title("Poisson Noise")
plt.subplot(2,2,3)
plt.imshow(addGaussianNoise(img,0.2)), plt.xticks([]), plt.yticks([]), plt.title("Gaussian Noise (factor=0.2)")
plt.subplot(2,2,4)
plt.imshow(addGaussianNoise(img,0.5)), plt.xticks([]), plt.yticks([]), plt.title("Gaussian Noise (factor=0.5)")