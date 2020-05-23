import pytest
from Viaje import Viaje
from User import User
from Vol import Vol
from Cars import Cars
from Hotels import Hotels
from unittest.mock import patch
from PaymentData import PaymentData
from Skyscanner import Skyscanner
from Rentalcars import Rentalcars
@pytest.mark.parametrize("viajero,expected", [
    (["Antonio"],1),
    (["Antonio","Eva"],2),
    ([],0),
    (["juan","antonio","jose","ilias"],4)])

def test_iniviaje(viajero, expected):
    u=User("Antonio", "47238223L", "08291", "711736632","antonio@gmail.com")
    a=Viaje(u,viajero)
    assert (a.numviajeros == expected and not a.destinos and a.vuelos.numvols==0 and a.precio==0)

@pytest.mark.parametrize("viajeros,destino,edestino,evuelo,epreu", [
    (["Antonio"],("Madrid",4),[("Madrid",4)],[Vol(157892,"Madrid",100,90)],90),
    (["Antonio", "Juan"],("Madrid",4),[("Madrid",4)],[Vol(157892,"Madrid",100,90)],180)
    ])
    
def test_agregardestino(viajeros,destino,edestino,evuelo,epreu):
    u=User("Antonio", "47238223L", "08291", "711736632","antonio@gmail.com")
    a=Viaje(u,viajeros)
    with patch('Skyscanner.Skyscanner.getlistvuelo') as mock_requests:
        mock_requests.return_value=  [Vol(157892, "Madrid",100,90)]
        with patch('User.User.seleccionarvuelo') as mock_requests1:
            mock_requests1.return_value=Vol(157892,"Madrid",100,90)
            a.agregardestino(destino)
    assert (edestino==a.destinos and a.vuelos.vols==evuelo and a.precio==epreu )


@pytest.mark.parametrize("viajeros,destino,edestino,evuelo,epreu", [
    (["Antonio","Oscar", "Juan"],"Nueva York",["Madrid", "Barcelona"],[Vol(157892,"Madrid",100,90),Vol(192548,"Barcelona",80,120)],630),
    ])
def test_eliminardestino(viajeros,destino,edestino,evuelo,epreu):
    u=User("Antonio", "47238223L", "08291", "711736632","antonio@gmail.com")
    a=Viaje(u,viajeros)
    with patch('Skyscanner.Skyscanner.getlistvuelo') as mock_requests:
        mock_requests.return_value=  [Vol(157892,"Madrid",100,90)]
        with patch('User.User.seleccionarvuelo') as mock_requests1:
            mock_requests1.return_value=Vol(157892,"Madrid",100,90)
            a.agregardestino("Madrid")   
    with patch('Skyscanner.Skyscanner.getlistvuelo') as mock_requests3:
        mock_requests3.return_value=  [Vol(185822,"Nueva York",200,450)]
        with patch('User.User.seleccionarvuelo') as mock_requests4:
            mock_requests4.return_value=Vol(185822,"Nueva York",200,450)
            a.agregardestino("Nueva York")
    with patch('Skyscanner.Skyscanner.getlistvuelo') as mock_requests5:
        mock_requests5.return_value=  [Vol(192548,"Barcelona",80,120)]
        with patch('User.User.seleccionarvuelo') as mock_requests6:
            mock_requests6.return_value=Vol(192548,"Barcelona",80,120)
            a.agregardestino("Barcelona")
    a.eliminardestino(destino)
    assert (edestino==a.destinos and a.vuelos.vols==evuelo and a.precio==epreu )

