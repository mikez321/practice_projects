"""Explore parameter types and where they can be placed."""


def func(p1, p2, *args, k, **kwargs):
    """Print out various parameters."""
    # p1 and p2 are two positional parameters
    # *args takes a variable number of args passed in as a tuple
    # k is a keyword arg and has to be passed in with a keyword
    # **kwargs is a var-keyword parameter
    print("positioinal or keyword.... {} {}".format(p1, p2))
    print("var-positional (*args):... {}".format(args))
    print("keyword:.................. {}".format(k))
    print("var-keyword:.............. {}".format(kwargs))


func(1, 2, 3, 4, 5, k=6, key1=7, key2=8)
