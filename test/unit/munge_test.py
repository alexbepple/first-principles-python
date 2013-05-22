from nose.tools import *
from hamcrest import *
from nose.plugins.skip import SkipTest


class TextMunger_Test:
    @istest
    def leaves_short_words_unchanged(self):
        assert_that(munge('abc'), equal_to('abc'))

    @istest
    def reverses_middle_in_longer_words(self):
        assert_that(munge('abcd'), equal_to('acbd'))

    @istest
    def munges_sentence_word_by_word(self):
        assert_that(munge('abc abc'), equal_to('abc abc'))

    @istest
    def ignores_punctuation(self):
        raise SkipTest
        assert_that(munge('abc abc!'), equal_to('abc abc!'))


def munge(text):
    if ' ' in text:
        return ' '.join(map(munge, text.split(' ')))
    if len(text) >= 4:
        return text[0] + text[-2:0:-1] + text[-1]
    return text
