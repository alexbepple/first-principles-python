def test_can_be_lent_and_returned():
    book = Book()
    assert book.islendable()
    book.borrow()
    assert not book.islendable()
    book.give_back()
    assert book.islendable()


class Book:
    def __init__(self):
        self.lendable = True

    def islendable(self):
        return self.lendable

    def borrow(self):
        self.lendable = False

    def give_back(self):
        self.lendable = True
