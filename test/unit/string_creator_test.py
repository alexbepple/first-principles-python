import re

def test_creates_only_whitespace():
    result = StringCreator().create()
    cleaned_up = re.sub(r'\s', '', result)
    assert not cleaned_up

class StringCreator:
    def create(self):
        return u' \t \n '
