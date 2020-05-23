# -*- coding: utf-8 -*-
 
from Hotels import Hotels
class Hotel_list:

    def __init__(self):
        self.hotels=[]
        self.preutotal=0
        self.numhotels=0
        
    def addhotel(self,h: Hotels):
        self.hotels.append(h)
        self.numhotels+=1
        self.preutotal+=((h.preu_persona*h.numerohostes)*h.durada)
        
    def rmvhotel(self,codihotel):
        for i in self.hotels:
            if i.codi == codihotel:
                self.numhotels -= 1
                self.preutotal -= ((i.preu_persona*i.numerohostes)*i.durada)
                self.hotels.remove(i)
