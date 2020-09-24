"""Explore Nested Lists and Style."""
menu = [
    ['egg', 'bacon'],
    ['egg', 'sausage', 'bacon'],
    ['egg', 'spam'],
    ['egg', 'bacon', 'spam'],
    ['spam', 'bacon', 'sausage', 'spam'],
    ['spam', 'sausage', 'spam', 'bacon', 'spam', 'tomato', 'spam'],
    ['spam', 'egg', 'spam', 'spam', 'bacon', 'spam'],
]
# The above line adheres to PEP8 styling.

for meal in menu:
    if 'spam' not in meal:
        print(meal)

        for item in meal:
            print(item)
    else:
        print(f"{meal} has a spam score of {meal.count('spam')}")