"""
@pytest.mark.parametrize("metodo,error", [
    (("Visa", "Jonathan", 1234567890, 5555),False),
    (("MC", "Ale", 1234532890, 5555),True)])
def test_pagamentvolsformapagamentError(metodo,error):
    a=Viaje(User("Antonio", "47238223L", "08291", "711736632","antonio@gmail.com"),["Antonio","Oscar", "Juan"])
    with patch('Skyscanner.Skyscanner.getlistvuelo') as mock_requests:
        mock_requests.return_value=  [Vol(157892,"Madrid",100,90)]
        with patch('User.User.seleccionarvuelo') as mock_requests1:
            mock_requests1.return_value=Vol(157892,"Madrid",100,90)
            a.agregardestino("Madrid")   
    with patch('Skyscanner.Skyscanner.getlistvuelo') as mock_requests:
        mock_requests.return_value=  [Vol(185822,"Nueva York",200,450)]
        with patch('User.User.seleccionarvuelo') as mock_requests1:
            mock_requests1.return_value=Vol(185822,"Nueva York",200,450)
            a.agregardestino("Nueva York")
    with patch('Bank.Bank.do_payment') as mock_requests:
        mock_requests.return_value=error
        with patch('User.User.rellenardatospago') as mock_requests1:
            mock_requests1.return_value=metodo
            resultado, me=a.pagar()
    assert resultado==error and me==metodo

"""
@pytest.mark.parametrize("error", [
    (True),
    (False)])
def test_confirmareserva(error):
    a=Viaje(User("Antonio", "47238223L", "08291", "711736632","antonio@gmail.com"),["Antonio","Oscar", "Juan"])
    with patch('Skyscanner.Skyscanner.getlistvuelo') as mock_requests:
        mock_requests.return_value=  [Vol(157892,"Madrid",100,90)]
        with patch('User.User.seleccionarvuelo') as mock_requests1:
            mock_requests1.return_value=Vol(157892,"Madrid",100,90)
            a.agregardestino("Madrid")   
    with patch('Skyscanner.Skyscanner.getlistvuelo') as mock_requests:
        mock_requests.return_value=  [Vol(185822,"Nueva York",200,450)]
        with patch('User.User.seleccionarvuelo') as mock_requests:
            mock_requests1.return_value=Vol(185822,"Nueva York",200,450)
            a.agregardestino("Nueva York")
    with patch('Skyscanner.Skyscanner.confirm_reserve') as mock_requests:
        mock_requests.return_value=error
        assert a.confirmareserva_total()==error

@pytest.mark.parametrize("datos,error,resultat", [
    (("visa", 1234567890, 5555),[True],True),
    (("visa", 1234567890, 5555),[False,True],True),
    (("visa", 123456789, 5555),[False,True],False),
    (("visa", 1234567890, 555),[False,True],False),
    (("", 1234567890, 555),[False,True],False),
    (("visa", 1234567890, 5555),[False,False,False,False,False],False)
    ])
def test_pagamentreintenta(datos,error,resultat):
    a=Viaje(User("Antonio", "47238223L", "08291", "711736632","antonio@gmail.com"),["Antonio","Oscar", "Juan"])
    with patch('Skyscanner.Skyscanner.getlistvuelo') as mock_requests:
        mock_requests.return_value=  [Vol(157892,"Madrid",100,90)]
        with patch('User.User.seleccionarvuelo') as mock_requests1:
            mock_requests1.return_value=Vol(157892,"Madrid",100,90)
            a.agregardestino("Madrid")   
    with patch('Skyscanner.Skyscanner.getlistvuelo') as mock_requests:
        mock_requests.return_value=  [Vol(185822,"Nueva York",200,450)]
        with patch('User.User.seleccionarvuelo') as mock_requests1:
            mock_requests1.return_value=Vol(185822,"Nueva York",200,450)
            a.agregardestino("Nueva York")
    with patch('User.User.rellenardatospago') as mock_requests1:
        mock_requests1.return_value=datos
        with patch('Bank.Bank.do_payment') as mock_requests:
            mock_requests.side_effect=error
            resultado, me=a.pagar()
    assert resultado==resultat
    
@pytest.mark.parametrize("error,resultat", [
    ([False,True],True),
    ([False,False,False,False,False],False)
    ])
