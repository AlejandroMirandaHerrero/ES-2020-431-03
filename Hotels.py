class Hotels:

    def __init__(self, codi_hotel, nomh, nh, numeroha, dies,preupersona):
        self.codi = codi_hotel
        self.nom = nomh
        self.numerohostes = nh
        self.numerohabitacions= numeroha
        self.durada= dies
        self.preu_persona=preupersona
    
    def __eq__(self, other):
        return self.codi == other.codi and self.nom==other.nom and self.numerohostes==other.numerohostes and  self.numerohabitacions==other.numerohabitacions and self.durada==other.durada and self.preu_persona==other.preu_persona
