"""This uses lessons from where we have learned so far to write a program."""
options = ["Make a Sandwich", "Watch TV", "Learn Python", "Get Outside",
           "Take a Nap", "Exit"]


def response(choice):
    """Print response and returns new choice."""
    print("{} is a great choice!".format(choice))
    choice = input("And then what? ")
    return choice


def display_list(list):
    """Display a numbered list from a provided list of options."""
    print("What do you want to do?")

    for option in options:
        if option == 'Exit':
            option_number = '0'
        else:
            option_number = str((options.index(option) + 1))
        print(option_number + ":\t" + option)


display_list(options)

choice = input()

while choice != "0":
    valid_choices = range(0, len(options))
    if choice.isalpha() or (int(choice) - 1) not in valid_choices:
        choice = input("Hum, Not sure about that one. Try again. ")
    else:
        choice = response(options[int(choice) - 1])
print("Bye!")
