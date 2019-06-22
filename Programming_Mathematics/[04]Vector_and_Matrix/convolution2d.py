'''
2D 컨볼루션 연산은 이미지 I에 커널 K를 슬라이딩해가며 성분곱 후
원소의 합을 구하는 연산을 말합니다.
numpy를 사용해서 2D 컨볼루션 연산을 직접 구현해봅시다.
패딩은 없으며 스트라이드값은 1이라고 가정합니다.

※ 커널을 뒤집지 않고 계산합니다.

입력
I: 이미지
K: 커널

출력
I와 K의 2D 컨볼루션 결과
'''
import numpy as np

def conv2d(I, K):
    # To-do
    row = len(I) - len(K) + 1
    col = len(I[0]) - len(K[0]) + 1
    res = np.zeros((row, col))


    for i in range(row):
        for j in range(col):
            subI = np.array([[I[i+ii, j+jj] for jj in range(len(K[0]))] for ii in range(len(K))])
            res[i,j] = sum(sum(subI * K))
    return res


# 결과 출력을 위한 코드입니다. 자유롭게 값을 바꿔보며 확인해보세요.
print(conv2d(np.array([[0, 1, 1, 1], [0, 0, 1, 1], [0, 0, 0, 1], [1, 0, 0, 1]]),
            np.array([[1, -1], [1, -1]])))
print(conv2d(np.array([[ 0,  1, -1,  1],
                  [ 1,  0,  1, -1],
                  [ 0, -1,  0,  1],
                  [ 0,  1,  0,  0]]),
        np.array([[1, 1, 1]])))
