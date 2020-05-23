import pytest
from Viaje import Viaje
from User import User
from Vol import Vol
from Cars import Cars
from Hotels import Hotels
from unittest.mock import patch
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
    (["Antonio"],"Madrid",["Madrid"],[Vol(157892,"Madrid",100,90)],90),
    (["Antonio", "Juan"],"Madrid",["Madrid"],[Vol(157892,"Madrid",100,90)],180)
    ])
    
def test_agregardestino(viajeros,destino,edestino,evuelo,epreu):
    u=User("Antonio", "47238223L", "08291", "711736632","antonio@gmail.com")
    a=Viaje(u,viajeros)
    with patch('Skyscanner.Skyscanner.getlistvuelo') as mock_requests:
        mock_requests.return_value=  [Vol(157892,"Madrid",100,90)]
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

@pytest.mark.parametrize("metodo,error", [
    ("VISA",False),
    ("MC",False),
    ("VISA",True),
    ("MC",True)])
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
        with patch('User.User.seleccionarMetodo') as mock_requests1:
            mock_requests1.return_value=metodo
            resultado, me=a.pagar()
    assert resultado==error and me==metodo

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
        assert a.confirmareserva()==error
        
@pytest.mark.parametrize("error,resultat", [
    ([False,True],True),
    ([False,False,False,False,False],False)
    ])
def test_pagamentreintenta(error,resultat):
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
        assert a.confirmareserva()==resultat
        
@pytest.mark.parametrize("viajeros,ecotxe,destino, epreu", [
    (["Antonio"],[Cars(1533186,"Mercedes",30,"Madrid",5)],"Madrid",150)
    ])

def test_agregarcotxe(viajeros,ecotxe,destino,epreu):
    u=User("Antonio", "47238223L", "08291", "711736632","antonio@gmail.com")
    a=Viaje(u,viajeros)
    with patch('Rentalcars.Rentalcars.getlistcotxe') as mock_requests:
        mock_requests.return_value=  [Cars(1533186,"Mercedes",30,"Madrid",5)]
        with patch('User.User.seleccionarcotxe') as mock_requests1:
            mock_requests1.return_value= Cars(1533186,"Mercedes",30,"Madrid",5)
            a.agregarcotxe(ecotxe, destino)
    assert (ecotxe==a.cotxes.cars and a.precio==epreu)
    
@pytest.mark.parametrize("viajeros,ecotxe,destino, epreu", [
    (["Antonio", "Juan"],[Cars(1533186,"Mercedes",30,"Madrid",5),(Cars(1234567,"BMW",50,"Madrid",5))], "Madrid",400)
    ])

def test_eliminarcotxe(viajeros,ecotxe,destino,epreu):
    u=User("Antonio", "47238223L", "08291", "711736632","antonio@gmail.com")
    a=Viaje(u,viajeros)
    
    with patch('Rentalcars.Rentalcars.getlistcotxe') as mock_requests:
        mock_requests.return_value=  [Cars(1533186,"Mercedes",30,"Madrid",5)]
        with patch('User.User.seleccionarcotxe') as mock_requests1:
            mock_requests1.return_value= Cars(1533186,"Mercedes",30,"Madrid",5)
            a.agregarcotxe(Cars(1533186,"Mercedes",30,"Madrid",5), "Madrid")
            
    with patch('Rentalcars.Rentalcars.getlistcotxe') as mock_requests3:
        mock_requests3.return_value=  [Cars(1533186,"BMW",50,"Madrid",5)]
        with patch('User.User.seleccionarcotxe') as mock_requests4:
            mock_requests4.return_value= Cars(1234567,"BMW",50,"Madrid",5)
            a.agregarcotxe(Cars(1234567,"BMW",50,"Madrid",5), "Madrid")
            
    with patch('Rentalcars.Rentalcars.getlistcotxe') as mock_requests5:
        mock_requests5.return_value=  [Cars(696969,"Porsche",90,"Nueva York",5)]
        with patch('User.User.seleccionarcotxe') as mock_requests6:
            mock_requests6.return_value=Cars(696969,"Porsche",90,"Nueva York",5) 
            a.agregarcotxe(Cars(696969,"Porsche",90,"Nueva York",5), "Nueva York")
            
    a.eliminarcotxe(696969)
    assert (ecotxe==a.cotxes.cars and a.precio==epreu)
    
    
