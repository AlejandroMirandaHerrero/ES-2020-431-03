import pytest
from Viaje import Viaje
from User import User
from Vol import Vol
from unittest.mock import patch
from Skyscanner import Skyscanner
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
            resultado, me=a.pagarvuelo()
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
        resultado, me=a.pagarvuelo()
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
    



