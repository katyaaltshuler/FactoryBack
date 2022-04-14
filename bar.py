"""Labeling Bar instances with serial ID number"""

import random


class Bar:
    def __init__(self):
        self.identifier = random.randint(1, 10000)

