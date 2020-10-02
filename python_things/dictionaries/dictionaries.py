"""Work with Dictionaries."""
fruit = {
    "orange": "a sweet, orange, citrus fruit",
    "apple": "good for making cider",
    "lemon": "a sour, yellow citrus fruit",
    "grape": "a small, sweet fruit growing in bunches",
    "lime": "a sour, green citrus fruit",
}

veg = {
    'cabbage': "every child's favorite",
    'carrots': 'bunnies love them',
    'sprouts': 'great on sammies'
}

# print(fruit)
# # print(fruit["lemon"])
# fruit['pear'] = 'an odd shaped apple'
# print(fruit)
# fruit['pear'] = 'great with tequila'
# print(fruit)
# del fruit['pear']
# print(fruit)
# # produces a key error
# print(fruit['tomato'])

# description = fruit.get('apple')
# print(description)
#
# description2 = fruit.get('cherry')
# print(description2)


# bike = {
#     "make": "Honda",
#     "model": "250 Dream",
#     "color": "Red",
#     "engine_size": 250,
# }
#
#
# print(bike['color'])
# bike.clear()
# print(bike)

# for item in fruit:
#     print(item)
#     print(fruit[item])
#
# print(fruit.values())
# print(list(fruit.keys()))
# print(fruit.items())

fruit.update(veg)
# for item in fruit:
#     print(item + "- " + fruit[item])
