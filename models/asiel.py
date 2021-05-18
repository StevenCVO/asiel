from models.dier import Dier

class Asiel:

    def __init__(self, naam, plaats, dieren=None, id=-1):
        # if dieren:
        #     self.dieren = dieren
        # else:
        #     self.dieren = []
        self.naam = naam
        self.plaats = plaats
        self.dieren = dieren if dieren else []
        self._id = id

    @property
    def id(self):
        return self._id   

    @property
    def dieren(self):
        return self._dieren

    @dieren.setter
    def dieren(self, dieren):
        # 2 voorwaarden:
        # 1. Is het een list?
        # 2. Zitten in de list alleen dieren?
        if not type(dieren) is list:
            raise ValueError
        # for dier in dieren:
        #     if isinstance(dier, Dier):
        #         continue
        #     else:
        #         raise ValueError
        if not all(isinstance(dier, Dier) for dier in dieren):
            raise ValueError
        self._dieren = dieren

    def dier_toevoegen(self, dier):
        if isinstance(dier, Dier):
            self._dieren.append(dier)
        else:
            raise ValueError

    def dier_verwijderen(self, dier):
        if dier in self.dieren:
            self._dieren.remove(dier)
        else:
            raise ValueError



asiel1 = Asiel("A1", "fskjdf")
asiel2 = Asiel("A2", "dsttyw")
asiel3 = Asiel("A2", "dsttyw", [1, 4, 6])

asiel1.dier_toevoegen(4)
asiel1.dieren.append(6)

print(asiel1.dieren)
print(asiel2.dieren)

