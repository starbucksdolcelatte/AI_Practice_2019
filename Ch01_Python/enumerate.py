#enumerate 실습
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