@pytest.mark.parametrize("error,resultat", [
([False,False,True],True),
([False,False,False,False,False],False)
])
def test_hotelreintenta(error,resultat):
    a=Viaje(User("Antonio", "47238223L", "08291", "711736632","antonio@gmail.com"),["Antonio","Oscar", "Juan"])
    
    with patch('Booking.Booking.getlisthotel') as mock_requests:
        mock_requests.return_value=  [Hotels(7654321,"Masia Cuatregats",4,2,5,10)]
        with patch('User.User.seleccionarhotel') as mock_requests:
            mock_requests.return_value=Hotels(7654321,"Masia Cuatregats",4,2,5,10)
            a.agregaralojamiento((7654321,"Masia Cuatregats",4,2,5,10),"Tarragona")
            
    with patch('Booking.Booking.getlisthotel') as mock_requests:
        mock_requests.return_value=  [Hotels(1234567,"Rafael Hoteles",4,2,5,30)]
        with patch('User.User.seleccionarhotel') as mock_requests:
            mock_requests.return_value=Hotels(1234567,"Rafael Hoteles",4,2,5,30)
            a.agregaralojamiento((1234567,"Rafael Hoteles",4,2,5,30),"Barcelona")   

            
    with patch('Booking.Booking.getlisthotel') as mock_requests1:
        mock_requests1.return_value=  [Hotels(157892,"Hotel W",4,2,5,40)]
        with patch('User.User.seleccionarhotel') as mock_requests1:
            mock_requests1.return_value=Hotels(157892,"Hotel W",4,2,5,40)
            a.agregaralojamiento((157892,"Hotel W",4,2,5,40),"Barcelona")   
        
        
    with patch('Booking.Booking.confirm_reserve') as mock_requests:
        mock_requests.side_effect=error
        assert a.confirmareserva_alojamiento()==resultat
        
        
@pytest.mark.parametrize("viajeros,ehotel,destino, epreu", [
    (["Antonio","Raul", "Sonia","Lucia"],[Hotels(157892,"Hotel W",4,2,5,40),Hotels(1234567,"Rafael Hoteles",8,2,5,40)],"Barcelona",2400), 
    ])

def test_agregaralojamiento(viajeros,ehotel,destino,epreu):
    u=User("Antonio", "47238223L", "08291", "711736632","antonio@gmail.com")
    a=Viaje(u,viajeros)
    with patch('Booking.Booking.getlisthotel') as mock_requests:
        mock_requests.return_value=  [Hotels(157892,"Hotel W",4,2,5,40)]
        with patch('User.User.seleccionarhotel') as mock_requests1:
            mock_requests1.return_value= Hotels(157892,"Hotel W",4,2,5,40)
            a.agregaralojamiento(ehotel, "Barcelona")
            
    with patch('Booking.Booking.getlisthotel') as mock_requests:
        mock_requests.return_value=  [Hotels(1234567,"Rafael Hoteles",8,2,5,40)]
        with patch('User.User.seleccionarhotel') as mock_requests2:
            mock_requests2.return_value= Hotels(1234567,"Rafael Hoteles",8,2,5,40)
            a.agregaralojamiento(ehotel, destino)
        assert (ehotel==a.hotel.hotels and a.precio==epreu)
    
  
@pytest.mark.parametrize("viajeros,ehotel,destino, epreu", [
    (["Antonio","Raul", "Sonia","Lucia"],[Hotels(157892,"Hotel W",4,2,5,40),Hotels(1234567,"Rafael Hoteles",8,2,5,40)],"Barcelona",2400), 
    ])

