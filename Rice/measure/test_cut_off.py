from PIL import Image

image = Image.open('asd.tif')\
    #.convert('L')
out = Image.new('L',(image.size[0],image.size[1]))


def WhiteWrite(img):
    WhiteXY = []
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            if img.getpixel((x, y)) < 50:
                out.putpixel((x, y), 0)  # 置为黑点
                #print(img.getpixel((x, y)))
            else:
                out.putpixel((x, y), 255)  # 置为白点
                #print(img.getpixel((x, y)))
    return WhiteXY

WhiteWrite(image)
out.save('test222.tif')