import pytest as pt
from isPrime import isPrime

def test_prime():
    assert isPrime(5) == True
    assert isPrime(7) == True
    assert isPrime(11) == True

def test_nonPrime():
    assert isPrime(4) == False
    assert isPrime(9) == False
    assert isPrime(15) == False

def test_edgeCases():
    assert isPrime(0) == False
    assert isPrime(1) == True
    assert isPrime(2) == True
    assert isPrime(3) == True