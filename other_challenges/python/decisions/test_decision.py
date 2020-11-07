"""Testing for decision object."""
from decision import Decision


def test_it_exists():
    """Create a decision object."""
    decision = Decision()
    assert type(decision) == Decision


def test_it_has_nothing_to_decide_about_when_new():
    """New decisions have nothing to decide about when new."""
    decision = Decision()
    assert decision.choices == {}


def test_choices_can_be_added():
    """Choices can be added to decide upon."""
    decision = Decision()
    decision.add_choice("Truck")
    assert decision.choices == {"Truck": []}
    decision.add_choice("Van")
    assert decision.choices == {"Truck": [], "Van": []}


def test_responses_can_be_added_to_choices():
    """A choice can have responses added to it."""
    decision = Decision()
    decision.add_choice('Truck')
    decision.add_choice('Van')
    decision.add_response('Truck', 'It goes offroad real nice')
    decision.add_response('Van', 'You can sleep in it')

    expected = {
        'Truck': ['It goes offroad real nice'],
        'Van': ['You can sleep in it'],
    }

    assert decision.choices == expected
