import Jatekos
import szoveg
import jatekter

targyakLista = []
jatekos = Jatekos.Jatekos(5,0)
parancsokLista = ["megy","eszik","felvesz","hasznal", "stat"]
evettSzam = 0   # Számolja, hogy hány kör telt el evés óta
eletero = jatekos.eletero
hanyadik = 1


def jatekMenet():

    while jatekter.hanyadik < 14:
        if jatekter.hanyadik > 4:
            jatekos.eletero -= 1
        if helyszin(jatekter.hanyadik):
            jatekter.hanyadik += 1


def felhasznaloBekeres():
    return input("Parancssor: ")


def helyszin(hanyadik):
    tovabbhalad = False
    szoveg.szovegListaba(hanyadik)
    parancs = felhasznaloBekeres()
    parancssor = parancs.split(" ")
    helyszin = ["epulet", "kut", "kastely", "vartemplom", "kamra"]
    while not tovabbhalad:
        # megy-re :
        if parancssor[0] == parancsokLista[0]:
            if len(parancssor) == 2:

                if hanyadik == 1 and parancssor[1] == helyszin[hanyadik-1]:
                    tovabbhalad = True
                    return tovabbhalad

                if hanyadik == 2 and parancssor[1] == helyszin[1]:
                    tovabbhalad = True
                    return tovabbhalad

                if hanyadik == 2 and parancssor[1] == helyszin[2]:
                    jatekter.hanyadik = 4
                    tovabbhalad = True
                    return tovabbhalad

                if hanyadik == 3 and parancssor[1] == helyszin[2]:
                    jatekter.hanyadik = 4
                    tovabbhalad = True
                    return tovabbhalad

                if hanyadik == 4 and parancssor[1] == helyszin[2]:
                    tovabbhalad = True
                    return tovabbhalad

                if hanyadik == 5 and parancssor[1] == helyszin[3]:
                    tovabbhalad = True
                    return tovabbhalad

                if hanyadik == 5 and parancssor[1] == helyszin[4]:
                    jatekter.hanyadik = 8
                    tovabbhalad = True
                    return tovabbhalad

        # felvesz:
        if parancssor[0] == parancsokLista[2]:
            if len(parancssor) == 2:
                if parancssor[1] == "penz":
                    targyakLista.append("pénz")
                    tovabbhalad = True
                    return tovabbhalad

        # stat:
        elif len(parancssor) == 1 and parancssor[0] == parancsokLista[4]:
            if parancssor[0] == parancsokLista[-1]:
                print(f"Életerő: {jatekos.eletero}\nTárgyak: {targyakLista}")
                break
        else:
            parancs = felhasznaloBekeres()
            parancssor = parancs.split(" ")

