#The more effective version
def isPrime2(n):
    # To-do
    if(n<=1):
        return False
    if(n%2 == 0):
        return False
    else:
        for i in range(1, int(n**0.5)):
            if(n % (i*2+1) == 0):
                return False
        return True
    pass

print(isPrime2(17))
