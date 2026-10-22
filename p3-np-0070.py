
# Array Indexing in NumPy
import numpy as np

# Axel Guzman NC 0070

n = np.array([10, 20, 30, 40, 50])

print(n)
print(n[0])
print(n[3])
print(n[-1])
print(n[-2])

print("----------------------------------------")

n = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print(n)
print(n[0, 0])
print(n[1, 2])
print(n[-1, -1])
print(n[-2, -2])

print("----------------------------------------")

n = np.array([
    [
        [10, 20, 30],
        [40, 50, 60]
    ],
    [
        [70, 80, 90],
        [100, 110, 120]
    ]
])

print(n)
print(n[0, 0, 0])
print(n[1, 1, 2])
print(n[-1, -1, -1])
print(n[-2, -2, -2])

print("Axel Guzman 0070")