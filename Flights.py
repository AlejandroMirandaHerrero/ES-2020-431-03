from Vol import Vol 
class Flights:

    def __init__(self):
        self.vols=[]
        self.preutotal=0
        self.numvols=0
        
    def agregarvol(self,v: Vol):
        self.vols.append(v)
        self.numvols+=1
        self.preutotal+=v.PreuperPas
        
    def elimnarvol(self,destino):
        aux=self.vols[:]
        for i in aux:
            if i.desti==destino:
                self.numvols-=1
                self.preutotal-=i.PreuperPas
                self.vols.remove(i)
