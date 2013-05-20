from nose.tools import *
from nose.plugins.skip import SkipTest

class Roman_Test:
    @istest
    def converts639(self):
        raise SkipTest
        eq_(roman(639), "DCXXXIX")

def roman(arabic):
    pass
