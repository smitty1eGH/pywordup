#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_pywordup
----------------------------------

Tests for `pywordup` module.
"""

import unittest

from pywordup import pywordup

TEST_STRING = "The difference between theory and practice is greater in practice than in theory."

class TestPywordup(unittest.TestCase):

    def setUp(self):
        self.p = pywordup.PuzzleSource(TEST_STRING, "Herb Sutter")
        
    def test_next_word(self):
        [print(w) for w in self.p.next_word()]

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()

