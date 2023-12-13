import Jatekos
import szoveg
targyakLista = []
jatekos = Jatekos.Jatekos(5,0)
parancsokLista = ["megy","eszik","felvesz","hasznal", "stat"]
evettSzam = 0   # Számolja, hogy hány kör telt el evés óta
eletero = jatekos.eletero

def jatekMenet():
    hanyadik = 1
    while hanyadik < 14:
        if hanyadik < 4:
            jatekos.eletero -= 1
        if helyszin(hanyadik):
            hanyadik += 1


def felhasznaloBekeres():
    return input("Parancssor: ")

def hanyKorMiotaEvett(hanyadikKor: int, nemEvett=evettSzam, eletero=eletero):
    if jatekos.eletero == eletero:
        nemEvett += 1
    else:
        nemEvett = 0


def helyszin(hanyadik):
    tovabbhalad = False
    szoveg.szovegListaba(hanyadik)
    parancs = felhasznaloBekeres()
    parancssor = parancs.split(" ")
    helyszin = ["epulet", "kut", "kastely"]
    while not tovabbhalad:
        if parancssor[0] == parancsokLista[0]:
            if len(parancssor) == 2:
                if hanyadik == 1 and parancssor[1] == helyszin[hanyadik-1]:
                    tovabbhalad = True
                    return tovabbhalad
                # if hanyadik == 2 and parancssor[1] == helyszin[]
        if len(parancssor) == 1:
            if parancssor[0] == parancsokLista[-1]:
                print(jatekos)
        else:
            parancs = felhasznaloBekeres()

