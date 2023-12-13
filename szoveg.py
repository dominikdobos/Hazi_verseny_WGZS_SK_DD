def szovegListaba(self, sorIndex: int):
    self.sorIndex = sorIndex
    szoveg = open("jatekSzoveg.txt", "r", encoding="utf-8")
    
    szoveg.close()