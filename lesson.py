import matplotlib.pyplot as plt
import numpy as np

img = np.array([
    [[255, 0, 0],   [0, 255, 0]],     # row 0: red, green
    [[0, 0, 255],   [255, 255, 255]]  # row 1: blue, white
], dtype=np.uint8)
print(img.shape)


plt.imshow(img)
plt.show()


top_row = img[0:1, :]   # row 0 only, all columns
print(top_row.shape)    # (1, 2, 3)
plt.imshow(top_row)
plt.show()

flipped = img[:, ::-1]
plt.imshow(flipped)
plt.show()

gray = img.mean(axis=2)
print(gray)
print(gray.shape)
plt.imshow(gray, cmap="gray", vmin=0, vmax=255)
plt.show()