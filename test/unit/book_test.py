from pytest import fixture

def test_can_be_lent_by_default():
    book = Book()
    assert book.is_lendable()

@fixture
def borrowed():
    book = Book()
    book.borrow()
    return book

def test_is_not_lendable(borrowed):
    assert not borrowed.is_lendable()

def test_is_lendable_again_after_given_back(borrowed):
    borrowed.give_back()
    assert borrowed.is_lendable()


class Book:
    def __init__(self):
        self.lendable = True
    def is_lendable(self):
        return self.lendable
    def borrow(self):
        self.lendable = False
    def give_back(self):
        self.lendable = True
