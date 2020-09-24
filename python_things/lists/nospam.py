"""Remove spam from meals challenge."""
# Print out the menu but with all spam removed from the meals.
menu = [
    ['egg', 'bacon'],
    ['egg', 'sausage', 'bacon'],
    ['egg', 'spam'],
    ['egg', 'bacon', 'spam'],
    ['spam', 'bacon', 'sausage', 'spam'],
    ['spam', 'sausage', 'spam', 'bacon', 'spam', 'tomato', 'spam'],
    ['spam', 'egg', 'spam', 'spam', 'bacon', 'spam'],
]

# delete spam from meals with reversed and enumerate
# for meal in menu:
#     meal_index = len(meal) - 1
#     for index, item in enumerate(reversed(meal)):
#         if item == 'spam':
#             del meal[meal_index - index]
#     print(meal)

# create new meals omitting spam
# spamless_menu = []
# for meal in menu:
#     spamless_meal = []
#     for item in meal:
#         if item != 'spam':
#             spamless_meal.append(item)
#     spamless_menu.append(spamless_meal)
#
# print(spamless_menu)

# lets make this look nicer with a join
for meal in menu:
    meal_index = len(meal) - 1
    for index, item in enumerate(reversed(meal)):
        if item == 'spam':
            del meal[meal_index - index]
    print(", ".join(meal))
