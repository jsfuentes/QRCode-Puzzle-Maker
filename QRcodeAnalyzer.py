from PIL import Image
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

def checkBlock(x, y):
    for x in range(startX, min(box[0]+startX, im.size[0])):
        for y in range(startY, min(box[1]+startY, im.size[1])):
            

im = Image.open('FINISH LINE.png')
pix = im.load()
print("SIZE: ", im.size)
startX, startY = findStart(im, pix, "black")
box = findBoxSize(im, startX, startY, pix)
colorBox(im, startX, startY, box, pix)
print("Box:", box)
#averageEachBox(im, startX,startY, box, pix)
drawGridLines(im, startX, startY, box, pix)
for i in range(0, int(im.size[0]/box[0]-1)):
    for j in range(0, int(im.size[1]/box[1]-1)):
        curBoxX, curBoxY = getStartOfBlock(startX, startY, i, j, box)


im.save('TestLines.png')

row1 = ['123479', '12378', '1467', '234589', '134679', '12389', '123679']
row2 = ['13467', '1245', '13469', '2368', '368', '258', '123456', ]