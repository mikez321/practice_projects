"""Remove items from lists."""
data = [4, 5, 104, 110, 120, 130, 130, 150, 160,
        170, 183, 4, 185, 187, 188, 191, 350, 360]

# delete outliers manually
# print(data)
# del data[0:2]
# print(data)
# del data[-2:]
# print(data)

min_valid = 100
max_valid = 200
result = []


print(data)
for num in data:
    if min_valid < num < max_valid:
        result.append(num)

print(result)
