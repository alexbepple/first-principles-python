from nose.tools import *

class LineCounter_Test:
    @istest
    def counts_lines(self):
        import urllib
        urllib.urlretrieve ("http://agileinaflash.blogspot.com/feeds/posts/default", "rss.xml")
        eq_(LineCounter("rss.xml").count(), 1)

class LineCounter():
    def __init__(self, file):
        self.file = file
    def count(self):
        with open(self.file) as f:
            return len(f.readlines())
