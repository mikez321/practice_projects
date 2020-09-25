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


def asteroids(rocks, safe=[]):
    """Produce outcome of all collissions."""
    pair = rocks[:2]
    if will_fight(pair):
        if fight_result(pair) is not None:
            safe.append(fight_result(pair))
        # print(safe)
    else:
        safe.append(pair[0])
        del rocks[0]

    print(safe)
    print(rocks)
    # return(safe)


def will_fight(pair):
    """Return true if pair have one num + and the other - ."""
    r1, r2 = pair
    return r1 // abs(r1) != r2 // abs(r2)


def fight_result(pair):
    """Return the larger of the absolute values or nothing if equal."""
    r1, r2 = pair
    if abs(r1) == abs(r2):
        'both explode'
    elif abs(r1) > abs(r2):
        return r1
    elif abs(r1) < abs(r2):
        return r2


asteroids([10, 10, -1])