def test_eliminaralojamiento(viajeros,ehotel,destino,epreu):
    u=User("Antonio", "47238223L", "08291", "711736632","antonio@gmail.com")
    a=Viaje(u,viajeros)
    
    with patch('Booking.Booking.getlisthotel') as mock_requests:
        mock_requests.return_value=  [Hotels(157892,"Hotel W",4,2,5,40)]
        with patch('User.User.seleccionarhotel') as mock_requests1:
            mock_requests1.return_value= Hotels(157892,"Hotel W",4,2,5,40)
            a.agregaralojamiento(ehotel, "Barcelona")
            
    with patch('Booking.Booking.getlisthotel') as mock_requests:
        mock_requests.return_value=  [Hotels(1234567,"Rafael Hoteles",8,2,5,40)]
        with patch('User.User.seleccionarhotel') as mock_requests2:
            mock_requests2.return_value= Hotels(1234567,"Rafael Hoteles",8,2,5,40)
            a.agregaralojamiento(ehotel, destino)
            
    with patch('Booking.Booking.getlisthotel') as mock_requests:
        mock_requests.return_value=  [Hotels(7654321,"Masia Cuatregats",4,2,5,10)]
        with patch('User.User.seleccionarhotel') as mock_requests3:
            mock_requests3.return_value=Hotels(7654321,"Masia Cuatregats",4,2,5,10)
            a.agregaralojamiento((7654321,"Masia Cuatregats",4,2,5,10),"Tarragona")
            
    a.eliminaralojamiento(7654321)
    assert (ehotel==a.hotel.hotels and a.precio==epreu)





@pytest.mark.parametrize("error", [
    (True),
    (False)])
def test_confirmareservacotxes(error):
    a=Viaje(User("Antonio", "47238223L", "08291", "711736632","antonio@gmail.com"),["Antonio","Oscar", "Juan"])
    with patch('Rentalcars.Rentalcars.getlistcotxe') as mock_requests:
        mock_requests.return_value=  [Cars(1533186,"Mercedes",30,"Madrid",5)]
        with patch('User.User.seleccionarcotxe') as mock_requests1:
            mock_requests1.return_value=Cars(1533186,"Mercedes",30,"Madrid",5)
            a.agregarcotxe(Cars(1533186,"Mercedes",30,"Madrid",5), "Madrid")    
    with patch('Rentalcars.Rentalcars.getlistcotxe') as mock_requests2:
        mock_requests2.return_value=  [Cars(1234567,"BMW",50,"Madrid",5)]
        with patch('User.User.seleccionarcotxe') as mock_requests3:
            mock_requests3.return_value=Cars(1234567,"BMW",50,"Madrid",5)
            a.agregarcotxe(Cars(1234567,"BMW",50,"Madrid",5), "Madrid")
    with patch('Rentalcars.Rentalcars.confirm_reserve') as mock_requests4:
        mock_requests4.return_value=error
        assert a.confirmareserva_coche()==error
        
@pytest.mark.parametrize("error,resultat", [
    ([False,True],True),
    ([False,False,False,False,False],False)
    ])
def test_confirmareservareintentacotxes(error,resultat):
    a=Viaje(User("Antonio", "47238223L", "08291", "711736632","antonio@gmail.com"),["Antonio","Oscar", "Juan"])
    with patch('Rentalcars.Rentalcars.getlistcotxe') as mock_requests:
        mock_requests.return_value=  [Cars(1533186,"Mercedes",30,"Madrid",5)]
        with patch('User.User.seleccionarcotxe') as mock_requests1:
            mock_requests1.return_value=Cars(1533186,"Mercedes",30,"Madrid",5)
            a.agregarcotxe(Cars(1533186,"Mercedes",30,"Madrid",5), "Madrid")   
    with patch('Rentalcars.Rentalcars.getlistcotxe') as mock_requests2:
        mock_requests2.return_value= [Cars(1234567,"BMW",50,"Madrid",5)]
        with patch('User.User.seleccionarcotxe') as mock_requests3:
            mock_requests3.return_value=Cars(1234567,"BMW",50,"Madrid",5)
            a.agregarcotxe(Cars(1234567,"BMW",50,"Madrid",5), "Madrid")
    with patch('Rentalcars.Rentalcars.confirm_reserve') as mock_requests4:
        mock_requests4.side_effect=error
        assert a.confirmareserva_coche()==resultat