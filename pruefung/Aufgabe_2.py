global i
i = 0
def rek_cannam(a, b):
    global i
    i += 1
    if (a==0):
        return b+1
    elif (b==0):
        return rek_cannam(a-1, 1)
    else:
        return rek_cannam(a-1, rek_cannam(a, b-1))

def main():
    print("Resultat:", rek_cannam(2,2))
    print("Anzahl Rekursionsschritte", i)
main()