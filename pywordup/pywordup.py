# -*- coding: utf-8 -*-

class PuzzleSource(object):
    """PuzzleSource receives a chunk of text and attribution for a puzzle
       
       This class is mostly a wrapper for the next_word generator.
    """
    def __init__(self, chunk, attrib):
        self.chunk  = chunk
        self.attrib = attrib

    def next_word(self):
        for w in self.chunk.split(" "):
            yield w

class PuzzleLayout(object):
    """Write the PuzzleSource out as a puzzle.
    
    """
    def __init__(self, puzzle_source, puzzle_width):
        self.puzzle_source = puzzle_source
        self.puzzle_width  = puzzle_width
