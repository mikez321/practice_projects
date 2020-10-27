"""Testing for beagle party."""
from beagle_party import beagle_party


def test_it_returns_a_list_of_only_beagles():
    """Given a list of dogs, it will only return beagles."""
    assert beagle_party([
            'doberman',
            'beagle',
            'schnauzer',
            'dachshund',
            'beagle',
            'lab',
            'beagle',
            'puggle',
            'poodle'
            ]) == ['beagle', 'beagle', 'beagle']
