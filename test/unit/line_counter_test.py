def test_counts_lines():
    import urllib
    urllib.urlretrieve("http://agileinaflash.blogspot.com/feeds/posts/default",
                       "rss.xml")
    assert LineCounter("rss.xml").count() == 1


class LineCounter():
    def __init__(self, file):
        self.file = file

    def count(self):
        with open(self.file) as f:
            return len(f.readlines())
