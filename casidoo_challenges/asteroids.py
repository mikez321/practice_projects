"""Casidoo Challenge: Asteroids."""
# Given an array of integers representing asteroids in a row, for each
# asteroid, the absolute value represents its size, and the sign represents
# its direction (positive = right, negative = left). Return the state of the
# asteroids after all collisions (assuming they are moving at the same speed).
# If two asteroids meet, the smaller one will explode. When they are the same
# size, they both explode. Asteroids moving in the same direction will never
# meet.
#
# Example:
#
# $ asteroids([5, 8, -5])
# $ [5, 8] // The 8 and -5 collide, 8 wins. The 5 and 8 never collide.
#
# $ asteroids([10, -10])
# $ [] // The 10 and -10 collide and they both explode.


def asteroids(rocks):
    """Determine which rocks survive and which ones explode."""
    rock_1, rock_2 = rocks[-2:]
    del rocks[-2:]
    if collide(rock_1, rock_2):
        return battle(rock_1, rock_2)
    else:
        return [rock_1, rock_2]


def battle(rock_1, rock_2):
    """Determine which rock survives the battle."""
    if abs(rock_1) == abs(rock_2):
        return []
    elif abs(rock_1) > abs(rock_2):
        return [rock_1]
    elif abs(rock_1) > abs(rock_2):
        return [rock_2]


def collide(rock_1, rock_2):
    """Determine if rocks are moving in opposing directions."""
    return rock_1 // abs(rock_1) != rock_2 // abs(rock_2)


if asteroids([10, -10]) == []:
    print("Boom!")
else:
    print("Floatin' out in space homie....")
