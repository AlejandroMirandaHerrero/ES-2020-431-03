# -*- coding: utf-8 -*-
"""
Created on Wed May 13 23:10:23 2020

@author: Ivan
"""
import pytest
import Hotels
import Cars
import math


"""@pytest.mark.parametrize("n_usuaris, preu_viatge, cotxe", [
    (2, 100,Cars(10,12345,"BMW","centre",7),170),
    (8, 100, Cars(10,12345,"BMW","centre",7),240),
    ])

def test_viatge_i_cotxes(n_usuaris,preu_viatge,cotxe : Cars,preu_final):
    if (n_usuaris%5) == 0:
        n_cotxes=n_usuaris/5
    else:
        n_cotxes=math.trunc(n_usuaris/5)+1
    print(n_cotxes)
    preu=preu_viatge+(n_cotxes*cotxe.preu_per_dia*cotxe.n_dies)
    print(preu)
    assert preu==preu_final
    
def test_viatge_no_cotxe(n_usuaris,preu_viatge,cotxe : Cars,preu_final):
    if (n_usuaris%5) == 0:
        n_cotxes=n_usuaris/5
    else:
        n_cotxes=math.trunc(n_usuaris/5)+1
    print(n_cotxes)
    preu=preu_viatge-(n_cotxes*cotxe.preu_per_dia*cotxe.n_dies)
    print(preu)
    assert preu==preu_final
    
def test_viatge_i_hotel(preu_viatge,hotel:Hotels,preu_final):
    
    preu=preu_viatge+(hotel.n_habitacions*hotel.n_dies*hotel.preu_per_dia)
    print(preu)
    assert preu==preu_final
    
def test_viatge_no_hotel(preu_viatge,hotel:Hotels,preu_final):
    
    preu=preu_viatge-(hotel.n_habitacions*hotel.n_dies*hotel.preu_per_dia)
    print(preu)
    assert preu==preu_final
"""