'''
길이가 같은 두 리스트가 주어졌을 때 다음과 같은 연산을 하는 함수를 작성해 봅시다.

numpy 행벡터로 변환
식 5(a+b)5(a+b) 계산
'''

import numpy as np

def vec_calc(a, b):
    # To-do
    return 5 * (np.array(a) + np.array(b))


    
print(vec_calc([1, 2, 3], [4, 5, 6]))
