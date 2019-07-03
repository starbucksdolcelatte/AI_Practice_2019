'''
파이썬은 함수를 정의할 때 함수 인자를 따로 설정하지 않고
함수를 사용할 때마다 필요한 만큼 넣을 수 있게 하는 기능을 제공합니다.
'''

# function(*args)
# 정해지지 않은 수의 파라미터를 튜플 형태로 args라는 이름의 변수에 저장합니다.
def adder(*args):
    return sum(args)
print(adder(3,2,1)) # 6
print(adder(1,2,3,4,5,6,7,8,9,10),'\n\n') # 55

def avg(*args):
    return sum(args)/len(args)
print(avg(1,2,3)) # 2.0
print(avg(35,45,85,97,98)) # 72.0

def print_input(*args):
    for i, v in enumerate(args):
        print(f'{i+1}번째로 입력받은 값 : {v}')
print_input('하이') # 1번째로 입력받은 값 : 하이
print('')
print_input('가', '나', '다라마')
'''
1번째로 입력받은 값 : 가
2번째로 입력받은 값 : 나
3번째로 입력받은 값 : 다라마
'''
