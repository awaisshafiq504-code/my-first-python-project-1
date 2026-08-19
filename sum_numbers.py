# Sum of Numbers
def sum_numbers(n):
    total = 0
    for i in range(1, n + 1):
        total = total + i
    return total
n = int(input("Enter a number: "))
print(f"The sum of numbers from 1 to {n} is: {sum_numbers(n)}")
