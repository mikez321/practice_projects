"""Decision class to help make choices."""


class Decision(object):
    """Decisions allow you to make choices."""

    def __init__(self):
        """Decisions have nothing to decide on at first."""
        self.choices = {}

    def add_choice(self, choice: str) -> None:
        """
        Add something to be decided upon.

        :param choice: A string of anything you want to be deciding on
        :return: This does not return anything but does update self.choices
        """
        self.choices[choice] = []

    def add_response(self, choice: str, res: str) -> None:
        """
        Add a response to a given choice.

        :param choice: A string of the choice to get a response.  This choice
            shold exist in self.choices.
        :param res: A string of positive feedback about that choice.  The
            response will be added to the list of responses for that choice
            and eventually will be added to determine which choice has the most
            positive responses.
        :return: None is returned from this function.  It only updaes
            self.choices.
        """
        self.choices[choice].append(res)
