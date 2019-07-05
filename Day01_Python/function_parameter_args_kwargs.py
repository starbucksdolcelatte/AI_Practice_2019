'''
function(*args, **kwargs): args와 kwargs 특징을 모두 갖는 함수를 정의합니다.
별 한개(*)는 불특정 다수의 인자를 키워드 없이 튜플 형태로 받음
별 두개(**)는 불특정 다수의 인자를 키워드와 함께 딕셔너리 형태로 받음
'''
# "*args", "**kwargs"를 사용하여 파라미터로 파라미터로 받은 'arg 변수'를
# '**kwargs'를 통해 받은 값들과 곱한 다음
# '변수이름 : 변수값'의 형태로 출력하는 함수를 만들어 봅니다.
def print_func2(*args, **kwargs):
    for k in kwargs.keys():
        print(f"{k}:{args[0]* kwargs[k]}")
    print('GPA:',sum([args[0] * int(kwargs[k]) for k in kwargs.keys()]))

print_func2(0.25, english = 85, math = 98, korean = 100, history = 85)
