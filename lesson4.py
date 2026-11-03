import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

img = np.array(Image.open("photo.png").convert("RGB"))

print(img.shape)
print(img.dtype)
print(img[0, 0])

plt.imshow(img)
plt.show()

crop = img[400:2160, 1300:3100]
print(crop.shape)

plt.imshow(crop)
plt.show()

crop = img[400:2160, 1300:3100]
flipped = img[:, ::-1]
gray = img.mean(axis=2)

print("crop:", crop.shape)
print("flipped:", flipped.shape)
print("gray:", gray.shape)

plt.subplot(2, 2, 1); plt.imshow(img);     plt.title("Original")
plt.subplot(2, 2, 2); plt.imshow(crop);    plt.title("Crop")
plt.subplot(2, 2, 3); plt.imshow(flipped); plt.title("Flipped")
plt.subplot(2, 2, 4); plt.imshow(gray, cmap="gray", vmin=0, vmax=255); plt.title("Gray")
plt.tight_layout()
plt.show()