import re

from hamcrest.core.base_matcher import BaseMatcher
from hamcrest import assert_that


def test_creates_only_whitespace():
    assert_that(StringCreator().create(), contains_only_whitespace())


class StringMatchesPattern(BaseMatcher):

    def __init__(self, pattern):
        self.pattern = pattern

    def describe_to(self, description):
        description.append_text("a string matching '") \
            .append_text(self.pattern) \
            .append_text("'")

    def _matches(self, item):
        return re.match(self.pattern, item)


def contains_only_whitespace():
    return StringMatchesPattern(r'^\s*$')


class StringCreator:
    def create(self):
        return u' \t \n '
