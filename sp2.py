# -*- coding: utf-8 -*-
"""
Created on Fri May 22 21:56:09 2020

@author: Ivan
"""

##en la clase viaje
    def errorreservaCoche(self):
        if not self.confirmareserva_coche():
            print('no se ha pogut fer la reserva adecuadament')
            return True
        else:
            return False
    def errorreservaAlojamiento(self):
        if not self.confirmareserva_alojamiento():
            print('no se ha pogut fer la reserva adecuadament')
            return True
        else:
            return False
        
##en payment_test
@pytest.mark.parametrize ("expected,result", [([
    ("visa", "Jonathan", 1533186, 888),
    ("mastercard", "Joan", 1533186, 888),
    ("visa", "Victor", 1533186, 888),
    ("mastercard", "Ivan", 1533186, 888),
    ("visa", "Alejandro", 1533186, 888)],True)])

def test_maximIntents(expected:list,result:bool):
    max_intents=5
    b=False
    i=0
    #for x in expected:
    while(b==False and i<max_intents):
        tipo,nombre,numero,codigo=expected[i]
        datos_bancarios= PaymentData(tipo,nombre,numero,codigo)
        bo= datos_bancarios.get_datapayment() == expected[i]

        if not bo:
            b=False
        else:
            b=True
        if not b:
            i+=1
    if i==max_intents:
        x=False
        print('has arribat al maxim de intents')
    else:
        x=True
    assert result==x 

## del test_viaje
@pytest.mark.parametrize("viajeros,error", [
    (["Antonio", "Juan"],False),
    (["Antonio"],False)])
def test_errorreservaCoche(viajeros,error):
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
    assert error==a.errorreservaCoche()

@pytest.mark.parametrize("viajeros,error", [
    (["Antonio", "Juan"],False),
    (["Antonio"],False)])
def test_errorreservaAlojamiento(viajeros,error):
    u=User("Antonio", "47238223L", "08291", "711736632","antonio@gmail.com")
    a=Viaje(u,viajeros)
    with patch('Booking.Booking.getlisthotel') as mock_requests:
        mock_requests.return_value=[Alojamiento(1234,'Ibis',2,1,7)]
        with patch('User.User.seleccionaralojamiento') as mock_requests1:
            mock_requests1.return_value= Alojamiento(1234,'Ibis',2,1,7)
            a.agregaralojamiento([Alojamiento(1234,'Ibis',2,1,7)])
    with patch('Booking.Booking.getlisthotel') as mock_requests:
        mock_requests.return_value=[Alojamiento(5678,'Vela',2,1,7)]
        with patch('User.User.seleccionaralojamiento') as mock_requests1:
            mock_requests1.return_value= Alojamiento(5678,'Vela',2,1,7)
            a.agregaralojamiento([Alojamiento(5678,'Vela',2,1,7)])
    assert error==a.errorreservaAlojamiento()