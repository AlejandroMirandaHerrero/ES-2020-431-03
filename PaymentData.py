class PaymentData:

    def __init__(self, tipo, titular, numero_t, codigo_t): #El unico parametro que se le pasa es tipo(VIDA o MC)
        self.tipo=tipo
        self.titular=titular
        self.numero_t=numero_t
        self.codigo_t=codigo_t
        self.correcto=True
        
        if type(self.tipo)!=str or type(self.titular)!=str or type(self.numero_t)!=int or type(self.codigo_t)!=int:
            print("Error de format.")
            self.correcto=False
            
        if self.tipo=="" or self.titular=="" or self.numero_t== None or self.codigo_t==None:
            print("Falten dades.")
            self.correcto=False
        
        if len(str(numero_t))!=10 or len(str(codigo_t))!=4:
            print("Error de format al numero de tarjeta o codi de seguretat.")
            self.correcto= False
            
    def get_datapayment(self):
        if self.correcto==True:
            return self.tipo, self.titular, self.numero_t, self.codigo_t
        else:
            return False


