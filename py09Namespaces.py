#_Global variable_____________________________________________---
myVar = "v1"
print("global scope:", myVar)

def func1():
    myVar = "v2"
    print("enclosed scope:", myVar)
    
    def func2():
        myVar = "v3"
        print("Local scope:", myVar)
        print("Local variables in func2:", locals())
        del myVar
    
    func2()
    print("enclosed scope:", myVar)
    print("Local variables in func1:", locals())
    del myVar
    func2()



func1()

print("global scope:", myVar)