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

TEST_STR2   = "hop head red"
TEST_WID2   = 4

TEST_VS0    = "And so was also James, and John, the sons of Zebedee, which were partners with Simon. And Jesus said unto Simon, Fear not; from henceforth thou shalt catch men. And when they had brought their ships to land, they forsook all, and followed him. LUKE 5:10-11"
TEST_WI0    = 60

TEST_VS1    = "And, behold, men brought in a bed a man which was taken with a palsy: and they sought means to bring him in, and to lay him before him. And when they could not find by what way they might bring him in because of the multitude, they went upon the housetop, and let him down through the tiling with his couch into the midst before Jesus. And when he saw their faith, he said unto him, Man, thy sins are forgiven thee. LUKE 5:18-20"

class TestPywordup(unittest.TestCase):

    def setUp(self):
        self.p = pywordup.puzzleSource( TEST_VS1 )
        self.l = pywordup.PuzzleLayout( self.p            , TEST_WI0 )
        self.f = pywordup.PuzzleFormat( self.l.do_layout(), TEST_WI0 )
        
    def test_next_word(self):
        [print(w) for w in self.p]

    def test_do_layout(self):
        print(self.l.do_layout())

    def test_puzzle_format(self):
        self.f.do_format()
        print(self.f.puzzle_lines)
        print(self.f.clue_lines)

    def test_puzzlePublish(self):
        self.f.do_format()
        print("<html><body>%s</body></html>" \
            % pywordup.puzzlePublish(self.f))
        
    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()

