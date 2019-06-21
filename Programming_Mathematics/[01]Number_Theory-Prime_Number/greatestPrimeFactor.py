def eratosthenes(n):
    # 숫자 목록을 준비 (True는 소수임을 의미)
    n += 1
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
    # 소수 목록 산출
    return [i for i in range(2, n) if sieve[i] == True]

def greatPrimeFacter(n):
    s = eratosthenes(n)
    len_s = len(s)-1
    # To-do
    for i in range(len(s)):
        num = s[len_s - i]
        if(n % num == 0):
            return num   


print(greatPrimeFacter(6))
