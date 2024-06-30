# Create 2 matrices consisting of 3X3 random numbers. Calculate the sum of these matrices.

import random

# create a 3x3 matrix
m1 = [[0 for x in range(3)] for j in range(3)]
m2 = [[0 for x in range(3)] for j in range(3)]
total = [[0 for x in range(3)] for j in range(3)]

# fill the matrix with random numbers
for i in range(3):
    for k in range(3):
        m1[i][k] = random.randint(0, 5)
        m2[i][k] = random.randint(0, 5)
        total[i][k] = m1[i][k] + m2[i][k]

print("matrix 1 = ", m1, "\n", "matrix2 = ", m2, "\n", "Total = ", total)

# matrix1 = [[4, 1, 3], [2, 0, 0], [4, 3, 5]]
# matrix2 = [[1, 0, 2], [4, 3, 0], [2, 4, 3]]
# Total =   [[5, 1, 5], [6, 3, 0], [6, 7, 8]]

mx = [[0 for x in range(10)] for j in range(4)]
print(mx)