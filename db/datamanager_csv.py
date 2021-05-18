import csv
from models.dier import Dier

class DataManagerCSV():

    def __init__(self, bestand_dieren, bestand_asielen):
        self.bestand_dieren = bestand_dieren
        self.bestand_asielen = bestand_asielen

    def get_dieren(self):
        with open(self.bestand_dieren, mode="r", encoding="utf-8") as bestand:
            reader = csv.DictReader(bestand, delimiter=";")
            return [Dier.from_dict(dier) for dier in reader]

    def get_dier_by_id(self, id):
        with open(self.bestand_dieren, mode="r", encoding="utf-8") as bestand:
            reader = csv.DictReader(bestand, delimiter=";")

            gevonden_dier = [dier for dier in reader if int(dier["id"]) == id]
            if gevonden_dier:
                return Dier.from_dict(gevonden_dier[0])
            else:
                return None
                      
    def get_asielen(self):
        pass