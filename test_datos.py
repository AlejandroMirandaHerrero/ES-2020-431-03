from User import User
import pytest 


@pytest.mark.parametrize("expected", [
    ("Antonio", "47238223L", "08291", "711736632","antonio@gmail.com"),
    ("Jose", "47224213J", "08290", "691725832","josemiguel@gmail.com"),
    ("Alberto", "46237432H", "08288", "692500663", "alb12@gmail.com"),
    ("Francisco", "46237342D", "08289", "692631634", "paco@gmail.com")])


def test_AñadirDatos(expected:str):
    
    nombre_completo, DNI, direccion_postal, num_tel, email = expected
   
    datos_usuario = User(nombre_completo, DNI, direccion_postal, num_tel, email)
    bo= datos_usuario.get_userdata() == expected
    if not bo:
        print("Error")
    assert datos_usuario.get_userdata() == expected
    

  
