from nose.tools import *
import re

class StringCreator_Test:
    @istest
    def createsOnlyWhitespace(self):
        result = StringCreator().create()
        cleaned_up = re.sub(r'\s', '', result)
        ok_(not cleaned_up)

class StringCreator:
    def create(self):
        return u' \t \n '
