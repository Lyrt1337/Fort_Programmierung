import numpy as np
from PIL import Image
import random as rnd

imgPath = "test.jpg"
img = Image.open(imgPath)

# Extracting pixel map:
# pixel_map = img.load()

# Bildgröße in Pixeln ermitteln, damit nachher die Ecken abgefragt werden können
width, height = img.size
width = int(width)-1
height = int(height)-1
# rgb_im = img.convert('RGB')

# Pixel-Liste
all_pixels = []
w, h = img.size
for x in range(w):
    for y in range(h):
        pixel = img.getpixel((x, y))
        all_pixels.append(pixel)

totalUniqueColors = len(all_pixels)
# number of Pixels: 65536
max_colors = totalUniqueColors

# Ausgabe der pixels in pixels.txt
with open("pixels.txt", "w") as b:
    b.write(str(img.getcolors(max_colors)))

all_colors = img.getcolors(max_colors)

# Alle Farben List1, sortiert
list1 = []
for i in all_colors:
    list1.append(i[0])
    list1.sort(reverse=True)

# Top10 colors
list2 = list1[0:10]
# print(list2)
colors = []
for i in all_colors:
    if i[0] in list2:
        colors.append(i[1])

# print("colors Top-Ten: ", colors)

# ========================================================================
# Test por Pixel-Update ab img, und speichern unter filename2.png
# Ist die pixel-Fabe in den Top-10, dann OK => sonst random aus den Top-10
# ========================================================================
w, h = img.size
for x in range(w):
    # fuer jedes n:
    for y in range(h):
        aktuPix = img.getpixel((x,y))
        if aktuPix not in colors:
            img.putpixel((x,y), rnd.choice(colors))

img.save("filename2.png", format="png")