def test_confirmareservareintenta(error,resultat):
    a=Viaje(User("Antonio", "47238223L", "08291", "711736632","antonio@gmail.com"),["Antonio","Oscar", "Juan"])
    with patch('Skyscanner.Skyscanner.getlistvuelo') as mock_requests:
        mock_requests.return_value=  [Vol(157892,"Madrid",100,90)]
        with patch('User.User.seleccionarvuelo') as mock_requests1:
            mock_requests1.return_value=Vol(157892,"Madrid",100,90)
            a.agregardestino("Madrid")   
    with patch('Skyscanner.Skyscanner.getlistvuelo') as mock_requests:
        mock_requests.return_value=  [Vol(185822,"Nueva York",200,450)]
        with patch('User.User.seleccionarvuelo') as mock_requests:
            mock_requests1.return_value=Vol(185822,"Nueva York",200,450)
            a.agregardestino("Nueva York")
    with patch('Skyscanner.Skyscanner.confirm_reserve') as mock_requests:
        mock_requests.side_effect=error
        assert a.confirmareserva_total()==resultat
        
@pytest.mark.parametrize("viajeros,destino,lcotxe,ecotxe, epreu", [
    (["Antonio"],("Madrid",5),[Cars(1533186,"Mercedes",30,"Madrid",5),Cars(1532286,"Audi",40,"Madrid",5)],[Cars(1533186,"Mercedes",30,"Madrid",5)],150),
    (["Antonio","Maria","Jose","Primo","Eric"],("Madrid",5),[Cars(1533186,"Mercedes",30,"Madrid",5),Cars(1532286,"Audi",40,"Madrid",5)],[Cars(1533186,"Mercedes",30,"Madrid",5),Cars(1532286,"Audi",40,"Madrid",5)],350)
    ])
def test_agregarcotxe(viajeros,destino,lcotxe,ecotxe, epreu):
    a=Viaje(User("Antonio", "47238223L", "08291", "711736632","antonio@gmail.com"),viajeros)
    with patch('Rentalcars.Rentalcars.getlistcotxe') as mock_requests:
        mock_requests.return_value= lcotxe
        with patch('User.User.seleccionarcotxes') as mock_requests1:
            mock_requests1.return_value= ecotxe
            a.agregarcotxe(destino)
    assert (ecotxe==a.cotxes.cars and a.precio==epreu)
    

@pytest.mark.parametrize("eldestino,ecotxe, epreu", [
    ("Madrid",[Cars(696969,"Porsche",90,"Nueva York",5)],450),
    ("Nueva York",[Cars(1533186,"Mercedes",30,"Madrid",5),Cars(1234567,"BMW",50,"Madrid",5)],400)
    ])

def test_eliminarcotxe(eldestino,ecotxe, epreu):
    a=Viaje(User("Antonio", "47238223L", "08291", "711736632","antonio@gmail.com"),["Antonio", "Juan"])
    with patch('Rentalcars.Rentalcars.getlistcotxe') as mock_requests:
        mock_requests.return_value= [Cars(1533186,"Mercedes",30,"Madrid",5),Cars(1234567,"BMW",50,"Madrid",5)]
        with patch('User.User.seleccionarcotxes') as mock_requests1:
            mock_requests1.return_value= [Cars(1533186,"Mercedes",30,"Madrid",5),Cars(1234567,"BMW",50,"Madrid",5)]
            a.agregarcotxe("Madrid")
    with patch('Rentalcars.Rentalcars.getlistcotxe') as mock_requests5:
        mock_requests5.return_value=  [Cars(696969,"Porsche",90,"Nueva York",5)]
        with patch('User.User.seleccionarcotxes') as mock_requests6:
            mock_requests6.return_value=[Cars(696969,"Porsche",90,"Nueva York",5)]
            a.agregarcotxe("Nueva York")            
    a.eliminarcotxe(eldestino)
    assert (ecotxe==a.cotxes.cars and a.precio==epreu)
    
        
   
