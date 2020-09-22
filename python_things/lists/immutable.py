"""A look into immutable objects."""

# result = True
# another_result = result
# print(id(result))
# print(id(another_result))
# The id() function returns returns the 'identity' of an object
# while your program is running each object will always have the same ID
# this is like that hex number you get with Ruby objects...

# result = False
# print(id(result))
# This result has a different ID than the result on lines 5 and 6.
# result has been assigned to a new object because bools are immutable in
# Python

result = 'Correct'
another_result = result

print(id(result))
print(id(another_result))

result += 'ish'
print(id(result))
print(result)
print(another_result)
# Again, this new result has a different ID than the first one.  Strings are
# also immutable objects so Python has created a new object called 'result' and
# this new object is the result of the code result += 'ish'
