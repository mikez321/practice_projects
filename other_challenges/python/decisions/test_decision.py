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
