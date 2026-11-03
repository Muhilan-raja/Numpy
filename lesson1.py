import numpy as np

a = np.array([1, 2, 3, 4])
print(a)
print(type(a))
print(a.dtype)
print(a.shape)

nums_list = [1, 2, 3]
nums_arr = np.array([1, 2, 3])

print(nums_list * 2)
print(nums_arr * 2)

print(nums_list + nums_list)
print(nums_arr + nums_arr)

b = np.array([1, 2, 3.5])
print(b, b.dtype)