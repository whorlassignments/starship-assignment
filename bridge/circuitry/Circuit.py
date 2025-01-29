#! /usr/bin/env python

import os
import sys
import random

class Circuit:

    def __init__(self):
        with open(".signals", "r") as fh:
            signals = eval(fh.read())
        for signal in signals:
            self.evaluate(*signal)

    def evaluate(self, red, blue, green):
        # TODO: Fix the signal paths to allow the console
        #       to work again!

if __name__ == "__main__":
    circuit = Circuit()
