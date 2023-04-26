from PIL import Image
import random as rnd


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
imgPath = "world.jpg"
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
