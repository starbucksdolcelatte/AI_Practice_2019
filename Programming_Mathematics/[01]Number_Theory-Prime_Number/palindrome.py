'''
회문(palindrome)은 앞으로 읽어도, 뒤로 읽어도 똑같이 읽히는 문장이나 낱말을 뜻합니다.
예를 들면 '소주만병만주소’가 있습니다.
소수 중에도 이렇게 회문이 되는 소수가 있습니다.
101은 소수이면서 회문입니다. 한 자리로만 이루어진 소수도 회문으로 여깁니다.

주어진 n보다 작은 수 중 이러한 회문 소수의 개수를 세는 함수를 작성해 봅시다.
'''
def eratosthenes(n):
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
    # 소수 목록 산출
    return [i for i in range(2, n) if sieve[i] == True]


print(eratosthenes(10))

def palindrome(n):
    # To-do
    primes = eratosthenes(n)
    primes = [str(x) for x in primes]
    res = [True for _ in range(len(primes))]

    j = 0
    for num in primes:
        l = len(num)
        if l == 1:
            pass
        else:
            for i in range(int(l/2)):
                if(num[i] != num[l-1-i]):
                    res[j] = False
        j += 1

    return sum(res)


print(palindrome(10))
