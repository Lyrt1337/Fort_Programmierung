# uebung1
"""
def leap_year(year):
    if year % 4 == 0 and (100 * round(year/100)) % 400 == 0:
        return True
    else:
        return False


print(leap_year(2000))
print(leap_year(2004))
print(leap_year(1900))
print(leap_year(2002))
"""

# uebung 2

"""
li = [34, 56, 28, 978, 0, 54, 86, 22, 76, 67, 453]
positions_liste = [2, 3, 8]

print([x for (i, x) in enumerate(li) if i not in positions_liste])
"""

# uebung 3
liste1 = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 128,
          136, 144, 152, 160, 168, 176, 184, 192, 200, 208, 216, 224, 232, 240, 248, 256]

new_list = []
for i in range(len(liste1)):
    if liste1[i] % 3 == 0:
        new_list.append(liste1[i] + 5)
print(new_list)

# def add(n):
#     return n + 5
#
# print([map(x, liste1) for i, x in enumerate(liste1) if liste1[i] % 3 == 0])
