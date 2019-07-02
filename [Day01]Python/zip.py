'''
zip
zip(*iterable)은 동일한 개수로 이루어진 자료형을 묶어 주는 역할을 하는 함수이다.
'''
print(list(zip([1,2,3],[4,5,6])))

country = ['Korea', 'France', 'US', 'China']
city = ['Seoul', 'Paris', 'DC', 'Beijing']
print(list(zip(country, city)))

e = ["유진", "민철", "가영", "민희", "영진", "미희", "진수", "영철", "민지", "영호", "호준", "지혜", "철수"]
f = ["YJ", "MC", "GY", "MH", "YJ", "MH", "JS", "YC", "MJ", "YH", "HJ", "JH", "CS"]
correspond_e_f = [[x,y] for x,y in zip(e,f)]
print(correspond_e_f)

correspond_c_c = [[x,y] for x,y in zip(country, city)]
print(correspond_c_c)
