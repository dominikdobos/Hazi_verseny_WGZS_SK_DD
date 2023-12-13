import Jatekos
import szoveg
targyakLista = []
jatekos = Jatekos.Jatekos(5,0)
parancsokLista = ["megy","eszik","felvesz","hasznal"]

def jatekMenet():
    hanyadik = 1
    while hanyadik < 14:
        if helyszin(hanyadik):
            hanyadik += 1





def felhasznaloBekeres():
    return input("Parancssor: ")


def helyszin(hanyadik):
    tovabbhalad = False
    szoveg.szovegListaba(hanyadik)
    parancs = felhasznaloBekeres()
    parancssor = parancs.split(" ")
    helyszin = ["epulet"]
    while not tovabbhalad:
        if parancssor[0] == parancsokLista[0]:
            if len(parancssor) == 2:
                if parancssor[1] == helyszin[hanyadik-1]:
                    tovabbhalad = True
                    return tovabbhalad
        else:
            parancs = felhasznaloBekeres()

