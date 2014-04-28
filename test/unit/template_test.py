import pytest

# integration usage:
#
# templater = Templater()
# templater.define('foo', Template('foo {bar}'))
# templater.get('foo').render({'bar': 'baz'})


@pytest.fixture
def template():
    return Template('foo {bar}')


def test_replaces_placeholders_with_actual_values(template):
    assert template.render({'bar': 'baz'}) == 'foo baz'


def test_can_be_rendered_multiple_times(template):
    template.render({'bar': 'baz'})
    assert template.render({'bar': 'foo'}) == 'foo foo'


class Template:
    def __init__(self, contents):
        self.contents = contents

    def render(self, values):
        contents = self.contents
        for k, v in values.items():
            contents = contents.replace('{' + k + '}', v)
        return contents
