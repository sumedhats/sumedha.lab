import numpy as np

# Create a 3x3 array with random integers between 1 and 20
arr = np.random.randint(1, 21, size=(3, 3))
print("Original Array:\n", arr)

# Calculate the mean
mean_value = np.mean(arr)
print("\nMean of the array:", mean_value)

# Replace elements less than 10 with 0
arr[arr < 10] = 0
print("\nModified Array (elements < 10 replaced with 0):\n", arr)

