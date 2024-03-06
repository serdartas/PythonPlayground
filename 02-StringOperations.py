# You can use input() function to read string input from console
myStringVar = input("Your name:")
print("Hello", myStringVar)

# You can define strings with double quotes or single quotes
myStringVar = "Hello world!"
myStringVar = 'Hello Jupiter!'

# for long strings you can use back slash to enter multiline text
myStringVar = "This is a very long string, \
hence we continue in the next line with \
a back slash!"

#  Multiline strings are created with triple single or double quotes
myStringVar = '''This is a
multiline string
built using triple
quotes'''

# Strings are char arrays, you can get the char at index in the same way as any other array
print(myStringVar[1], myStringVar[2]) # h i

# Substrings are also taken using array methods
print(myStringVar[1:3]) # hi

# You can concatanete strings using plus sign
myStringVar = "Two" + " words"

# len() brings the array size of the string
print("'" + myStringVar + "' has", len(myStringVar), "charachters") # 'Two words' has 9 charachters

# Change the case in string using string.lower() or string.upper()
print(myStringVar.upper()) # TWO WORDS

# Trim using strip method
myStringVar = "     my string       "
print(myStringVar.strip()) # my string

# You can create string arrays from your string using split method
myStringVar = "One two three are my favorite numbers"
myStringArray = myStringVar.split(" ") # ['One', 'two', 'three', 'are', 'my', 'favorite', 'numbers']
print(myStringArray) # two

# Find the starting index of the first occurance of a substring
print(myStringVar.find("two"))

# Replace a substring (doesn't modify the string itself)
print(myStringVar.replace("two", "twee"))
print(myStringVar.replace("t", "w", 2)) # replace first two occurance only

# You can convert any type into string using str function
myStringVar = str(123)
print(type(myStringVar))

# Direct formatting is available using format method of print function
outputText = "One of the brightest people in the history was named {}. His last name was {}"
a = "Nicola"
b = "Tesla"
print(outputText.format(a, b))

# You can specify the order
outputText = "One of the brightest people in the history was named {1}. His last name was {2}"
print(outputText.format("hello", a, b))