from nose.tools import *

class Book_Test:
    @istest
    def can_be_lent_and_returned(self):
        book = Book()
        assert_true(book.islendable())
        book.borrow()
        assert_false(book.islendable())
        book.give_back()
        assert_true(book.islendable())

class Book:
    def __init__(self):
        self.lendable = True
    def islendable(self):
        return self.lendable
    def borrow(self):
        self.lendable = False
    def give_back(self):
        self.lendable = True
