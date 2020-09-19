"""Unicorn object from Turings Mythical Creatures."""


class Unicorn:
    """This is a unicorn object and it has properties."""

    def __init__(self, name, color="White"):
        """Create unicorn with default color and name args."""
        self.name = name
        self.color = color

    def say(self, whatever):
        """Unicorns say sparkly things."""
        return "**;* {} *;**".format(whatever)


rob = Unicorn('Robert')
barb = Unicorn('Barbara', 'Purple')

print(rob.name == "Robert")
print(rob.color == "White")
print(barb.color == "Purple")
print(rob.say('Fabulous!') == "**;* Fabulous! *;**")
