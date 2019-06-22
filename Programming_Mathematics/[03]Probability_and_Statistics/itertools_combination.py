'''
순열과 마찬가지로 조합을 구하는 함수도 존재합니다.
itertools.combinations을 사용하면 주어진 리스트에서 조합을 구할 수 있습니다.
permutation과 달리 뽑는 개수가 반드시 지정되어야 합니다.

>>> import itertools
>>> a = ['A', 'B', 'C']
>>> print(list(itertools.combinations(a, 3)))
[('A', 'B', 'C')]
>>> print(list(itertools.combinations(a, 2)))
[('A', 'B'), ('A', 'C'), ('B', 'C')]
Copy
combinations 함수를 사용하여 nCr의 값을 구하는 함수를 작성해 봅시다.
'''
import itertools

def c(n, r):
    # To-do
    a = [i for i in range(n)]
    return len(list(itertools.combinations(a,r)))



    
print(c(3, 2))
