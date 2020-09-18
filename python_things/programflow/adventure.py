"""Practice with While Loops."""

available_exits = ['north', 'south', 'east', 'west']

chosen_exit = ''

while chosen_exit not in available_exits:
    chosen_exit = input('Choose a direction to exit: ')
    if chosen_exit.casefold() == 'quit':
        print('Game over')
        break
else:
    print('Yay, you escaped the room!')
