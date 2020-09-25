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
    """Loop through until galaxy is calm and return remaining rocks."""
    if all(calm(make_pairs(rocks))):
        print('All is calm in the galaxy.')
    else:
        print('Gonna be a rock beatdown')
    # result = battle(rocks)
    # asteroids(result)


def no_collision(rock_1, rock_2):
    """Determine if rocks are moving in same directions."""
    return rock_1 // abs(rock_1) == rock_2 // abs(rock_2)


def make_pairs(rocks):
    """Pair out the rocks into neighbors."""
    pairs = []
    while len(rocks) > 0:
        pairs.append(rocks[:2])
        del rocks[:2]
    return pairs


def calm(pairs):
    """Determine if any neighbors are going to battle."""
    calm_status = []
    for rock_1, rock_2 in pairs:
        calm_status.append(no_collision(rock_1, rock_2))
    return calm_status


asteroids([1, 8, 11, -5])
# def asteroids(rocks):
#     """Determine which rocks survive and which ones explode."""
#     battle_pairs = []
#     battle_results = []
#
#     while len(rocks) > 1:
#         battle_pairs.append(rocks[-2:])
#         del rocks[-2:]
#
#     for rock_1, rock_2 in battle_pairs:
#         print(no_collision(rock_1, rock_2))
#         battle_results.append(battle(rock_1, rock_2))
#
#     for result in battle_results:
#         for rock in result:
#             rocks.append(rock)
#
#
# def battle(rock_1, rock_2):
#     """Determine which rock survives the battle."""
#     if abs(rock_1) == abs(rock_2):
#         return []
#     elif abs(rock_1) > abs(rock_2):
#         return [rock_1]
#     elif abs(rock_1) > abs(rock_2):
#         return [rock_2]
#
#

#
#
# def beef(rocks, battle_pairs=[]):
#     """Determine if any rocks will battle."""
#     if len(rocks) % 2 == 0:
#         while len(rocks) > 0:
#             battle_pairs.append(rocks[-2:])
#             del rocks[-2:]
#         print(all(no_collision(battle_pairs)))
#     else:
#         odd_pair = rocks[0:2]
#         while len(rocks) > 1:
#             battle_pairs.append(rocks[-2:])
#             del rocks[-2:]
#         print(all(no_collision(battle_pairs)))
#         print(all(no_collision(odd_pair)))


# asteroids([5, 8, -5])
# if asteroids([10, -10]) == []:
#     print("Boom!")
# else:
#     print("Floatin' out in space homie....")
#
# if asteroids([5, 8, -5]) == [5, 8]:
#     print("Boom Boom!!")
# else:
#     print("Floatin', but you got lifeline bruh.")
