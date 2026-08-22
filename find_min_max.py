# Find the smallest measurement
# Find the largest measurement
numbers = [-20, -5, 0, 12, 7, -30, 15]
smallest = numbers[0]
largest = numbers[0]
for n in numbers:
    if n < smallest:
        smallest = n
    if n > largest:
        largest = n
print(f"The smallest measurement is: {smallest}")
print(f"The largest measurement is: {largest}")