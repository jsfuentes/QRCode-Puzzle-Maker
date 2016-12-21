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
            if pix[x, y][0] >= 250:
                print("Corner: ",pix[x, y])
                print("Coordinates: ", x, y)
                pix[x,y] = (256, 0, 0, 256)
                done = True
                box = (x-startX, y-startY)
                break
            pix[x, y] = (128, 128, 128, 256)
    return box

def colorBox(startX, startY, box, pix):
    for x in range(startX, box[0]+startX):
        for y in range(startY, box[1]+startY):
            pix[x, y] = (128, 56, 128, 256)

def drawGridLines(im, startX, startY, box, pix):
    for x in range(startX, im.size[0]):
        #print(x-startX+1, box[0], x-startX+1%box[0])
        if (x-startX) % box[0] == 0:
            for y in range(startY, im.size[1]):
                pix[x, y] = (256, 56, 128, 256)
    for y in range(startY, im.size[1]):
        if (y-startY) % box[1] == 0:
            for x in range(startX, im.size[0]):
                pix[x, y] = (256, 56, 128, 256)

def averageEachBox(im, startX, startY, box, pix):
    for i in range(0, im.size[0], box[0]):
        for j in range(0, im.size[0], box[1]):
            total = 0
            number = 0
            for x in range(i, i+box[0]):
                for y in range(j, j+box[1]):
                    total += pix[x, y][0]
                    number += 1

im = Image.open('FINISH LINE.png')
pix = im.load()
print("SIZE: ", im.size)
startX, startY = findStart(im, pix, "black")
box = findBoxSize(im, startX, startY, pix)
colorBox(startX, startY, box, pix)
print("Box:", box)
drawGridLines(im, startX, startY, box, pix)
im.save('Test.png')