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
        self.puzzle_lines  = []
        self.current_line  = ""
        
    def do_layout(self):
        """Map the PuzzleSource into the upper half of the puzzle.
        """
        def do_word( some_word ):
            """Try to add SOMEO_WORD to the current line.

               If word no fit-fit, add current_line to puzzle_lines. 
            """
            if (len(some_word) + len(self.current_line) + 1 > self.puzzle_width):
                self.puzzle_lines.append( self.current_line )
                self.current_line  = " "
                self.current_line  = some_word + " "
            else:
                self.current_line += some_word + " "

                
        [do_word( w ) for w in self.puzzle_source.next_word()]
        self.puzzle_lines.append( self.current_line )
        return self.puzzle_lines
