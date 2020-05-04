## pip install Pillow

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import PIL

# use PIL.Image
ShowText = 'Python PIL'

font = ImageFont.truetype('arialbd.ttf', 15) #load the font
size = font.getsize(ShowText)  #calc the size of text in pixels
image = Image.new('1', size, 1)  #create a b/w image
draw = ImageDraw.Draw(image)
draw.text((0, 0), ShowText, font=font) #render the text to the bitmap
for rownum in range(size[1]): 
#scan the bitmap:
# print ' ' for black pixel and 
# print '#' for white one
    line = []
    for colnum in range(size[0]):
        if image.getpixel((colnum, rownum)): line.append(' '),
        else: line.append('#'),
    print (''.join(line))


