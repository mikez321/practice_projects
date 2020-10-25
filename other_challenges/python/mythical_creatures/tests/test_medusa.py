"""Tests for medusa.py."""
from medusa import Medusa

def test_it_exists():
    barb = Medusa('Barb')
    assert type(barb) == Medusa
