"""Lesson about for loops."""

#
# parrot = "Norwegeian Blue"
#
# for character in parrot:
#     print(character.casefold())

number = "9,223;372:036 854,775;807"
separators = None
numbers = []

for char in number:
    if not char.isnumeric() and separators is None:
        separators = char
    elif not char.isnumeric():
        separators = separators + char
    else:
        numbers.append(char)

print(separators)
print("".join(numbers))
