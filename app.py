from models.dier import Dier
from datetime import datetime
from db.datamanager_csv import DataManagerCSV

dm = DataManagerCSV("data/dieren.csv", "data/asielen.csv")
dieren = dm.get_dieren()
for dier in dieren:
    print(dier.naam)

dier_met_id = dm.get_dier_by_id(1)
print(dier_met_id.naam)
