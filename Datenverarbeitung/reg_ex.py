import re

names = [
    "Thomas Mächler",
    "Lisa Maria Kindle",
    "Karolina Thöny-Tyganova",
    "Josh",
    "Xuyen Thi Nguyen"
]

# re.split(r"")
# res = [re.fullmatch(r"((?P<first>.*?) +)?(?P<last>\S*)", str).groupdict() for str in names]
# print(res)
#
# res = [{"first": " ".join(re.split(r"\s+", name)[0:-1]), "last": re.split(r"\s+", name)[-1]} for name in names]
#
# print(res)

# res = [{"first": " ".join(re.split(r"\s+", name)[0]), "last": re.split(r"\s+", name)[-1]} for name in names]
# print(res)

# res = [{"something": (re.split(r"\s", name)[0:-1]), "last":re.split(r"\s+", name)[-1]} for name in names]
# print(res)

# print(names)

