'''
map(f, x): (iterable) x에 f라는 함수를 적용한 값을 map object의 형태로 반환
'''

temp1 = [x for x in range(ord('가'), ord('힣')+1)]
result1 = list(map(chr, temp1)) # chr(x) 는 숫자를 ascii 코드에 따라 문자로 변환
print(result1)

twice = lambda x : x*2
temp2 = [x for x in range(0,20,2)]
result2 = list(map(twice, temp2))
print(temp2)    # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
print(result2)  # [0, 4, 8, 12, 16, 20, 24, 28, 32, 36]

nim = lambda x : str(x)+'님'
temp3 = {'나연':1, '정연':2, '다현':3, '지효':4, '채영':5}
result3 = list(map(nim, temp3.keys()))
print(type(temp3.keys()))   # <class 'dict_keys'>
print(result3)              # ['나연님', '정연님', '다현님', '지효님', '채영님']
