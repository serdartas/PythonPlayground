# Classical first line of code
print("Hello world!")

# two lines in one line
print("1st command"); print("2nd command")

# use a back slash \ to continue command in next line
print("this is \
actually a one liner!")

# if statement
if 1==1:
    print("You need to use indents ")

# any ammount of whitespace on a single line is ok
x     =        1        +        2

# define a void function
def say_hello():
    print("Hello there!")

say_hello()

# define a function with input parameter
def say_my_name(name):
    print(name)

say_my_name("My name is Serdar")

# define a function that returns a value
def add_two_numbers(num1, num2):
    return num1 + num2

print(add_two_numbers(1,2))

# variables can change their types on the go!
intVar = 3          # intVar is an integer
intVar = "string"   # now it is a string

# assign multiple values in same line
a, b, c = 1, 2, 3
print(a+b+c)

# you can also print multiple variables in one line
print(a, b, c)

# you can dispose variable with del command
del a

# of course you can dispose multiple ones of them in one line
del b, c, intVar

# python data types are as follows:
# numeric (interger, float, complex number)
# sequence (string, list, tuple)
# dictionary
# bool
# set

# you can use type() to write the type of the variable
myVar = 1
print(type(myVar))

# define a float
myVar = 1.0
print(type(myVar))

# define a complex number
myVar = 10 + 10j
print(type(myVar))

# define a string
myVar = "string"
print(type(myVar))

# define a list
myVar = [1 , "a", 5]
print(type(myVar))

# define a tuple
myVar = (1, 'hello', 4.5, "world")
print(type(myVar))

# define a dictionary
myVar = {'height':182, 'weight': 85}
print(type(myVar))

# define a bool
myVar = True
print(type(myVar))

# define a set
myVar = {1, 'hello', 3, "world"}
print(type(myVar))


# Try Catch
try:
    1/0
except:
    print("Error!")

# Try catch with the exception itself
try:
    1/0
except Exception as e:
    print("Error!", e)

# Try catch with the specifit error types
try:
    1/0
except ZeroDivisionError:
    print("Zero division error")
except Exception as e:
    print("Error!", e)