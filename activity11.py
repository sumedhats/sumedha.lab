import numpy as np

# Create two 3x3 arrays with random integers between 1 and 10
a = np.random.randint(1, 11, size=(3, 3))
b = np.random.randint(1, 11, size=(3, 3))

print("Matrix A:\n", a)
print("\nMatrix B:\n", b)

# Matrix subtraction
subtraction = a - b
print("\nMatrix Subtraction (A - B):\n", subtraction)

# Element-wise division (A / B)
division = a / b
print("\nElement-wise Division (A / B):\n", division)

