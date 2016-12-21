from PIL import Image
import wordSelector
#(255, 255, 255, 255) is white
#(0, 0, 0, 255) is black

def findStart(im, pix, color, startX=0, startY=0):
    done = False
    for k in range(startX, min(im.size[0], im.size[1])):
        if done:
            break
        x = startX
        y = k + startY
        while y >= 0:
            if pix[x, y][0] <= 128 and color == "black":
                done = True
                break
            elif pix[x, y][0] > 128 and color == "white":
                done = True
                break
            else:
                if color == "black":
                    pix[x, y] = (0, 128, 256, 256)
                elif color == "white":
                    pix[x, y] = (256, 128, 0, 256)
                x += 1
                y -= 1
    return x, y

def findBoxSize(im, startX, startY, pix):
    box = 0
    done = False
    for x in range(startX, im.size[0]):
        if done == True:
            break
        for y in range(startY, (startY-startX)+x+1):
            if pix[x, y][0] >= 128:
                print("Corner: ",pix[x, y])
                print("Coordinates: ", x, y)
                pix[x,y] = (256, 0, 0, 256)
                done = True
                box = (x-startX, y-startY)
                break
            pix[x, y] = (128, 128, 128, 256)
    return box

def colorBox(im,startX, startY, box, pix, color=(128, 56, 128, 256)):
    for x in range(startX, min(box[0]+startX, im.size[0])):
        for y in range(startY, min(box[1]+startY, im.size[1])):
            pix[x, y] = color

def drawGridLines(im, startX, startY, box, pix):
    counter = 1
    offset = 0
    for x in range(startX, im.size[0]):
        #print(x-startX+1, box[0], x-startX+1%box[0])
        if counter == 4:
            offset += 1
            counter = 1
        if (x-startX-offset) % box[0] == 0:
            counter += 1
            for y in range(startY, im.size[1]):
                pix[x, y] = (256, 56, 128, 256)
    counter = 1
    offset = 0
    for y in range(startY, im.size[1]):
        if counter == 4:
            offset += 1
            counter = 1
        if (y-startY-offset) % box[1] == 0:
            counter += 1
            for x in range(startX, im.size[0]):
                pix[x, y] = (256, 56, 128, 256)

def averageEachBox(im, startX, startY, box, pix):
    for i in range(startX, im.size[0], box[0]):
        for j in range(startY, im.size[1], box[1]):
            total = 0
            number = 0
            for x in range(i, min(i+box[0], im.size[0])):
                for y in range(j, min(j+box[1], im.size[1])):
                    total += pix[x, y][0]
                    number += 1
            if total/number > 120:
                colorBox(im, i, j, box, pix, (256, 256, 256, 256))
            else:
                colorBox(im, i, j, box, pix, (0, 0, 0, 256))

def getStartOfBlock(startX, startY, x, y, box):
    offsetX = int(x/2)
    offsetY = int(y/2)
    return startX+(x*box[0])+offsetX, startY+(y*box[1])+offsetY

def checkBlock(startX, startY, box, pix):
    total = 0
    number = 0
    for x in range(startX, min(box[0]+startX, im.size[0])):
        for y in range(startY, min(box[1]+startY, im.size[1])):
            total+=pix[x, y][0]
            number+=1
    if total/number > 150:
        return 0
    else:
        return 1

def rowsToStrings(rows):
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


im = Image.open('FINISH LINE.png')
pix = im.load()
print("SIZE: ", im.size)
startX, startY = findStart(im, pix, "black")
box = findBoxSize(im, startX, startY, pix)
colorBox(im, startX, startY, box, pix)
print("Box:", box)
#averageEachBox(im, startX,startY, box, pix)
drawGridLines(im, startX, startY, box, pix)
rows = []
for j in range(0, int(im.size[1]/box[1]-1)):
    row = []
    for i in range(0, int(im.size[0]/box[0]-1)):
        curBoxX, curBoxY = getStartOfBlock(startX, startY, i, j, box)
        black = checkBlock(curBoxX, curBoxY, box, pix)
        if black:
            colorBox(im, curBoxX, curBoxY, box, pix, (0, 256, 56, 256))
        row.append(black)
    rows.append(row)
for row in rows:
    print(row)
strings = rowsToStrings(rows)
for str in strings:
    print(str)
strToWords = wordSelector.intializeDicts()
for string in strings:
    for str in string:
        if str[0] == '1':
                str = str[1:]
        if len(str) > 4:
            if str[::2] in strToWords and str[1::2] in strToWords:
                print(str, strToWords[str[::2]], strToWords[str[1::2]])
                break
        if str in strToWords:
            print(str, strToWords[str])


im.save('TestLines.png')

