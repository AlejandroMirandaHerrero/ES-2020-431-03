# -*- coding: utf-8 -*-
"""
Created on Sun May 17 22:11:53 2020

@author: aleja
"""
from Skyscanner import Skyscanner
from User import User
from Flights import Flights
from PaymentData import PaymentData
from Bank import Bank
class Viaje:

    def __init__(self, usuario,viajerosi):
        self.viajeros = viajerosi
        self.destinos = []
        self.vuelos = Flights()
        
        self.precio= 0
        self.numviajeros= len(self.viajeros)
        self.usu=usuario
        
    def agregardestino(self,destino):
        self.destinos.append(destino)
        l=Skyscanner.getlistvuelo(destino)
        v=self.usu.seleccionarvuelo(l)
        self.precio=self.precio-self.vuelos.preutotal*self.numviajeros
        self.vuelos.agregarvol(v)
        self.precio+=(self.vuelos.preutotal*self.numviajeros)
    def eliminardestino(self,destino):
        self.destinos.remove(destino)
        self.precio=self.precio-self.vuelos.preutotal*self.numviajeros
        self.vuelos.elimnarvol(destino)
        self.precio+=(self.vuelos.preutotal*self.numviajeros)
    def pagarvuelo(self):
        metodopago=self.usu.seleccionarMetodo()
        p=PaymentData(metodopago, self.usu.nombre_completo, 15477952,1589)
        b=Bank()
        veri=False
        i=0
        while (i in range(0,5) and not veri):
            veri=b.do_payment(self.usu, p)
            if veri:
                print("Se ha podido realizar el pago")
                return True, metodopago
            i+=1
        print("No se ha podido realizar el pago")
        return False, metodopago
    def confirmareserva(self):
        b,metodo=self.pagarvuelo()
        if b:
            s=Skyscanner()
            veri=False
            i=0
            while (i in range(0,5) and not veri):
                veri=s.confirm_reserve(self.usu, self.vuelos)
                if veri:
                    print("Se ha podido realizar la confirmación")
                    return True
                i+=1
            print("No se ha podido realizar la confirmacion")
            return False
        return b
