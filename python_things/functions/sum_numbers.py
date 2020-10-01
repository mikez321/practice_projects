"""Pass in multiple args and sum them."""
from typing import Union


def sum_numbers(*args: Union[int, float]) -> Union[int, float]:
    """
    Sum all numbers passed in as args.

    :param args: The numbers to be summed.
    :return: The sum of all args.
    """
    sum = 0
    for num in args:
        sum += num

    return sum


print(sum_numbers(1, 2, 3, 4.5))
