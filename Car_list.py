# -*- coding: utf-8 -*-

  
from Cars import Cars 

class Car_list:

    def __init__(self):
        self.coches=[]
        self.preutotal=0
        self.numcoches=0
        
    def agregarcoche(self,c: Cars):
        self.coches.append(c)
        self.numcoches+=1
        self.preutotal+=c.preu_persona
        
    def elimnarcoche(self,coche):
        for i in self.coches:
            if i.codi == coche:
                self.numcoches -= 1
                self.preutotal -= i.preu
                self.coches.remove(i)

