from nose.tools import *

class Templater_Test:
    @istest
    def replaces_placeholders_with_actual_values(self):
        templater = Templater()
        templater.define('foo', 'foo {bar}')
        rendered = templater.render('foo', {'bar': 'baz'})
        eq_('foo baz', rendered)


class Templater:
    def __init__(self):
        self.templates = {}

    def define(self, name, contents):
        self.templates[name] = contents
    
    def render(self, name, values):
        return self._supplant(self.templates[name], values)

    def _supplant(self, contents, values):
        for k, v in values.items():
            contents = contents.replace('{' + k + '}', v)
        return contents
