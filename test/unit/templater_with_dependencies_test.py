from nose.tools import *
from mock import Mock
from mock import sentinel as s
from hamcrest import *

# integration usage:
#
# templater = Templater(Renderer())
# templater.define('foo', 'foo {bar}')
# templater.render('foo', {'bar': 'baz'})

class Templater_Test:
    @istest
    def uses_the_renderer_for_rendering(self):
        renderer_stub = Mock()
        renderer_stub.render.return_value = s.rendered

        templater = Templater(renderer_stub)
        templater.define('name', 'contents')

        assert_that(templater.render('name', 'actual_values'), equal_to(s.rendered))
        renderer_stub.render.assert_any_call('contents', 'actual_values')



class Templater:

    def __init__(self, renderer):
        self.templates = {}
        self.renderer = renderer

    def define(self, name, contents):
        self.templates[name] = contents

    def render(self, name, actual_values):
        return self.renderer.render(self.templates[name], actual_values)
