# -*- coding: utf-8 -*-
 
from Hotels import Hotels
class Hotel_list:

    def __init__(self):
        self.habs=[]
        self.preutotal=0
        self.numhabs=0
        
    def addhotel(self,h: Hotels):
        self.habs.append(h)
        self.numhabs+=1
        self.preutotal+=((h.preu_persona*h.numerohostes)*h.durada)
        
    def rmvhotel(self,desti):
        aux=self.habs[:]
        for i in aux:
            if i.lloc == desti:
                self.numhabs -= 1
                self.preutotal -= ((i.preu_persona*i.numerohostes)*i.durada)
                self.habs.remove(i)
