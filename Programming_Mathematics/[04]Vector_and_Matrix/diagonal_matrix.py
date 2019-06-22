'''
어떤 수 n이 주어졌을 때 1, 2, 3, …, n을 대각성분으로 가지는 대각행렬을 만드는 함수를 작성해 봅시다.
>>> n_diag(3)
array([[1 0 0]
       [0 2 0]
       [0 0 3]])
'''
import numpy as np

def n_diag(n):
    # To-dp
    res = np.diag(np.arange(n)+1)
    return res


# 결과 출력을 위한 코드입니다. 자유롭게 값을 바꿔보며 확인해보세요.
print(n_diag(10))
