class PaymentData:

    def __init__(self, tipo, titular, numero_t, codigo_t): #El unico parametro que se le pasa es tipo(VIDA o MC)
        self.tipo=tipo
        self.titular=titular
        self.numero_t=numero_t
        self.codigo_t=codigo_t
        
    def get_datapayment(self):
        return self.tipo, self.titular, self.numero_t, self.codigo_t


