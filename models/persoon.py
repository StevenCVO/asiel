class Persoon:
    def __init__(self, naam, voornaam, email, id=-1):
        self.naam = naam
        self.voornaam = voornaam
        self.email = email
        self._id = id

    @property
    def volledige_naam(self):
        return f"{self.voornaam} {self.naam}"

    @property
    def id(self):
        return self._id