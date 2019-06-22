'''
파이썬의 기본 라이브러리 중에는 순열의 가능한 경우를 모두 구할 수 있는 기능이 존재합니다.
itertools.permutations을 이용하면 주어진 리스트의 순열을 구할 수 있습니다.

>>> import itertools
>>> a = ['A', 'B', 'C']
>>> print(list(itertools.permutations(a)))
[('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'),
('C', 'A', 'B'), ('C', 'B', 'A')]
>>> print(list(itertools.permutations(a, 2)))
[('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]

permutations을 사용해서 nPr의 값을 구하는 함수를 작성해 봅시다.
'''

import itertools

def p(n, r):
    # To-do
    a = [i for i in range(n)]
    return len(list(itertools.permutations(a,r)))


    
print(p(5, 2))
