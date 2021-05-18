from datetime import datetime

class Dier:
    # De variabele SOORTEN doet dienst als CONSTANTE variabele die beschikbaar is
    # voor elke instantie van de klasse Dier. Zelfs zonder instantie kan ze opgevraagd
    # worden in het programma, via Dier.SOORTEN.
    # Men noemt dit soort variabelen STATIC VARIABLES.
    # In dit geval houdt de statische variabele SOORTEN een lijst bij van mogelijke diersoorten
    SOORTEN = [
        "hond",
        "kat",
        "hamster",
        "konijn"
    ]
    
    def __init__(self, naam, soort, geslacht, id=-1, opname_datum=None):
        # Het Id van het dier is standaard -1. Voor ons betekent dit dat het nog
        # geen Id heeft gekregen van de databank.
        # De opname_datum krijgt de standaardwaarde None om het optioneel te maken
        # De bedoeling is hier datetime.now() aan toe te wijzen indien weggelaten,
        # maar dit mag niet in de __init__() methode gebeuren, omdat elke instantie
        # dan exact hetzelfde moment als standaard zal krijgen, nl. het moment dat
        # het programma voor de eerste keer wordt uitgevoerd.

        self.naam = naam
        # Soort en geslacht zijn properties en worden via de setter gebruikt
        # De eigenlijke attributen zijn _soort en _geslacht, maar deze worden enkel in
        # de setter toegewezen
        self.soort = soort
        self.geslacht = geslacht
        # _id is een afgeschermd attribuut. Het duidt erop dat we niet toelaten dat
        # het id van buiten de klasse wordt gewijzigd. Dit is logisch, want id's worden
        # normaliter door de databank gegenereerd.
        self._id = id
        # De standaardwaarde voor de opname_datum is None, maar indien het None
        # is wijzen we het huidige moment toe aan het attribuut.
        self.opname_datum = opname_datum or datetime.now()

    # De property id heeft een GETTER die toegang geeft tot de waarde van het attribuut _id
    # Deze property krijgt geen bijhorende SETTER en is dus READ-ONLY:
    # ze kan niet van buiten de klasse gewijzigd worden
    @property
    def id(self):
        return self._id

    @property
    def soort(self):
        return self._soort

    @soort.setter
    def soort(self, soort):
        # De soort is alleen geldig als ze in de lijst van toegelaten SOORTEN zit
        if soort.lower() in self.SOORTEN:
            self._soort = soort.lower()
        else:
            raise ValueError

    @property
    def geslacht(self):
        return self._geslacht

    @geslacht.setter
    def geslacht(self, geslacht):
        # Enkel "m" en "v" zijn geldige waardes voor geslacht
        if geslacht.lower() in ["m", "v"]:
            self._geslacht = geslacht.lower()
        else:
            raise ValueError

diertje = Dier("Bennie", "Hond", "M")
# diertje.soort = "Vleermuis"
print(diertje.id)
print(diertje.soort)
diertje.geslacht = "F"

