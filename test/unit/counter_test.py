from nose.tools import *

class Counter_Test:
    @istest
    def can_be_incremented(self):
        Counter.increment()
        eq_(Counter.value, 1)

    @istest
    def can_be_incremented_multiple_times(self):
        Counter.increment()
        eq_(Counter.value, 2)

class Counter:
    value = 0
    @staticmethod
    def increment():
        Counter.value += 1

