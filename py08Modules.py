# CTRL or CMD click on the module to go in the definition
#_sys_____________________________________________________________________________________________
import sys
info = {"version: ":sys.version, "platform: ": sys.platform, "path: ": sys.path, "copyright: ": sys.copyright, ": ": sys.modules}
print(info)


#_calendar_____________________________________________________________________________________________

import calendar

print("there are", calendar.leapdays(2000, 2024), "leap days between 2000 and 2024")
if calendar.isleap(2024):
    print("2024 has 29 days in February")

# You can import .py files without using the extension
import py01HelloWorld
print(py01HelloWorld.add_two_numbers(1,2))
# you will notice import runs every line in the file to be able to initialize the file

# You can add a folder to path using sys.path.insert()
sys.path.insert(1, r'E:\Repos\PythonPlayground\practices')

import isPrime
if isPrime.isPrime(123):
    print("123 is a prime number")
else:
    print("123 is not a prime number")