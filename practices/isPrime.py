def isPrime(intNum):
    if intNum < 4:
        return True
    for num in range(2,int(intNum**0.5)+1):
        if intNum % num == 0:
            return False
    return True
