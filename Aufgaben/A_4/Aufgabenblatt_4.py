"""
-------------------------
Aufgabenblatt_4.py Fort.Prog
Autor: Christian Gilomen
Datum: 20.04.2023
-------------------------
"""
# imports
from PIL import Image
import random as rnd


print("----------------------")
print("Aufgabe 16 - Dateien einlesen")
print("----------------------")
# Funktion returniert read_data nicht, da die Funktion selbst
# den Inhalt auf die Konsole ausgeben soll gem. Aufgabe.

def readFile(path):
    with open(path) as f:
        read_data = f.read()
        print(read_data)


readFile("Read_me.txt")

print("----------------------")
print("Aufgabe 17 - Dateien verändern")
print("----------------------")


def modifyFile(path):
    res = ""
    with open(path, "r") as f:
        read_data = f.read()
        for i in read_data:
            res = res + chr(ord(i) + 1)
    with open(path, "w") as f:
        f.write(res)
    print(f"- Original text from {path} was successfully encoded -")


modifyFile("Read_me2.txt")

print("----------------------")
print("Aufgabe 18 - Dateien aneinanderhängen")
print("----------------------")


def connect(path1, path2):
    with open(path1, "r") as f:
        read_data = f.read()
    with open(path2, "r") as f2:
        read_data2 = f2.read()
    with open("concat.txt", "w") as ff:
        res = read_data + " " + read_data2
        ff.write(res)
    print("- New File generated -")
    print("- concat.txt -")


connect("some.txt", "another.txt")


print("----------------------")
print("Aufgabe 19 - Operationen auf Dateiinhalten")
print("----------------------")
"""
Aufgabe war etwas verwirrend... anhand des Bildes oberhalb, hätte ich erwartet, dass die Pixel
mittels clustering ersetzt werden sollen. Ich habe mich aber an die Aufgabestellung gehalten, auch wenn
das resultierende Bild nicht wirklich etwas aussagt.
"""


def countColors(path):
    img = Image.open(path)
    # listing pixels
    all_pixels = []
    w, h = img.size
    for k in range(w):
        for m in range(h):
            pixel = img.getpixel((k, m))
            all_pixels.append(pixel)
    num_of_pixels = len(all_pixels)
    max_colors = num_of_pixels
    # number of Pixels: 65536

    # list of all unique colors with ranking
    ranking = img.getcolors(max_colors)

    # save pixels in pixels.txt
    with open("pixels.txt", "w") as b:
        b.write(str(ranking))
    return ranking, img


# set path and call function countColors
imgPath = "test.jpg"
colors_ranked, img_data = countColors(imgPath)

# find top10
# all colors without ranking, sorted
all_colors = []
for i in colors_ranked:
    all_colors.append(i[0])
    all_colors.sort(reverse=True)

# top10 colors
top_ten_ranking = all_colors[0:10]
top_ten_colors = []
for i in colors_ranked:
    if i[0] in top_ten_ranking:
        top_ten_colors.append(i[1])

# replace all pixels not in top10
width, height = img_data.size
for x in range(width):
    for y in range(height):
        curr_pixel = img_data.getpixel((x, y))
        if curr_pixel not in top_ten_colors:
            img_data.putpixel((x, y), rnd.choice(top_ten_colors))

# save resulting image
img_data.save("img_out.png", format="png")
print("- New image was created -")
print("- img_out.png -")


print("----------------------")
print("Aufgabe 20 - Bilddateien verschmelzen")
print("----------------------")


def mergeImages(path1, path2):
    img1 = Image.open(path1)
    img2 = Image.open(path2)
    w, h = img1.size
    for y in range(int(h)):
        for x in range(int(w/2)):
            if y % 2 != 0:
                img2.putpixel((x * 2, y), img1.getpixel((x * 2, y)))
            else:
                img2.putpixel((x * 2 - 1, y), img1.getpixel((x * 2 - 1, y)))
    img2.save("merge.png", format="png")


path_1 = "sunset.jpg"
path_2 = "tiger.jpg"
mergeImages(path_1, path_2)

print("- New image was created -")
print("- merge.png -")
