from PIL import Image
#(255, 255, 255, 255) is white
#(0, 0, 0, 255) is black

def findStart(im):
    startX = 0
    startY = 0
    done = False
    while done == False:
        if pix[startX, startY][0] <= 128:
            done = True
        else:
            pix[startX, startY] = (0, 128, 256, 256)
            if startX <= startY:
                startX += 1
            else:
                startY += 1
    return startX, startY

im = Image.open('smallCode.png')
pix = im.load()
print(im.size)
done = False
startX, startY = findStart(im)
box = 0

print(startX, startY, pix[startX, startY])

done = False
for x in range(startX, im.size[0]):
    if done == True:
        break
    for y in range(startY, x+1):
        if pix[x, y][0] >= 128:
            print(pix[x, y])
            print(x, y)
            done = True
            box = (x-startX, y-startY)
            break
        pix[x, y] = (128, 128, 128, 256)

print("FINAL:", box)



im.save('Test.png')