"""Create kettle object."""


class Kettle(object):
    """This is a kettle and it can do kettle things."""

    power_source = 'electricity'

    def __init__(self, make, price):
        """
        Initialize a new kettle with a make and price and on status to False.

        :param make: The make of this kettle
        :param price: The price of the kettle
        """
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        """Turn 'on' to True."""
        self.on = True


kenwood = Kettle("Kenwood", 8.99)
print(kenwood.make)
print(kenwood.price)

kenwood.price = 12.75
# print(kenwood.make)
# print(kenwood.price)

hamilton = Kettle("Hamilton", 14.99)
print(hamilton.make)
print(hamilton.price)

# print(hamilton.on)
# hamilton.switch_on()
# print(hamilton.on)

# kenwood.on
#
# kenwood.power = 1.5
#
# print(kenwood.power)
# print(hamilton.power)

print(Kettle.power_source)
print(kenwood.power_source)
print(hamilton.power_source)
# Kettle.power_source = 'atomic'
hamilton.power_source = 'atomic'
print(Kettle.power_source)
print(kenwood.power_source)
print(hamilton.power_source)
