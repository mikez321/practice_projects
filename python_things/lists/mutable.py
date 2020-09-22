"""Exploring mutable objects."""
shopping_list = ['milk',
                 'pasta',
                 'eggs',
                 'spam',
                 'bread',
                 'rice'
                 ]
another_list = shopping_list
print(id(shopping_list))
print(id(another_list))

shopping_list.append('cookies')
print(shopping_list)
print(id(shopping_list))
# And in this case, the new item gets added to our existing list and
# it didn't need to create a new object, just add to the existing one

# Another interesting point... because no new object was created and
# instead the same object was modified, shopping list and another_list
# are both bound to the same object.  In contrast, look at what happens
# when you do the same thing to an immutable string... another_result
# is not the same thing as result.
# This code was snagged from immutable.py

result = 'Correct'
another_result = result

print(id(result))
print(id(another_result))

result += 'ish'
print(id(result))
print(result)
print(another_result)
