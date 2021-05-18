import csv
from models.dier import Dier
from models.asiel import Asiel

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

    def dict_asiel_met_dieren(self, asiel):
        return {
            "id": asiel["id"],
            "naam": asiel["naam"],
            "plaats": asiel["plaats"],
            "dieren": [self.get_dier_by_id(int(id)) for id in asiel["dieren"].split(",")]
        }

    def get_asielen(self):
        with open(self.bestand_asielen, mode="r", encoding="utf-8") as bestand:
            reader = csv.DictReader(bestand, delimiter=";")
            asielen = [
                self.dict_asiel_met_dieren(asiel) for asiel in reader
            ]
            return [Asiel.from_dict(asiel) for asiel in asielen]

    def get_asiel_by_id(self, id):
        with open(self.bestand_asielen, mode="r", encoding="utf-8") as bestand:
            reader = csv.DictReader(bestand, delimiter=";")

            gevonden_asiel = [asiel for asiel in reader if int(asiel["id"]) == id]
            if gevonden_asiel:
                return Asiel.from_dict(self.dict_asiel_met_dieren(gevonden_asiel[0]))
            else:
                return None