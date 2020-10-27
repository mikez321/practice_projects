"""Practice removing things from lists by iterating backwards."""


def beagle_party(dog_list):
    """Remove all dogs from the dog_list that aren't beagles."""
    for i in range(0, len(dog_list))[::-1]:
        if dog_list[i] != 'beagle':
            del dog_list[i]

    return dog_list
