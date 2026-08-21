# Find the largest measurement
numbers = [-5, -2, -10, -1, 3]
largest = numbers[0]
for n in numbers:
    if n > largest:
        largest = n
print(f"The largest measurement is: {largest}")