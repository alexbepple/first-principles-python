from nose.tools import *
from hamcrest import *

# integration usage:
#
# templater = Templater()
# templater.define('foo', Template('foo {bar}'))
# templater.get('foo').render({'bar': 'baz'})

class Template_Test:

    @istest
    def replaces_placeholders_with_actual_values(self):
        template = Template('foo {bar}')
        assert_that(template.render({'bar': 'baz'}), is_(equal_to('foo baz')))

    @istest
    def can_be_used_multiple_times(self):
        template = Template('foo {bar}')
        template.render({'bar': 'baz'})
        assert_that(template.render({'bar': 'foo'}), is_(equal_to('foo foo')))


class Template:
    def __init__(self, contents):
        self.contents = contents

    def render(self, values):
        contents = self.contents
        for k, v in values.items():
            contents = contents.replace('{' + k + '}', v)
        return contents
