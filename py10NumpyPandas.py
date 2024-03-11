import numpy as np
# Create a two dimentional array which contains only zeros
arr = np.zeros((3,3))
print(arr)

# Create 2 dimentional array with 5s
arr = np.full((2,2), 5)
print(arr)

# Equally split the values between two given values in given times
arr = np.linspace(0, 12, 4)
print(arr)


import pandas as pd

a = pd.DataFrame({'Animals': ['Dog','Cat','Lion','Cow','Elephant'],
                    'Sounds':['Barks','Meow','Roars','Moo','Trumpet']})

print(a)
print(a.describe())

b = pd.DataFrame({
    "Letters" : ['a', 'b', 'c', 'd', 'e', 'f'],
    "Numbers" : [12, 7, 9, 3, 5, 1]  })

print(b.sort_values(by="Numbers"))

b = b.assign(new_values = b['Numbers']*3)
print(b)
