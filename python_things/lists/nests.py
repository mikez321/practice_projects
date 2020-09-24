"""Nested Lists."""
empty_list = []
even = list(range(2, 9, 2))
odd = list(range(1, 10, 2))
numbers = [even, odd]
print(numbers)

for number_list in numbers:
    print(number_list)

    for value in number_list:
        print(value)
