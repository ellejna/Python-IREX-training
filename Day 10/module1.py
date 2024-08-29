import numpy as np
# 2D array creation
array_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print the array
print(array_2d)

# this is how you can get a specific element
print(array_2d[1, 2])

# show the dimensions
print(array_2d.ndim)

# shows how many rows and columns it has
print(array_2d.shape)

# shows number of elements in total
print(array_2d.size)

# gets a specific row and column
array_sub = array_2d[:2, :2]
print(array_sub)
print(array_2d[-2:, -2:])
print(np.sum(array_2d))

# find the mean
mean = np.mean(array_2d)
print(mean)

# sum of columns for each row
sum_columns = np.sum(array_2d, axis=0)
print(sum_columns)
