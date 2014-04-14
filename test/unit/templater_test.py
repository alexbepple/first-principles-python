def test_replaces_placeholders_with_actual_values():
    templater = Templater()
    templater.define('foo', 'foo {bar}')
    rendered = templater.render('foo', {'bar': 'baz'})
    assert 'foo baz' == rendered


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
