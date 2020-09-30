"""Work with functions in Python."""


def multiply(x, y):
    """Multiply two numbers, x and y."""
    result = x * y
    return result


answer = multiply(10.5, 4)
print(answer)

forty_two = multiply(6, 7)
print(forty_two)

for val in range(1, 5):
    two_times = multiply(2, val)
    print(two_times)
