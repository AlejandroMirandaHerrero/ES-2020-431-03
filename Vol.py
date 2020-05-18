# -*- coding: utf-8 -*-
"""
Created on Mon May 18 00:36:37 2020

@author: aleja
"""

class Vol:
    
    def __init__(self, codi_vol, destinacio, numero_passatgers, preupasatger):
        self.codivol = codi_vol
        self.desti = destinacio
        self.np = numero_passatgers
        self.PreuperPas=preupasatger
    
    def __eq__(self, other):
        return self.codivol == other.codivol and self.desti==other.desti and self.np==other.np and  self.PreuperPas==other.PreuperPas