#enumerate 실습
import collections

#iterable types
var_list = [10, 20, 30]
print('list:', isinstance(var_list, collections.Iterable)) #True

var_dict = {'math' : 98, 'english':90, 'art': 70}
print('dict:', isinstance(var_dict, collections.Iterable)) #True

var_range = range(0,6)
print('range:', isinstance(var_range, collections.Iterable)) #True

'''
집합(set)
집합은 여러 개의 자료를 하나의 변수로 관리할 때 사용하는 자료형 중의 하나입니다.

집합 자료형은 수학의 집합과 같은 성질을 가집니다.
즉, 집합은 중복된 데이터를 가질 수 없고, 순서가 없습니다.
따라서 순서와 관련된 인덱스기호([ ])를 사용할 수 없고,
중복 데이터를 만드는 +, *를 사용할 수 없습니다.
하지만, in, not in, len()은 사용할 수 있습니다.
'''
var_set = {1, 3}
print('set:', isinstance(var_set, collections.Iterable)) #True

var_str = 'helloworld'
print('string:', isinstance(var_str, collections.Iterable)) #True

'''
bytes는 1바이트 단위의 값을 연속적으로 저장하는 시퀀스 자료형
bytes로 바이트 객체를 만드는 방법 3가지
 - bytes(길이): 정해진 길이만큼 0으로 채워진 바이트 객체를 생성
 - bytes(반복가능한객체): 반복 가능한 객체로 바이트 객체를 생성
 - bytes(바이트객체): 바이트 객체로 바이트 객체를 생성
'''
var_bytes = b'helloworld'
print('bytes:', isinstance(var_bytes, collections.Iterable)) #True

var_tuple = (1,3,5,7)
print('tuple:', isinstance(var_tuple, collections.Iterable)) #True

# step = 3
# range(start, end, step)
step3_list = list(range(0,30,3))
for l in step3_list:
    print(l)

step5_list = list(range(0,30,5))
for l in step5_list:
    print(l)

step6_list = list(range(0,30,6))
for l in step6_list:
    print(l)

step2_list = list(range(0,30,2))
for l in step2_list:
    print(l)


'''
enumerate
반복문 사용 시 몇 번째 반복문인지 확인이 필요할 수 있습니다. 이때 사용합니다.
인덱스 번호와 컬렉션의 원소를 tuple형태로 반환합니다.
'''
print('tuple')
for v in enumerate(var_str):
    print(v)

print('index and value')
for i,v in enumerate(var_str):
    print(i+1,'번째 글자:', v)

for idx, val in enumerate(var_set):
    print(idx+1,':',val)

for i, v in enumerate(var_range):
    print(i+1,'번째:',v)


e = ["유진", "민철", "가영", "민희", "영진", "미희", "진수", "영철", "민지", "영호", "호준", "지혜", "철수"]

e_with_rank=[str(i+1)+'등 : '+name for i,name in enumerate(e)]
print(e_with_rank)
