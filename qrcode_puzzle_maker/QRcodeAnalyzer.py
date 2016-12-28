from PIL import Image
import wordSelector
#(255, 255, 255, 255) is white
#(0, 0, 0, 255) is black



class qrcode_puzzle_maker:
    def __init__(self, im, trace=False):
        self.im = Image.open(im)
        self.pix = self.im.load()
        self.trace = trace
        self.startX, self.startY = self.findColor("black")
        if self.trace:
            print("SIZE: ", self.im.size)
            print("QRCode Start: ", self.startX, self.startY)
        self.getBoxOffset()
        self.findBoxSize()
        if self.trace:
            print("Box Size: ", self.box)
            self.colorBox(self.startX, self.startY)

    def getStrings(self, wordsFile):
        rows = []
        for j in range(0, int(self.im.size[1]/self.box[1]-1)):
            row = []
            for i in range(0, int(self.im.size[0]/self.box[0]-1)):
                curBoxX, curBoxY = self.getStartOfBlock(i, j)
                black = self.checkBlock(curBoxX, curBoxY)
                if black:
                    self.colorBox(curBoxX, curBoxY, (0, 256, 56, 256))
                row.append(black)
            rows.append(row)
        if self.trace:
            for row in rows:
                print(row)
        strings = self.rowsToStrings(rows)
        if self.trace:
            for str in strings:
                print(str)
        strToWords = wordSelector.intializeDicts(wordsFile)
        wordsDict = {}
        for i, string in enumerate(strings):
            for j, str in enumerate(string):
                oneActive = "one off"
                if str[0] == '1':
                        str = str[1:]
                        oneActive = "one on"
                wordsDict[(i, j)] = [oneActive]
                if str in strToWords:
                    wordsDict[(i,j)].append(strToWords[str])
                else:
                    wordsDict[(i,j)].append("NONE")
                if self.trace:
                    print(str, (i,j), wordsDict[(i,j)])
        return wordsDict

    def findColor(self, color, startX=0, startY=0):
        done = False
        for k in range(0, min(self.im.size[0], self.im.size[1])):
            if done:
                break
            x = startX
            y = k + startY
            while y >= startY:
                if self.pix[x, y][0] <= 128 and color == "black":
                    done = True
                    break
                elif self.pix[x, y][0] > 128 and color == "white":
                    done = True
                    break
                else:
                    if self.trace:
                        if color == "black":
                            self.pix[x, y] = (0, 256, 0, 256)
                        elif color == "white":
                            self.pix[x, y] = (256, 128, 0, 256)
                    x += 1
                    y -= 1
        return x, y

    def findBoxSize(self):
        endX, endY = self.findColor("white", self.startX, self.startY)
        if self.trace:
            print("From X ", self.startX, " to ", endX, " AND Y ", self.startY, " to ", endY)
        self.box = (endX - self.startX, endY - self.startY)
        extraX = self.cornerBox[0]%self.box[0]
        extraY = self.cornerBox[1]%self.box[1]
        self.paddingX = ((self.cornerBox[0]-extraX)/self.box[0])/extraX
        self.paddingY = ((self.cornerBox[1]-extraY)/self.box[1])/extraY
        if self.trace:
            print("Add an extra line every", self.paddingX, self.paddingY)

    def colorBox(self, startX, startY, color=(128, 56, 128, 256)):
        for x in range(startX, min(self.box[0]+startX, self.im.size[0])):
            for y in range(startY, min(self.box[1]+startY, self.im.size[1])):
                self.pix[x, y] = color

    def getBoxOffset(self):
        curX = self.startX
        curY = self.startY
        while self.pix[curX, curY][0] <= 128:
            curX+=1
        right = (curX, curY)
        curX = self.startX
        curY = self.startY
        while self.pix[curX, curY][0] <= 128:
            curY +=1
        down = (curX, curY)
        self.cornerBox = (right[0]-self.startX, down[1]-self.startY)
        if self.trace:
            self.pix[down[0], down[1]] = (256,0,0,256)
            self.pix[right[0], right[1]] = (256,0,0,256)
            print("Total Square Size: ", self.cornerBox)

    def getStartOfBlock(self, x, y):
        offsetX = int(x/self.paddingX)
        offsetY = int(y/self.paddingY)
        return self.startX+(x*self.box[0])+offsetX, self.startY+(y*self.box[1])+offsetY

    def drawGridLines(self):
        boxX = 1
        boxY = 1
        curBoxCoords = self.getStartOfBlock(boxX, boxY)
        while curBoxCoords[0] < self.im.size[0] and curBoxCoords[1] < self.im.size[1]:
            for i in range(self.startY, self.im.size[1]):
                self.pix[curBoxCoords[0], i] = (256, 56, 128, 256)
            boxX += 1
            curBoxCoords = self.getStartOfBlock(boxX, boxY)
        boxX = 1
        boxY = 1
        curBoxCoords = self.getStartOfBlock(boxX, boxY)
        while curBoxCoords[0] < self.im.size[0] and curBoxCoords[1] < self.im.size[1]:
            for i in range(self.startX, self.im.size[0]):
                self.pix[i, curBoxCoords[1]] = (256, 56, 128, 256)
            boxY += 1
            curBoxCoords = self.getStartOfBlock(boxX, boxY)

    def checkBlock(self, startX, startY, threshold=150):
        total = 0
        number = 0
        for x in range(startX, min(self.box[0]+startX, self.im.size[0])):
            for y in range(startY, min(self.box[1]+startY, self.im.size[1])):
                total+=self.pix[x, y][0]
                number+=1
        if total/number > threshold:
            return 0
        else:
            return 1

    def rowsToStrings(self, rows):
        strings = []
        for y in range(0, len(rows), 3):
            if y + 2 >= len(rows):
                break
            string = []
            for x in range(0, len(rows[0]), 3):
                if x + 2 >= len(rows[0]):
                    break
                str = ""
                if rows[y][x]:
                    str += '1'
                if rows[y][x+1]:
                     str += '2'
                if rows[y][x+2]:
                    str += '3'
                if rows[y+1][x]:
                    str += '4'
                if rows[y+1][x+1]:
                    str += '5'
                if rows[y+1][x+2]:
                    str += '6'
                if rows[y+2][x]:
                    str += '7'
                if rows[y+2][x+1]:
                    str += '8'
                if rows[y+2][x+2]:
                    str += '9'
                string.append(str)
            strings.append(string)
        return strings

    def save(self, newIm):
        self.im.save(newIm)


# def averageEachBox(im, startX, startY, box, pix):
#     for i in range(startX, im.size[0], box[0]):
#         for j in range(startY, im.size[1], box[1]):
#             total = 0
#             number = 0
#             for x in range(i, min(i+box[0], im.size[0])):
#                 for y in range(j, min(j+box[1], im.size[1])):
#                     total += pix[x, y][0]
#                     number += 1
#             if total/number > 120:
#                 colorBox(im, i, j, box, pix, (256, 256, 256, 256))
#             else:
#                 colorBox(im, i, j, box, pix, (0, 0, 0, 256))
