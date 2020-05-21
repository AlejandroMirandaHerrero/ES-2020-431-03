# -*- coding: utf-8 -*-

  
from Hotel import Hotel 
class Hotel_list:

    def __init__(self):
        self.hotels=[]
        self.preutotal=0
        self.numhotels=0
        
    def agregarhotel(self,h: Hotel):
        self.hotels.append(h)
        self.numhotels+=1
        self.preutotal+=h.preu_persona
        
    def elimnarhotel(self,hotel):
        for i in self.hotels:
            if i.nom == hotel:
                self.numhotels -= 1
                self.preutotal -= i.preu_persona
                self.hotels.remove(i)
