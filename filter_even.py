# Filters Even Numbers
def filter_even_numbers(numbers):
    numbers = [1, 2, 3, 10, 11, 20, 21, 30]
    even_numbers = []
    for n in numbers:
        if n % 2 == 0:
            even_numbers.append(n)
    return even_numbers
print(filter_even_numbers([1, 2, 3, 10, 11, 20, 21, 30]))
