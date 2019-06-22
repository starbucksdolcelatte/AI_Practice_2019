'''
행렬곱 연산
두 numpy 배열 A, B가 주어졌을때 다음의 계산을 하는 함수를 작성해 봅시다.
5(A × B)
'''
import numpy as np

def mat_calc(A, B):
    # To-do
    return 5 * np.dot(A, B)


print(mat_calc(np.array([[1, 2, 3], [4, 5, 6]]), np.array([[1, 2], [3, 4], [5, 6]])))
