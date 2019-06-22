'''
어떤 수 n이 주어졌을 때
n을 넘는 가장 작은 피보나치 수열은 몇 번째 항인지 구하는 함수

입력
n: 자연수

출력
n을 넘는 가장 작은 피보나치 수열의 항 번호
'''

def fibonacci(n):
    # To-do
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def fibonacci2(n):
    # To-do
    i = 1
    while (fibonacci(i) <= n):
        i += 1
    return i


    
print(fibonacci2(2))
