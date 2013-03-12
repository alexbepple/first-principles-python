from nose.tools import *

class Roman_Test:
    @istest
    def converts639(self):
        eq_(roman(639), "DCXXXIX")

def roman(arabic):
    pass
