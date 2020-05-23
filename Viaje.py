
from Skyscanner import Skyscanner
from Alojamiento import Alojamiento
from Rentalcars import Rentalcars
from Hotel_list import Hotel_list
from Booking import Booking
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
        if(self.hotel.habs):
            self.eliminaralojamiento(destino)
        if(self.cotxes.cars):
            self.eliminarcotxe(destino)
        
    def pagar(self):
        metodopago, ntarjeta, ncodigo =self.usu.rellenardatospago()
        p=PaymentData(metodopago, self.usu.nombre_completo, ntarjeta,ncodigo)
        aux=p.get_datapayment()
        print("Import a pagar sense IVA: ", self.precio, " Import amb IVA: ", self.precio*1.21 )
        if aux!=False: 
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
    
    
    def confirmareserva_total(self): #ns si es lo k quereis
        b, meodo =self.pagar()
        if b:
            s=Skyscanner()
            r=Rentalcars()
            b=Booking()
            veri = False
            s_bool = False
            if self.cotxes.cars:
                r_bool = False
            else:
                r_bool=True
            if self.hotel.habs:
                b_bool = False
            else:
                b_bool=True
            i = 0
            while i in range(0,5) and not veri:
                if not s_bool:
                    s_bool = s.confirm_reserve(self.usu, self.vuelos)
                    if s_bool:
                        print("Se ha podido realizar la confirmación de vuelos")
                if not r_bool:
                        r_bool = r.confirm_reserve(self.usu, self.cotxes)
                        if r_bool:
                            print("Se ha podido realizar la confirmación de coches")
                if not b_bool:
                    b_bool = b.confirm_reserve(self.usu, self.cotxes)
                    if b_bool:
                        print("Se ha podido realizar la confirmación de hoteles")
                veri = s_bool and r_bool and b_bool
                if veri:
                    print("Se ha podido realizar la confirmación")
                    return True
                i += 1
            print("No se ha podido realizar la confirmación")
            
            return False
        return b
  
    def agregaralojamiento(self,destino):
        l = Booking.getlisthotel(destino)
        h = self.usu.seleccionarhotels(l)
        self.precio-=self.hotel.preutotal
        for i in h:
            self.hotel.addhotel(i)
        self.precio+=self.hotel.preutotal
   
    def eliminaralojamiento(self,destino):
        self.precio-=(self.hotel.preutotal)
        self.hotel.rmvhotel(destino)
        self.precio+=(self.hotel.preutotal)
    
    def agregarcotxe(self, destino):
        l= Rentalcars.getlistcotxe(destino)
        v=self.usu.seleccionarcotxes(l)
        self.precio-=self.cotxes.preutotal
        for i in v:
            self.cotxes.addcar(i)
        self.precio+=self.cotxes.preutotal
        
        
    def eliminarcotxe(self,destino):
        self.precio-=(self.cotxes.preutotal)
        self.cotxes.rmvcars(destino)
        self.precio+=(self.cotxes.preutotal)
    

