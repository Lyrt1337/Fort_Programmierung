from PIL import Image


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
    img2.save("result.png", format="png")


path_1 = "sunset.jpg"
path_2 = "tiger.jpg"
mergeImages(path_1, path_2)

print("done")
