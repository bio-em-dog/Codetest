from PIL import Image


image = Image.open('d-2.jpg').convert('L')
out = Image.new('L',(image.size[0],image.size[1]))


def WhiteWrite(img):
    WhiteXY = []
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            #print(img.getpixel((x, y)))
            if img.getpixel((x, y)) < 128:
                out.putpixel((x, y), 0)  # 置为黑点
                #print(img.getpixel((x, y)))
            else:
                out.putpixel((x, y), 255)  # 置为白点
                WhiteXY.append((x, y))
                #print(img.getpixel((x, y)))
    return WhiteXY


def DrawLine(img,start,end,rgb):
    if (end[0] - start[0]) == 0:
        for j in range(start[1], end[1]):
            img.putpixel((end[0], j), rgb)
    else:
        if abs(start[1]-end[1]) <= abs(start[0]-end[0]):
            for k in range(min(start[0],end[0]), max(start[0],end[0])):
                yy = (start[1]-end[1])/((start[0]-end[0])+0.1-0.1)*(k-end[0]) + end[1]
                img.putpixel((k, int(round(yy))), rgb)
        else:
            for l in range(min(start[1],end[1]), max(start[1],end[1])):
                xx = (start[0]-end[0])/((start[1]-end[1])+0.1-0.1)*(l-end[1]) + end[0]
                img.putpixel((int(round(xx)), l), rgb)


white = WhiteWrite(image)
min_x = image.size[0]*0.5
max_x = image.size[0]*0.5
min_y = image.size[1]*0.5
max_y = image.size[1]*0.5
for i in white:
    x=i[0]
    y=i[1]
    if x < min_x:
        min_x = x
        zuo = i
    if x > max_x:
        max_x = x
        you = i
    if y < min_y:
        min_y = y
        xia = i
    if y > max_y:
        max_y = y
        shang = i
print("shang%s\txia%s\tzuo%s\tyou%s" % (shang,xia,zuo,you))
out.putpixel(shang,128)
out.putpixel(xia,128)
out.putpixel(zuo,128)
out.putpixel(you,128)

DrawLine(out,zuo,you,128)
DrawLine(out,shang,xia,128)

out.save('test.tif')
