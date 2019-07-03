'''
파이썬은 함수를 정의할 때 함수 인자를 따로 설정하지 않고
함수를 사용할 때마다 필요한 만큼 넣을 수 있게 하는 기능을 제공합니다.
# function(**kwargs)
# ‘keyword=value’ 라는 형태로 값을 받으며,
이를 {‘keyword’: value} 형태를 지닌 kargs라는 이름의 딕셔너리 값으로 저장합니다.
'''

# "**kargs"를 사용하여 파라미터로 입력되는 모든 변수들을
# print 함수를 통해서 '변수이름 : 변수값'의 형태로 출력하는 함수를 만들어 봅니다.
def print_func(**kwargs):
    for key in kwargs.keys():
        print(key, ':', kwargs[key])
    print(f'합계 : {sum(kwargs.values())}')
print('\n\n***** print_func *****')
print_func(num1 = 3, num2 = 5, num3 = 10)

# 내가 만든 시리 함수
def siri(**kwargs):
    for key in kwargs.keys():
        print(f'{key} : {kwargs[key]}')
    if 'call' in kwargs.keys():
        if 'Siri야' in kwargs['call'] or '시리야' in kwargs['call']:
            print('네, 부르셨어요?')
        else:
            print('묵묵부답')
    else:
        print('묵묵..')
        pass
print('\n\n***** siri *****')
siri(call = 'Siri야') # 네, 부르셨어요?
siri(call = '시리야') # 네, 부르셨어요?
siri(call = '시리아') # 묵묵부답
siri(call = 'OK Google!') # 묵묵부답
siri(click = 'On') # 묵묵..

'''
Python dictionary의 .get() 함수는 key에 해당하는 value를 돌려준다.
만약 key가 없으면 None 또는 설정해둔 default 값을 반환한다.
'''
print('\n\n***** dictionary.get(key) *****')
print({0:'영', 1:'일', 2:'이'}.get(0)) # '영'
print({0:'영', 1:'일', 2:'이'}.get(3)) # None
print({0:'영', 1:'일', 2:'이'}.get(3, '없는 숫자입니다.')) # '없는 숫자입니다.'

'''
Python의 dictionary .get() 속성을 이용하여 간결하게 switch문을 만들 수 있다.
참고: https://thrillfighter.tistory.com/602
'''
def switch(x):
    order_dict = {'음악 들려줘' : '최근에 자주 들은 노래를 재생할게요.',
            '엽떡 배달해줘' : '배달의민족 어플에서 시켜드릴게요.'}
    print(f"Siri   : {order_dict.get(x, '무슨 말씀인지 못 알아 들었어요.')}")
print('\n\n***** switch *****')
switch('음악 들려줘이이잉') # '무슨 말씀인지 못 알아 들었어요.'

def updated_siri(**kwargs):
    for key in kwargs.keys():
        pass
    if 'call' in kwargs.keys():
        print(f"사용자 : {kwargs['call']}")
        if 'Siri야' in kwargs['call'] or '시리야' in kwargs['call']:
            print('Siri   : 네, 부르셨어요?')
            if 'order' in kwargs.keys():
                print(f"사용자 : {kwargs['order']}")
                switch(kwargs['order'])
        else:
            print('Siri   : 묵묵부답')
    else:
        print('묵묵..')
        pass
print('\n\n***** updated_siri *****')
updated_siri(call = '시리야', order = '엽떡 배달해줘')
updated_siri(call = '시리야', order = '꺼져')
updated_siri(call = '빅스비!', order = '음악 들려줘')
'''
### OUTPUT ###
***** updated_siri *****
사용자 : 시리야
Siri   : 네, 부르셨어요?
사용자 : 엽떡 배달해줘
Siri   : 배달의민족 어플에서 시켜드릴게요.
사용자 : 시리야
Siri   : 네, 부르셨어요?
사용자 : 꺼져
Siri   : 무슨 말씀인지 못 알아 들었어요.
사용자 : 빅스비!
Siri   : 묵묵부답
'''
