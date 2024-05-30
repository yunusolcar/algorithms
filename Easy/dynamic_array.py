# Take multiple numbers from the user. Write these numbers into an array and sort it. Then, print the sum and calculate the average of the array.
count = int(input("kaç adet sayı girmek istiyorsunuz?: "))

list = []

for i in range(count):
    list.append(int(input("sayi giriniz: ")))

list.sort(reverse=True)
print(list)


"""
total
"""
total = 0
for j in list:
    total += j

print("end: ", total)


"""
sum
"""
arr_sum = total / len(list)
print("Sum: ", arr_sum)
