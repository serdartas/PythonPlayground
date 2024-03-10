# / division returns always float
print(type(10/2))

# power is double star
print(2**3)

# logical operators
print(2==2 and (3<4 or 4<3))

# if statement
if 1<2 and not 2<1:
    print("1 is smaller than 2 and 2 is not smaller than 1")

# else statement
if 2<1:
    print("2<1")
elif 2<0:
    print("2<0")
else:
    print("2 is not smaller than 1 or 0")
# switch
http_status = 300
message = ""
match http_status:
    case 200 | 201:
        message="Ok"
    case 404:
        message="Not found"
    case 500:
        message="Server error"
    case _:
        message="Unknown"
print(http_status, message)
# for each loop
for letter in message:
    print(letter)

# for loop
for i in range(5):
    print(i)

for i in range(3,5):
    print("Range 3,5", i)

# while loop
i = 0
while i<5:
    print("While loop", i)
    i+=1 # Note that i++ notation won't work in Ptyhon

# break
numbers = [1, 3, 7, 9, 11, 14, 16]

for num in numbers:
  if num % 2 == 0 and num > 5:
    print("First even number greater than 5:", num)
    break

# continue
for num in range(1, 11):
  if num % 2 != 0: # Check if the number is odd
    continue # Skip to the next iteration if it's odd
  print(num, end = " ")

# pass keyword is used as a placeholder and literally does nothing, using example above with pass
for num in range(1, 11):
  if num % 2 != 0: # Check if the number is odd
    pass # does nothing
  print(num, end = " ")
print("")
# enumerate function returns you data and the index
num_list = ['cats', 'dogs','ducks']

for x,num in enumerate(num_list):
    print(x, num)