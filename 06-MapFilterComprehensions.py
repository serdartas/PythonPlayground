from practices.isPrime import isPrime
cities = ["New York", "Chicago", "Michigan", "Portland", "Washington", "Atlanta", "Dallas", "New Hampshire", "Nashville", "New Orleans", "Newark"]

# Map and Filter both requires a function to be used in the list provided
# Here is a basic one to filter items starting with letter "N"

def nCities(city):
    if city[0:1]=='N':
        return city

# Map will iterate through each item in the iterable and return the output of the provided function in a map class <class 'map'>
mapOutput = map(nCities, cities)
print("\n", "Map_______________________________________________________________________________________________", sep="")
print("Type of output from map function is", type(mapOutput))
print("This is how it looks when printed", mapOutput)
print("Here are the contents to output:")
for item in mapOutput:
    print(item)
del mapOutput

# Map function creates an item in output for each inoput item in iterable. Hence, although function doesn't return any value for some items, output contains nulls there
# Filter function, filters out "None"s
filterOutput = filter(nCities, cities)
print("\n", "Filter____________________________________________________________________________________________", sep="")
print("Type of output from map function is", type(filterOutput))
print("This is how it looks when printed", filterOutput)
print("Here are the contents to output:")
for item in filterOutput:
    print(item)
del filterOutput

# Comprehensions is the way to create a new sequence from an existing sequence
print("\n", "Comprehensions_____________________________________________________________________________________", sep="")
cities = ["City: " + city for city in cities]
print(cities)

del cities
myList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Comprehensions work like an SQL query, you can filter input data using if statement
# here is the syntax for list
# [ <expression> for x in <sequence> if <condition>]

# Print odd numbers
print("Odd numbers: ", [num for num in myList if num % 2 == 1 ])
# Print square of odd numbers
print("Square of odd numbers: ", [num**2 for num in myList if num % 2 == 1 ])
# Print prime numbers between 1 and 100
print("Prime numbers: ", [num for num in range(1,100) if isPrime(num)])


# Comprehensions also work on dictionaries.
print({"Square of " + str(i):i**2 for i in range(1, 5)})

# zip function creates tuples out of given iterables
monthNames = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
monthNums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# zip returns an object of a type zip whihc you can cast into a dictionary
months = dict(zip(monthNames, monthNums))
print(months)
del months

# Using comprehensions instead of casting
months = {key:value for (key, value) in zip(monthNums, monthNames)}
print(months)
del months
# You can also create a set with comprehensions
months = {month for month in monthNames}
print(months)


