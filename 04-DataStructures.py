## List
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
## Tuple is an immutable list
# tuple is defined using paranthesis
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
#
#
#
#
#
## Dictionary
#
#
#
#
#
#
## Stack
#
## Queue
#
## Tree
#
## Linked List
#
## Graph
#
## HashMap
#