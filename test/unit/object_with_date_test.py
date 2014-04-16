from datetime import date
import pytest


@pytest.fixture
def object_with_date():
    return ObjectWithDate()


def test_knows_when_it_was_created(object_with_date):
    assert object_with_date.creation == date.today()


def test_knows_when_it_was_created2(object_with_date):
    print object_with_date.creation


class ObjectWithDate:
    def __init__(self):
        self.creation = date.today()
