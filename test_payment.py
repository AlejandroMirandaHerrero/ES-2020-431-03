# -*- coding: utf-8 -*-
"""
Created on Thu May 14 10:57:33 2020

@author: Jonathan
"""

from PaymentData import PaymentData
import pytest

@pytest.mark.parametrize ("expected", [
    ("visa", "Jonathan", 1533186, 888),
    ("mastercard", "Joan", 1533186, 888),
    ("visa", "Victor", 1533186, 888),
    ("mastercard", "Ivan", 1533186, 888),
    ("visa", "Alejandro", 1533186, 888)])
    



    
def test_PaymentData(expected:str):
    
    tipo,nombre,numero,codigo= expected
    
    datos_bancarios= PaymentData(tipo,nombre,numero,codigo)
    
    assert datos_bancarios.get_datapayment() == expected
