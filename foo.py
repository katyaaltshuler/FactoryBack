"""Labeling Foo instances with serial ID number"""

import random


class Foo:
    def __init__(self):
        self.identifier = random.randint(1, 10000)
