"""Intro to some basic sequence methods."""
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]
empty_list = []

numbers = even + odd

print(numbers)
sorted_numbers = sorted(numbers)
print(sorted_numbers)
print(numbers)
print(list('2198462'))
more_numbers = list(numbers)
print(more_numbers)
print(id(numbers))
print(id(more_numbers))
print(numbers is more_numbers)
even_more_numbers = numbers[:]
print(even_more_numbers)
print(even_more_numbers is numbers)
too_many_numbers = numbers.copy()
print(too_many_numbers)
print(too_many_numbers is numbers)

# print(min(even))
# print(max(even))
# print(min(odd))
# print(max(odd))
# print('*' * 20)
# print(len(even))
# print(len(odd))
# print('*' * 20)
# print('mississippi'.count("iss"))
# even.extend(odd)
# print(even)
# even.sort()
# print(even)
# even.sort(reverse=True)
# print(even)
