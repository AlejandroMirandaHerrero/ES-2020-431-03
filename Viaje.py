
from Skyscanner import Skyscanner
from Alojamiento import Alojamiento
from Rentalcars import Rentalcars
from Hotel_list import Hotel_list
from User import User
from Flights import Flights
from Cars import Cars
from PaymentData import PaymentData
from cars_list import cars_list
from Bank import Bank

class Viaje:

    def __init__(self, usuario,viajerosi):
        self.viajeros = viajerosi
        self.destinos = []
        self.vuelos = Flights()
        self.precio = 0
        self.numviajeros = len(self.viajeros)
        self.usu = usuario
        self.hotel = Hotel_list()
        self.alojamientos = []
        self.cotxes = cars_list()
        
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
    
    def confirmareserva_coche(self):
        b,metodo=self.pagarcoche()
        if b:
            s=Rentalcars()
            if s.confirm_reserve(self.usu, self.coches):
                return True
            print("No se ha podido realizar la confirmacion")
            return False
        return b
    
    
    def confirmareserva_alojamiento(self):
        b,metodo=self.pagaralojamiento()
        if b:
            s=Alojamiento()
            if s.confirm_reserve(self.usu, self.hotel):
                return True
            print("No se ha podido realizar la confirmacion")
            return False
        return b

      
    def agregaralojamiento(self,alojamiento):
        self.alojamientos.append(alojamiento)
        l = Alojamiento.getlisthotel(alojamiento)
        h = self.usu.seleccionarhotel(l)
        self.precio=self.precio-self.hotel.preu_persona*self.numviajeros
        self.hotel.agregarhotel(h)
        self.precio+=(self.hotel.preu_persona*self.numviajeros)
        
        
        
    def eliminaralojamiento(self,alojamiento):
        self.alojamientos.remove(alojamiento)
        self.precio=self.precio-self.hotel.preu_persona*self.numviajeros
        self.hotel.eliminarhotel(alojamiento)
        self.precio+=(self.hotel.preu_opersona*self.numviajeros)
    
    def agregarcotxe(self, cotxe, destino):
        l= Rentalcars.getlistcotxe(destino)
        v=self.usu.seleccionarcotxe(l)
        self.cotxes.addcar(v)
        self.precio+=self.cotxes.preutotal
        
        
    def eliminarcotxe(self,codi_cotxe):
        self.cotxes.rmvcars(codi_cotxe)
        self.precio=(self.cotxes.preutotal)
              
