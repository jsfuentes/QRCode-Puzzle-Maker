from qrcode_puzzle_maker import qrcode_puzzle_maker

test = qrcode_puzzle_maker("FINISH LINE.png")
test.drawGridLines()
test.trace = True
test.save("TestClass.png")
answer = test.getStrings("qrcode_puzzle_maker/words.txt")
