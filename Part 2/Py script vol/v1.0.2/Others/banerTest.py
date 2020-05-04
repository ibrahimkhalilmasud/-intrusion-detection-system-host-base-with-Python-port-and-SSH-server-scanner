# Banner display text
# https://www.tecmint.com/protect-ssh-logins-with-ssh-motd-banner-messages/



## pip install Pillow

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import PIL

ShowText = 'Python PIL'


font = ImageFont.truetype('arialbd.ttf', 15) #load the font
size = font.getsize(ShowText)  #calc the size of text in pixels
image = Image.new('1', size, 1)  #create a b/w image
draw = ImageDraw.Draw(image)
draw.text((0, 0), ShowText, font=font) #render the text to the bitmap

def mapBitToChar(im, col, row):
    if im.getpixel((col, row)): return ' '
    else: return '#'

for r in range(size[1]):
    print (''.join([mapBitToChar(image, c, r) for c in range(size[0])]))

## pip install Pillow

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import PIL

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


text = ("Hi there")
from PIL import Image, ImageDraw, ImageFont
import numpy as np
myfont = ImageFont.truetype("verdanab.ttf", 12)
size = myfont.getsize(text)
img = Image.new("1",size,"black")
draw = ImageDraw.Draw(img)
draw.text((0, 0), text, "white", font=myfont)
pixels = np.array(img, dtype=np.uint8)
chars = np.array([' ','#'], dtype="U1")[pixels]
strings = chars.view('U' + str(chars.shape[1])).flatten()
print( "\n".join(strings))




