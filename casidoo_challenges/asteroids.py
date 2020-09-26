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
    if len(rocks) == 0:
        pass
    elif len(rocks) == 1:
        pair = safe[-1], rocks[0]
        if will_fight(pair):
            if fight_result(pair) is not None:
                safe.append(fight_result(pair))
            del rocks[0]
        else:
            safe.append(pair[1])
            del rocks[0]
        asteroids(rocks, safe)
    elif len(rocks) != 0:
        pair = rocks[:2]
        if will_fight(pair):
            if fight_result(pair) is not None:
                safe.append(fight_result(pair))
            del rocks[:2]
        else:
            safe.append(pair[0])
            del rocks[0]
        asteroids(rocks, safe)
    print(safe)
    return(safe)


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


# Two equal numbers in opposite directions returns nothing.
if asteroids([10, -10]) == []:
    print("Two numbers of equal values in opposite directions both explode.")
else:
    print("still need to fix the first part")


# Two numbers collide and the larger abs val wins.
if asteroids([5, 8, -5]) == [5, 8]:
    print("The larger abs value wins when two asteroids collide.")
else:
    print("still need to fix the second part")


# It can handle extra asteroids.
if asteroids([5, 8, -5, 2]) == [5, 8, 2]:
    print("More asteroids can join the party")
else:
    print("still need to fix the third part")
