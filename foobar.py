"""Defines foobar and stores foo' and bar' serial ID numbers"""


class Foobar:
    def __init__(self):
        self.bar_identifier = None
        self.foo_identifier = None
        self.foobar = {}

    def create_foobar(self, foo, bar):
        self.foobar = {
            "foo_identifier": foo.identifier,
            "bar_identifier": bar.identifier,
        }
        return self.foobar
