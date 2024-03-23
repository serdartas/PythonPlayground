import pytest
import Palindrome

def test_palindrome():
    assert Palindrome.isPalindrome("ses") == True
    assert Palindrome.isPalindrome("sedes") == True
    assert Palindrome.isPalindrome("cartrac") == True
    assert Palindrome.isPalindrome("tuput") == True

def test_nonpalindrome():
    assert Palindrome.isPalindrome("sek") == False
    assert Palindrome.isPalindrome("serdar") == False
    assert Palindrome.isPalindrome("super") == False
    assert Palindrome.isPalindrome("cart") == False