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
