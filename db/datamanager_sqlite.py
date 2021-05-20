from db.database import dbconn
from models.dier import Dier
from models.asiel import Asiel

class DataManagerSQLite():

    def get_dieren(self):
        with dbconn() as cur:
            cur.execute("SELECT * FROM dieren")
            rijen = cur.fetchall()
            return [Dier.from_dict(rij) for rij in rijen]

    def get_dier_by_id(self, id):
        with dbconn() as cur:
            cur.execute("SELECT * FROM dieren WHERE id = ?", [id])
            rij = cur.fetchone()
            return Dier.from_dict(rij) if rij else None

    def get_asielen(self):
        with dbconn() as cur:
            cur.execute("SELECT * FROM asielen")
            asiel_rijen = cur.fetchall()

            asielen = []
            for asiel_rij in asiel_rijen: 
                cur.execute("SELECT * FROM dieren WHERE asiel_id = ?", [asiel_rij["id"]])
                dieren_rijen = cur.fetchall()
                dieren = [Dier.from_dict(dieren_rij) for dieren_rij in dieren_rijen]
                asielen.append(Asiel(asiel_rij["naam"], asiel_rij["plaats"], dieren))
        
            return asielen

    

    
