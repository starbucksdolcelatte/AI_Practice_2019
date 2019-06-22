'''
대칭행렬은 행렬 A와 그 전치행렬인 AT 가 동일한 행렬을 말합니다.
주어진 행렬이 대칭행렬인지 확인하는 함수를 작성해 봅시다.

A의 전치행렬 = np.transpose(A)
두 numpy 행렬 A와 B의 모든 원소가 같은지 확인 : np.allclose(A, B)
'''

import numpy as np

def is_symmetric(A):
    # To-do
    if (np.allclose(A, np.transpose(A))):
        return True
    else:
        return False


    
print(is_symmetric(np.array([[1, 2], [2, 3]])))
