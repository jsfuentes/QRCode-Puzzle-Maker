Overview
This is a qrcode_puzzle_maker that takes a QRcode and turns it into a array 
representation of 1's and 0's. That array is converted into potential words
that can represent the QRcode in a puzzle and returns that python dictionary.

Usage
The dictionary has the following interface:
puzzleDict[x,y] i.e puzzleDict[1,2]
which returns the list of potential words for that xy coordinate.

To understand the puzzle, see the 
bottom of this article: 
https://qz.com/15321/inside-the-epic-all-night-goldman-sachs-scavenger-hunt/

Testing
There is limited correction in the program so the QRcode should be straight.
As in test.py, use drawGridLines and turn on trace to better understand the
code, visualize the changes, and ensure the program is properly reading the
QRcode.

See the included word document for a sample puzzle I created and test.py for
sample usage.
