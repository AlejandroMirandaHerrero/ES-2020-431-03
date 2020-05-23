from Cars import Cars
   

class cars_list:
    
    def __init__(self):
        self.cars=[]
        self.preutotal=0
        self.numcotxes=0
        
    def addcar(self,c: Cars):
        self.cars.append(c)
        self.numcotxes+=1
        self.preutotal+=(c.preu_dia*c.durada)
        
    def rmvcars(self,destino):
        aux=self.cars[:]
        for i in aux:
            if i.lloc==destino:
                self.numcotxes-=1
                self.preutotal-=(i.preu_dia*i.durada)
                self.cars.remove(i)

