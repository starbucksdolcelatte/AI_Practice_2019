'''
점화식

a1 = a
an+1 = p*an + q

an을 구하는 함수 짜기
'''

def recurrSeq2(a, p, q, n):
    # To-do
    if n == 1:
        return a
    else:
        return p * recurrSeq2(a, p, q, n-1) + q




# 결과 출력을 위한 코드입니다. 자유롭게 값을 바꿔보며 확인해보세요.
print(recurrSeq2(1, 2, 3, 5))
