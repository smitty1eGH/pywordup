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
TEST_WIDTH  = 25

class TestPywordup(unittest.TestCase):

    def setUp(self):
        self.p = pywordup.PuzzleSource( TEST_STRING       ,"Herb Sutter" )
        self.l = pywordup.PuzzleLayout( self.p            , TEST_WIDTH )
        self.f = pywordup.PuzzleFormat( self.l.do_layout(), TEST_WIDTH )
        
    def test_next_word(self):
        [print(w) for w in self.p.next_word()]

    def test_do_layout(self):
        print(self.l.do_layout())

    def test_puzzle_format(self):
        self.f.do_format()
        print(self.f.puzzle_lines)
        print(self.f.clue_lines)
        
    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()

