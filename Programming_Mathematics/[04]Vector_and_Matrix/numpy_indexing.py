'''numpy는 강력한 인덱싱 기능을 제공합니다.
a[1:3,2:5]라고 실행하면 행렬 a의 1, 2행과 2, 3, 4열에 해당하는
2x3 크기의 부분 행렬을 얻을 수 있습니다.
여기에 할당 연산자 =로 2x3의 행렬을 대입하는 것도 가능합니다.

짝수 자연수 m, n이 주어졌을때 다음의 형태를 띠는 numpy 행렬을 만들어 봅시다.
numpy의 인덱스 기능을 이용하면 더 쉽게 해결할 수 있습니다.

"중앙을 원점으로 각 사분면의 번호를 값으로 가지는 mxn 크기의 xy 평면 행렬"

[입력]
m: 좌표 평면의 행 수
n: 조표 평면의 열 수

[출력]
문제의 조건을 만족하는 numpy 행렬
'''

import numpy as np

def mat_coord(m, n):
    # To-do
    half_row = m//2
    half_col = n//2

    res = np.zeros((m,n))
    res[0:half_row, 0:half_col] = 2
    res[0:half_row, half_col:n] = 1
    res[half_row:m, 0:half_col] = 3
    res[half_row:m, half_col:n] = 4

    return res



print(mat_coord(2, 2))
