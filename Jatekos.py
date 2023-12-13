class Jatekos:
    def __init__(self, eletero: int, ehseg: int):
        self.eletero = eletero
        self.ehseg = ehseg

    def __str__(self):
        return f"Életerő: {self.eletero}\nÉhség: {self.ehseg}"