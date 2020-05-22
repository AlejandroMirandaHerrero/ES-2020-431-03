class Cars:

    def __init__(self, codi_cotxe, marcac,preuperdia, recollida, dies):
        self.codi = codi_cotxe
        self.marca = marcac
        self.lloc = recollida
        self.durada= dies
        self.preu_dia=preuperdia
        
    def __eq__(self, other):
        return self.codi == other.codi and self.marca==other.marca and self.lloc==other.lloc and  self.durada==other.durada and self.preu_dia==other.preu_dia
