# Count Even Numbers
def count_even(n):
    count = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            count += 1
    return count
n = int(input("Enter a number: "))
print(f"The count of even numbers from 1 to {n} is: {count_even(n)}")
