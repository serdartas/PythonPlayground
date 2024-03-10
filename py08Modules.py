# CTRL or CMD click on the module to go in the definition
#_sys_____________________________________________________________________________________________
import sys
info = {"version: ":sys.version, "platform: ": sys.platform, "path: ": sys.path, "copyright: ": sys.copyright, ": ": sys.modules}
print(info)


#_assign alias to imported module_____________________________________________________________________________________________

import calendar as c

print("there are", c.leapdays(2000, 2024), "leap days between 2000 and 2024")
if c.isleap(2024):
    print("2024 has 29 days in February")

#_partial/method import_____________________________________________________________________________________________
from math import factorial, ceil # or simply use * to import all
print("factorial 4 is", factorial(4))
print("celiling of 9.5 is", ceil(9.5))
# method import with alias
from math import sqrt as sx
print("square root of 16 is", sx(16))


#_own files_____________________________________________________________________________________________
# You can import .py files without using the extension
import py01HelloWorld
print(py01HelloWorld.add_two_numbers(1,2))
# you will notice import runs every line in the file to be able to initialize the file

# You can add a folder to path using sys.path.insert()
sys.path.insert(1, r'./practices')

import isPrime
if isPrime.isPrime(123):
    print("123 is a prime number")
else:
    print("123 is not a prime number")

# reload function cna be used to reload the imported module. This could be useful for dynamicly changing modules\
# imported 
from importlib import reload
reload(isPrime)

