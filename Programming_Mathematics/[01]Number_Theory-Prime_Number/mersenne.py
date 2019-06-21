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

def mersenne(n):
    return isPrime2(2**n-1)


# 결과 출력을 위한 코드입니다. 자유롭게 값을 바꿔보며 확인해보세요.
print(mersenne(2))
