from nose.tools import *
from datetime import date

class ObjectWithDate_Test:
    def setUp(self):
        self.object_with_date = ObjectWithDate()

    @istest
    def knows_when_it_was_created(self):
        eq_(self.object_with_date.creation, date.today())

    @istest
    def knows_when_it_was_created2(self):
        print self.object_with_date.creation

class ObjectWithDate:
    def __init__(self):
        self.creation = date.today()

