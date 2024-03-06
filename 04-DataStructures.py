## List____________________________________________________________________________
# List is defined using square brackets
myList = [1, 2.3, "a", True]
print("First item in my list is", myList[1])

# Lists can contain lists and any data type
myList = [1, 2, ["a", "b", "c"]]
print("Third item in my list is", myList[2])
# Some printing examples
myList = ["a", 1, 2, "b"]
print(myList) # ['a', 1, 2, 'b']
print(*myList)# a 1 2 b
myList.insert(2, "2nd item") # insert an item in the given index
print(myList)
myList.append("last item") # append an item to the end of the list
print(myList)
myList.extend([5, 6, 7]) # append a list to end of the list
print(myList)
myList.pop(2) # remove an item from the list
print(myList)
del myList #remove list from memory

## Tuple____________________________________________________________________________
# Tuple is an immutable list defined using paranthesis
myTuple = (1, 'string', 1.2, True)
print(myTuple[1])
# Count method can be used to get the size of tuple or count of specific item in tuple
print(myTuple.count(1.2))
# You can use index to get the index of an item in tuple
print(myTuple.index(1.2))
del myTuple
## Set is a data type that is immutable and has all the items only for once. items are hashed for O(1) search and it is unordered so you can't get the index of an item
mySet = {1, 2, 3, 'a'}
print(mySet)
# you can add and remove items
mySet.add(5)
mySet.remove(2)
print(mySet)
del mySet
# You can use mathematical operators on sets
setA = {1, 2, 3, 4}
setB = {3, 4, 5, 6}
print("A U B =", setA.union(setB))
print("A intersect B =", setA.intersection(setB))
del setA
del setB

## Dictionary____________________________________________________________________________
## Dictionary is a set that contains key value pairs (tuples)
myDict = {'fruit': 'apple', 'main dish':'spagetti', 'drink':'milk', 2:'some number :)'}
myDict["drink"] = 'juice'
del myDict[2]
# to add a new key simply upsert it
myDict["starter"]='bruchetta'

for myPair in myDict.items():
    print(*myPair, sep=':')
# alternatively you can assign tuple into two variables
for key, value in myDict.items():
    print(key, ':', value)

## args & kwargs____________________________________________________________________________
# You can define indefinite amount of input parameters using args.
# Notation is single star before input parameter name
def sumOf(*numbers):
    sum = 0
    for num in numbers:
        sum += num
    return sum
print(sumOf(1,2,3,4))
del sumOf
# You can define indefinite amount of input parameters in key value pair 
# tuples similar to React props using kwargs.
# Notation is double star before input parameter name
def calculateBill(**order):
    sum = 0
    for dish, price in order.items():
        sum += price
    return round(sum, 2)
print(calculateBill(coffee=2.99, cake=4.55, juice=2.99))

## Stack___________________________________________________________________________
# There's no built in stack in Python but you can use list as one
stack = [4, 5, 6]
stack.append(7)
stack.append(8)
print(stack.pop())
print(stack)
del stack
## Queue
from collections import deque
queue = deque([4, 5, 6])
queue.append(7)
print(queue.popleft())
print(queue)


