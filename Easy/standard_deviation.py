# Generate a sequence by generating random numbers and calculate its standard deviation
import random
import math

array_length = int(input("Enter the array length: "))

random_array = []
for i in range(array_length):
    random_array.append(random.randint(0, 100))

random_array.sort()
print("Array: ", random_array)

total_sum = 0
for num in random_array:
    total_sum += num

average = total_sum / array_length
print("Total: ", total_sum)
print("Average: ", average)


total_diff_squared = 0

for num in random_array:
    diff = num - average
    diff_squared = diff**2
    total_diff_squared += diff_squared

standard_deviation = math.sqrt(total_diff_squared / array_length)
print("Standard deviation: ", standard_deviation)
