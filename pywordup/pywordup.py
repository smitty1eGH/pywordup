# -*- coding: utf-8 -*-

from random import shuffle

def puzzleSource(chunk):
    """Generator for words of a puzzle
    """
    for w in chunk.split(" "):
        yield w + " "

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

        def do_word(some_word):
            """Try to add SOMEO_WORD to the current line.

               If word no fit-fit, add current_line to puzzle_lines. 
            """
            line_len = len(self.current_line)
            if ((len(some_word) + line_len) > self.puzzle_width):
                self.puzzle_lines.append(self.current_line + pad_space(line_len))
                self.current_line = some_word
            else:
                self.current_line += some_word

        #Go through the input words and write them out to a list of lines.
        #  Afterward, handle the leftover words, and he attribution.
        [do_word(w) for w in self.puzzle_source]
        self.puzzle_lines.append(self.current_line + pad_space(len(self.current_line)))
        #self.puzzle_lines.append( self.puzzle_source.attrib + pad_space( len(self.current_line)))
        
        return self.puzzle_lines

class PuzzleFormat(object):
    """PuzzleFormat receives the list of strings and clue lines 
       That will become the puzzle when fed to the publisher
    """
    def __init__(self, puzzle_lines, puzzle_width):
        self.line_count   = len(puzzle_lines)
        self.puzzle_lines = puzzle_lines
        self.puzzle_width = puzzle_width
        self.vertical     = []            #will hold a vertical slice of puxzzle_lines
        self.puzzle_lines = puzzle_lines
        self.divider      = 'x' * puzzle_width
        self.clue_lines   = []            #list of lists of  munged values of self.vertical
        [self.clue_lines.append([]) for x in range(0, self.line_count)]
        
    def do_format(self):
        """
        """
        def vertical_slice(j):
            """Take the vertical slice of the input character strings
               at j. Omit spaces. Append to self.vertical
            """
            self.vertical = [""]
            [self.vertical.append((self.puzzle_lines[x][j:j+1]).lower())
                for x in range(0, self.line_count)]
            #return shuffle(self.vertical)
            return self.vertical.sort(reverse=True)
        for j in range(0, self.puzzle_width):
            vertical_slice(j)
            #print(self.vertical)
            for k in range(0,self.line_count):
                self.clue_lines[k].append(self.vertical[k])
            
def puzzlePublish(puzzle_format):
    """PuzzlePublish takes the PuzzleFormat instance and renders its 
       puzzle_lines and clue_lines as HTML
    """
    FULL_BLOCK = "&#9608;"
    HALF_BLOCK = "&#9600;"    
    #make a big list of all of the characters as lists of TD tags
    puzz = [["<td>%s</td>" % "&nbsp;"   if   c != ' ' \
                                        else          \
             "<td>%s</td>" % FULL_BLOCK for  c in x]  \
                                        for  x in puzzle_format.puzzle_lines] \
         + [["<td>%s</td>" % HALF_BLOCK for c in puzzle_format.divider]] \
         + [["<td>%s</td>" % c for c in x]
                               for x in puzzle_format.clue_lines]

    answ = [["<td>%s</td>" % c          if   c != ' ' \
                                        else          \
             "<td>%s</td>" % FULL_BLOCK for  c in x]  \
                                        for  x in puzzle_format.puzzle_lines] \
         + [["<td>%s</td>" % HALF_BLOCK for c in puzzle_format.divider]] \
         + [["<td>%s</td>" % c for c in x]
                               for x in puzzle_format.clue_lines]

    #make a TABLE
    return "<table border='1'>"    \
         + "".join(["<tr>%s</tr>"  % "".join(r) for r in puzz]) \
         + "</table><br/><br/>"    \
         + "<table border='1'>"    \
         + "".join(["<tr>%s</tr>"  % "".join(r) for r in answ]) \
         + "</table>"






