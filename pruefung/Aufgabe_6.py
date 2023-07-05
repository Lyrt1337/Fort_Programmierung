liste = [1, "something", 7, "test"]
def list_Reverse(liste):
    if len(liste) == 0:
        return []
    else:
        return [liste.pop()] + list_Reverse(liste)
print(list_Reverse(liste))
