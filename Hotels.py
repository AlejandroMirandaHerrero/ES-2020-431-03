class Hotels:

    def __init__(self, codi_hotel, nomh, ndesti, nh, dies,preupersona):
        self.codi = codi_hotel
        self.nom = nomh
        self.lloc=ndesti
        self.numerohostes = nh
        self.durada= dies
        self.preu_persona=preupersona
    
    def __eq__(self, other):
        return self.codi == other.codi and self.nom==other.nom and self.numerohostes==other.numerohostes  and self.lloc==other.lloc and self.durada==other.durada and self.preu_persona==other.preu_persona
