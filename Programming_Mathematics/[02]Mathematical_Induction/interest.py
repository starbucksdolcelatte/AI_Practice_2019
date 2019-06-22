'''
복리를 구해보자
원금 a, 이자율 r일 때, n년 후 총 이자의 금액
'''
def interest(a, r, n):
    # To-do
    res = a
    for i in range(n):
        res = res + res*r
    return res - a




print(interest(1000000, 0.01, 2))
