from PIL import Image
from PIL.ExifTags import TAGS
img = Image.open(r"test.jpg")
for tag,value in img._getexif().items():
	print (TAGS.get(tag, tag),value)

def convert():
        lat=lat_degree+lat_minutes/60+lat_second/60/60
        #wei
        lng=lat_degree+lat_minutes/60+lat_second/60/60
        #jing
