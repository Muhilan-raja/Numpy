import numpy as np

# ---------- Creating a 2D array ----------
m = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120]
])

print("Array:")
print(m)
print("shape:", m.shape)   # (3, 4) -> 3 rows, 4 cols
print("ndim:", m.ndim)     # 2
print("size:", m.size)     # 12

# ---------- Single elements: m[row, col] ----------
print("\n--- Single elements ---")
print("m[0, 0] =", m[0, 0])     # 10
print("m[1, 2] =", m[1, 2])     # 70
print("m[2, 3] =", m[2, 3])     # 120
print("m[-1, -1] =", m[-1, -1]) # 120

# ---------- Rows and columns ----------
print("\n--- Rows and columns ---")
print("row 0:", m[0])          # [10 20 30 40]
print("row 0:", m[0, :])       # same
print("col 1:", m[:, 1])       # [ 20  60 100]
print("last col:", m[:, -1])   # [ 40  80 120]

# ---------- Slicing a block (crop) ----------
print("\n--- Block m[0:2, 1:3] ---")
print(m[0:2, 1:3])

# ---------- Step slicing ----------
print("\n--- Every 2nd column ---")
print(m[:, ::2])

print("\n--- Columns reversed (horizontal flip) ---")
print(m[:, ::-1])

print("\n--- Rows reversed (vertical flip) ---")
print(m[::-1, :])

# ---------- Math on every element ----------
print("\n--- Math ---")
print("m + 5:")
print(m + 5)
print("m * 2:")
print(m * 2)
print("max:", m.max())    # 120
print("min:", m.min())    # 10
print("mean:", m.mean())  # 65.0
print("sum:", m.sum())    # 780
