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
        
    def rmvcars(self,codi_cotxe):
        for i in self.cars:
            if i.codi==codi_cotxe:
                self.numcotxes-=1
                self.preutotal-=(i.preu_dia*i.durada)
                self.cars.remove(i)

