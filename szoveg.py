def szovegListaba(sorIndex: int):
    szoveg = open("jatekSzoveg.txt", "r", encoding="utf-8")
    szLista = szoveg.readlines()
    print(szLista[sorIndex-1])
    szoveg.close()

