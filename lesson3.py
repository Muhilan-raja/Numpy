import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# ---------- Load the photo as a NumPy array ----------
img = np.array(Image.open("photo.jpg").convert("RGB"))

print("type:", type(img))
print("shape:", img.shape)   # (height, width, 3)
print("dtype:", img.dtype)   # uint8 -> values 0 to 255
print("top-left pixel:", img[0, 0])   # [R G B]

h, w, _ = img.shape

# ---------- 1. Crop (center half) ----------
crop = img[h//4 : 3*h//4, w//4 : 3*w//4]

# ---------- 2. Flip horizontally ----------
flipped = img[:, ::-1]

# ---------- 3. Red channel only ----------
red_only = img.copy()
red_only[:, :, 1] = 0   # remove green
red_only[:, :, 2] = 0   # remove blue

# ---------- 4. Grayscale ----------
gray = img.mean(axis=2)  # average R, G, B for each pixel

# ---------- 5. Brighten (the safe way) ----------
bright = np.clip(img.astype(int) + 80, 0, 255).astype(np.uint8)

# ---------- Show everything ----------
images = [img, crop, flipped, red_only, gray, bright]
titles = ["Original", "Crop", "Flipped", "Red only", "Grayscale", "Brighter"]

plt.figure(figsize=(12, 7))
for i in range(6):
    plt.subplot(2, 3, i + 1)
    plt.imshow(images[i], cmap="gray" if i == 4 else None)
    plt.title(titles[i])
    plt.axis("off")
plt.tight_layout()
plt.savefig("day01_results.png")
plt.show()