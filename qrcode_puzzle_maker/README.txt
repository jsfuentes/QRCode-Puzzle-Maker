OVERVIEW:
This is a qrcode_puzzle_maker that can be used to analyze a QRcode
and convert it into the necessary words to make a puzzle similar to the one
at the bottom of this link:
    http://qz.com/15321/inside-the-epic-all-night-goldman-sachs-scavenger-hunt/

BASICS:
See test.py for simple usage
Note the answers are returned in the form of a dictionary indexable with a x, y
coordinate tuple of the 3x3 grids with the upper left corner being (0,0)
i.e. answers[(1,1)]
The answers are returned with the first element noting whether one is active and
the second element being the entire list of possible words or None

LIMITATIONS:
The QRcode must be straight and there is limited correction for different
sizes. Use drawGridLines as in test.py to ensure the program is correctly
detecting edges. If you wanna gain more understanding of the code, turn
on trace as in test.py or in the constructor with trace=True as a parameter.

SAMPLE:
See my sample puzzle I created with this program in "QRpuzzle" for "FINISH LINE.png"
