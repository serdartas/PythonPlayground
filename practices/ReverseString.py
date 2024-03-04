def reverse(str):
    return str[::-1] # str[start:stop:step]

print(reverse("string"))

def recursiveReverse(str):
    if len(str) == 1:
        return str
    return recursiveReverse(str[1:]) + str[0:1]

print(recursiveReverse("string"))