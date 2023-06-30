import pytest
import math
from src.main import suma
from src.main import resta
from src.main import multiplicacion
from src.main import division
from src.main import seno
from src.main import coseno
from src.main import tangente 
from src.main import resolver_ecuaciones 

def test_suma():
    assert suma(3, 5) == 8
def test_resta():
    assert resta(-7, 4) == -11
def test_multiplicacion():
    assert multiplicacion(2.5, 1.8) == 4.5
def test_division():
    assert division(8, 0) == None
def test_seno():
    assert seno(234) == -0.8090169943749473
def test_coseno():
    assert coseno(-46) == 0.6946583704589973
def test_tangente():
    assert tangente(0) == 0
def test_resolver_ecuaciones():
     assert resolver_ecuaciones(1, 2, 3, 3, 2, 1) == (-1.0, 2.0)


    
    


