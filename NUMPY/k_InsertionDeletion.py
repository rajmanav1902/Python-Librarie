import numpy as np

a = np.array([[1, 2], [3, 4]])

# Insert 40 at index 2 along axis 1 (columns)
inserted_array = np.insert(a, 2, 40, axis=1)
print("Inserted array:")
print(inserted_array)

# Delete the element at index (1, 1)
deleted_array = np.delete(a, (1, 1))
print("Array after deletion:")
print(deleted_array)
