from nose.tools import *

class Book_Test:

    @istest
    def can_be_lent_by_default(self):
        book = Book()
        assert_true(book.islendable())


class BookOnceBorrowed_Test:

    def setUp(self):
        self.book = Book()
        self.book.borrow()

    @istest
    def is_not_lendable(self):
        assert_false(self.book.islendable())

    @istest
    def is_lendable_again_after_given_back(self):
        self.book.give_back()
        assert_true(self.book.islendable())


class Book:
    def __init__(self):
        self.lendable = True
    def islendable(self):
        return self.lendable
    def borrow(self):
        self.lendable = False
    def give_back(self):
        self.lendable = True
