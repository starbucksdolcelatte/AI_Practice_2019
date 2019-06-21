def eratosthenes(n):
    n += 1
    # 숫자 목록을 준비 (True는 소수임을 의미)
    sieve = [True] * n

    for i in range(2, n):
        # i가 소수인 경우
        if sieve[i] == True:
            # i의 배수를 False 판정
            # To-do
            j = 2
            while (j*i < n):
                sieve[i*j] = False
                j += 1
            pass
    # 소수 목록 산출
    return [i for i in range(2, n) if sieve[i] == True]

def primeFactor(n):
    # To-do

    s = eratosthenes(n)
    res = []
    for i in range(len(s)):
        while(n % s[i] == 0):
            n /= s[i]
            res.append(s[i])

    return res

print(primeFactor(17))
