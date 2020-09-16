"""Just wanted to play around and not follow a video."""


def counter(name):
    """Count letters in a name."""
    count_name = list(name)
    counter = 0
    for letter in count_name:
        counter += 1

    print(f"There are {counter} letter in the name {name}.")
    print(f"\tAnd btw... {name} backwards is {name[::-1].lower()}.")


name = input("Enter a name and I'll count the letters for you: ")
counter(name)
