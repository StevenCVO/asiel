from db.datamanager_sqlite import DataManagerSQLite
from models.dier import Dier
from datetime import datetime
from db.datamanager_csv import DataManagerCSV

dm = DataManagerCSV("data/dieren.csv", "data/asielen.csv")

dm_sql = DataManagerSQLite()
# dieren = dm.get_dieren()
# for dier in dieren:
#     print(dier.naam)

# dier_met_id = dm.get_dier_by_id(1)
# print(dier_met_id.naam)

asielen = dm.get_asielen()
for asiel in asielen:
    print(f"In het asiel {asiel.naam} zitten:")
    for dier in asiel.dieren:
        print(dier.naam)

print("="*40)

asielen = dm_sql.get_asielen()
for asiel in asielen:
    print(f"In het asiel {asiel.naam} zitten:")
    for dier in asiel.dieren:
        print(dier.naam)