# Filters Numbers Divisible by 3
def filter_divisible_by_3(numbers):
    numbers = [4, 6, 9, 11, 12, 15, 17, 20]
    divisible_by_3 = []
    for n in numbers:
        if n % 3 == 0:
            divisible_by_3.append(n)
    return divisible_by_3

print(filter_divisible_by_3([4, 6, 9, 11, 12, 15, 17, 20]))