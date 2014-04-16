import pytest
skip = pytest.mark.skipif


def test_leaves_short_words_unchanged():
    assert munge('abc') == 'abc'


def test_reverses_middle_in_longer_words():
    assert munge('abcd') == 'acbd'


def test_munges_sentence_word_by_word():
    assert munge('abc abc') == 'abc abc'


@skip
def test_ignores_punctuation():
    assert munge('abc abc!') == 'abc abc!'


def munge(text):
    if ' ' in text:
        return ' '.join(map(munge, text.split(' ')))
    if len(text) >= 4:
        return text[0] + text[-2:0:-1] + text[-1]
    return text
