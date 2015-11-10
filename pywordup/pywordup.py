# -*- coding: utf-8 -*-


from random import shuffle

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
        def pad_space(line_len):
            return " " * (self.puzzle_width - line_len)

        def do_word( some_word ):
            """Try to add SOMEO_WORD to the current line.

               If word no fit-fit, add current_line to puzzle_lines. 
            """
            if (len(some_word) + len(self.current_line) + 1 > self.puzzle_width):
                line_len = len(self.current_line)
                self.puzzle_lines.append( self.current_line + pad_space(line_len))
                self.current_line  = ""
                self.current_line  = some_word + " "
            else:
                self.current_line += some_word + " "

        #Go through the input words and write them out to a list of lines.
        #  Afterward, handle the leftover words, and he attribution.
        [do_word( w ) for w in self.puzzle_source.next_word()]
        self.puzzle_lines.append( self.current_line         + pad_space( len(self.current_line)))
        self.puzzle_lines.append( self.puzzle_source.attrib + pad_space( len(self.current_line)))
        
        return self.puzzle_lines

class PuzzleFormat(object):
    """PuzzleFormat receives the list of strings and clue lines 
       That will become the puzzle when fed to the publisher
    """
    def __init__(self, puzzle_lines, puzzle_width):
        self.line_count   = len(puzzle_lines)
        self.puzzle_lines = puzzle_lines
        self.puzzle_width = puzzle_width
        self.vertical     = []                      #will hold a vertical slice of puzzle_lines
        self.puzzle_lines = puzzle_lines
        self.clue_lines   = [ "" ] #holds munged values of self.vertical
        [self.clue_lines.append("") for x in range(0, self.line_count-1)]
        
    def do_format(self):
        """
        """
        def vertical_slice(j):
            """Take the vertical slice of the input character strings
               at j. Omit spaces. Append to self.vertical
            """
            x = 0
            self.vertical = [""]
            for x in range(0, self.line_count-1):
                y = self.puzzle_lines[x][j:j+1]
                if x != " ":
                    self.vertical.append( y )
                else:
                    print("%s\t%s" % (x,y))
            return shuffle( self.vertical )
        
        j = 0
        k = 0

        for j in range(0, self.puzzle_width -1):
            vertical_slice( j )
            #print(self.vertical)
            for k in range(0, len(self.vertical) -1):
                self.clue_lines[k] += self.vertical[k]


