"""Intro to some basic sequence methods."""
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

# print(min(even))
# print(max(even))
# print(min(odd))
# print(max(odd))
# print('*' * 20)
# print(len(even))
# print(len(odd))
# print('*' * 20)
# print('mississippi'.count("iss"))
even.extend(odd)
print(even)
even.sort()
print(even)
even.sort(reverse=True)
print(even)
