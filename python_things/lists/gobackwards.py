"""Remove values backwards by index."""
data = [104, 101, 4, 105, 308, 103, 5, 107, 100, 306, 106, 102, 108]

min_valid = 100
max_valid = 200

print("This is the original dataset with values that need to be excluded.")
print(data)

# for index in range(len(data) - 1, -1, -1):
#     if data[index] > max_valid or data[index] < min_valid:
#         del data[index]

data_length = len(data) - 1
for index, value in enumerate(reversed(data)):
    if min_valid > data[data_length - index] < max_valid:
        del data[data_length - index]

print("-" * 30)
print("Here are all numbers between 100 and 200.")
print(data)
