import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as img
import random as rnd

imgPath = "test.jpg"

rgb_data = img.imread(imgPath)
picture = Image.open(imgPath)
uniqueColors = []

w, h = picture.size
for x in range(w):
    for y in range(h):
        pixel = picture.getpixel((x, y))
        uniqueColors.append(pixel)

totalUniqueColors = len(uniqueColors)

# print("Unique colors: ", totalUniqueColors)

max_colors = totalUniqueColors
all_colors = picture.getcolors(max_colors)

# ranking of all colors
list1 = []
for i in all_colors:
    list1.append(i[0])
    list1.sort(reverse=True)

# find top10
list2 = list1[0:10]
# print(list2)
top_colors = []
for i in all_colors:
    if i[0] in list2:
        top_colors.append(i[1])

top_colors = np.array(top_colors)
print("colors: ", top_colors)
print("unique len:", range(len(uniqueColors)))
# switching pixels for top10
pixuls = []

new_pic = []
# print(range(len(rgb_data[:, :, 1])))
# for j in range(0, 3):
#     for i in range(len(rgb_data[0])):
#         if rgb_data[j, i] not in top_colors:
#             new_pic[j, i] = rnd.choice(top_colors)


plt.imshow(new_pic)
plt.show()
