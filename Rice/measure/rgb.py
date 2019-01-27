from PIL import Image
#im = Image.open("testimage.jpg")
im = Image.open("testimage.png", 'r')
#png (R,G,B,A)
#JPEG (R,G,B)
out = Image.new("L", (im.size[0], im.size[1]))
pix = im.load()
width = im.size[0]
height = im.size[1]

for x in range(width):
    for y in range(height):
        r, g, b, a = pix[x, y]
        print(b)


out.save("sdf_r.tif")