@pytest.mark.parametrize("viatgers, destino,lhotel,ehotel, epreu", [
    (["Antonio", "Juan"],("Barcelona",5),[Hotels(157892,"Hotel W","Barcelona",2,5,40),Hotels(1234567,"Rafael Hoteles","Barcelona",2,5,80)],[Hotels(157892,"Hotel W","Barcelona",2,5,40)],400), 
    (["Antonio", "Juan","Maria", "Jose"],("Barcelona",5),[Hotels(157892,"Hotel W","Barcelona",2,5,40),Hotels(1234567,"Rafael Hoteles","Barcelona",2,5,80)],[Hotels(157892,"Hotel W","Barcelona",3,5,40),Hotels(157892,"Hotel W","Barcelona",1,5,40)],800)
    ])

def test_agregaralojamiento(viatgers, destino,lhotel,ehotel,epreu):
    a=Viaje(User("Antonio", "47238223L", "08291", "711736632","antonio@gmail.com"),viatgers)
    with patch('Booking.Booking.getlisthotel') as mock_requests:
        mock_requests.return_value=  lhotel
        with patch('User.User.seleccionarhotels') as mock_requests1:
            mock_requests1.return_value= ehotel
            a.agregaralojamiento(destino)
    assert (ehotel==a.hotel.habs and a.precio==epreu)
    
            
@pytest.mark.parametrize("ehotel,destino, epreu", [
    ([Hotels(157892,"Hotel Wola","Madrid",3,1,50),Hotels(157892,"Hotel Wola","Madrid",1,1,50)],"Barcelona",200), 
    ([Hotels(157892,"Hotel W","Barcelona",3,5,40),Hotels(157892,"Hotel W","Barcelona",1,5,40)],"Madrid",800),
    ])

def test_eliminaralojamiento(ehotel,destino,epreu):
    a=Viaje(User("Antonio", "47238223L", "08291", "711736632","antonio@gmail.com"),["Antonio", "Juan"])
    with patch('Booking.Booking.getlisthotel') as mock_requests:
        mock_requests.return_value=  [Hotels(157892,"Hotel W","Barcelona",3,5,40),Hotels(157892,"Hotel W","Barcelona",1,5,40)]
        with patch('User.User.seleccionarhotels') as mock_requests1:
            mock_requests1.return_value= [Hotels(157892,"Hotel W","Barcelona",3,5,40),Hotels(157892,"Hotel W","Barcelona",1,5,40)]
            a.agregaralojamiento(("Barcelona",5))
    with patch('Booking.Booking.getlisthotel') as mock_requests:
        mock_requests.return_value=  [Hotels(157892,"Hotel Wola","Madrid",3,1,50),Hotels(157892,"Hotel Wola","Madrid",1,1,50)]
        with patch('User.User.seleccionarhotels') as mock_requests2:
            mock_requests2.return_value= [Hotels(157892,"Hotel Wola","Madrid",3,1,50),Hotels(157892,"Hotel Wola","Madrid",1,1,50)]
            a.agregaralojamiento(("Madrid",1))
    a.eliminaralojamiento(destino)
    assert (ehotel==a.hotel.habs and a.precio==epreu)

@pytest.mark.parametrize ("tipo,nom,numero,codi,resultat", [
    ("visa", "Jonathan", 1234567890, 5555, ("visa", "Jonathan", 1234567890, 5555)),
    ("", "Joan", 4545454545, 8888,False),
    ("visa", "Victor", 1987654321, 6969,("visa", "Victor", 1987654321, 6969)),
    ("mastercard", "Ivan", 1533186, 1,False),
    ("visa", "Alejandro", 1111111111, 1010,("visa", "Alejandro", 1111111111, 1010))
    ])
    
def test_PaymentData(tipo,nom,numero,codi, resultat):
    
    p=PaymentData(tipo,nom,numero,codi)
    resultado= p.get_datapayment()
    assert resultado == resultat

