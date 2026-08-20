# Count Numbers Divisible by 3
def count_divisible_by_3(n):
    count = 0
    for i in range(1, n + 1):
        if i % 3 == 0:
            count += 1
    return count

n = int(input("Enter a number: "))
print(f"The count of numbers divisible by 3 from 1 to {n} is: {count_divisible_by_3(n)}")