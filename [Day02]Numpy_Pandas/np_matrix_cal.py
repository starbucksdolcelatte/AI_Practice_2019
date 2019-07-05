import numpy as np

array1 = np.array([[1,2,3], [4,5,6], [7,8,9]])

# array1을 전치한 배열을 구해봅시다.
transposed = np.transpose(array1)
print(transposed, '는 array1을 전치한 행렬입니다.')
# array1과 array1의 전치 행렬의 행렬곱을 구해봅시다
power = np.dot(array1, np.transpose(array1))
print(power,'는 array1과 array1의 전치 행렬을 행렬곱한 것입니다.')

# array1과 array1의 전치 행렬의 요소별 곱을 구해봅시다.
elementwise_prod = array1 * np.transpose(array1)
print(elementwise_prod, '는 array1과 array1의 전치행렬을 요소별로 곱한 행렬입니다.')

array2 = np.array([[2,3],[1,7]])

# array2의 역행렬을 만들어 봅시다.
inverse_array2 = np.linalg.inv(array2)
print(inverse_array2,'는 array2의 역행렬입니다.')

# array2의 대각 성분을 추출해 봅시다.
diagonal = np.diag(array2)
print(diagonal,'는 array2의 대각 성분입니다.')

# array2와 array2의 역행렬을 곱한 행렬을 만들어 봅시다.
producted = array2 * np.transpose(array2)
print(producted,'는 array2와 array2의 역행렬을 곱한 행렬입니다.')
