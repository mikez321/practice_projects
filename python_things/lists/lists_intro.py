"""List lesson from Python Udemy course."""
computer_parts = ['computer',
                  'monitor',
                  'keyboard',
                  'mouse',
                  'mouse mat'
                  ]
#
# for part in computer_parts:
#     print(part)
#
# print(computer_parts[2])
# print(computer_parts[0:3])
# print(computer_parts[-1])
print(computer_parts)
# computer_parts[3] = 'trackball'
computer_parts[3:] = ['trackball', 'lamp', 'speakers', 'microphone']
print(computer_parts)
