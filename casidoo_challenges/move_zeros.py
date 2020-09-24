"""Move zeros to the end of the list."""
# Given an array of random integers, move all the zeros in the array to the end
# of the array. Try to keep this in O(n) time (or better)!
# Example:
# moveZeros([1, 2, 0, 1, 0, 0, 3, 6])
# [1, 2, 1, 3, 6, 0, 0, 0]


def move_zeros(numbers_list, zeros=[], indexes=[]):
    """Rearrange the list and move zeros to the end."""
    for index, num in enumerate(numbers_list):
        if num == 0:
            zeros.append(0)
            indexes.append(index)
    indexes.reverse()
    for index in indexes:
        del numbers_list[index]
    return numbers_list + zeros


given = [1, 2, 0, 1, 0, 0, 3, 6]

result = move_zeros(given)
expected = [1, 2, 1, 3, 6, 0, 0, 0]

if result == expected:
    print("You solved the challenge!")
else:
    print("Not there yet.")
