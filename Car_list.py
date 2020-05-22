from Cars import Cars
   

class cars_list:
    
    def __init__(self):
        self.cotxes=[]
        self.preutotal=0
        self.numcotxes=0
        
    def agregarcotxe(self,c: Cars):
        self.cotxes.append(c)
        self.numcotxes+=1
        self.preutotal+=(c.preu_dia*c.durada)
        
    def eliminarcotxe(self,codi_cotxe):
        for i in self.cotxes:
            if i.codi==codi_cotxe:
                self.numcotxes-=1
                self.preutotal-=(i.preu_dia*i.durada)
                self.cotxes.remove(i)
