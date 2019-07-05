import numpy as np
'''
### 난수 발생과 카운팅 ###
파이썬을 이용하여 데이터를 무작위로 섞거나 임의의 수
즉, 난수(random number)를 발생시키는 방법에 대해 알아본다.
이 기능은 주로 NumPy의 random 서브패키지에서 제공한다.
'''
# random value
np.random.seed(0)
print(np.random.rand(5))
print(np.random.rand(10))
print(np.random.rand(13))

'''
### 데이터 순서 바꾸기 ###
데이터의 순서를 바꾸려면 shuffle 명령을 사용한다.
'''
x = np.arange(10)
print(x)
np.random.shuffle(x)
print(x)
# np.random.shuffle()은 return값이 없다.
# 파라미터가 변한다.
y = np.arange(20)
np.random.shuffle(y)
print(y)


'''
### 데이터 샘플링
이미 있는 데이터 집합에서 일부를 무작위로 선택하는 것을 샘플링(sampling)이라고 한다.
샘플링에는 choice 명령을 사용한다. choice 명령은 다음과 같은 인수를 가질 수 있다.
numpy.random.choice(a, size=None, replace=True, p=None)
 - a : 배열이면 원래의 데이터, 정수이면 arange(a) 명령으로 데이터 생성
 - size : 정수. 샘플 숫자
 - replace : 불리언. True이면 한번 선택한 데이터를 다시 선택 가능
 - p : 배열. 각 데이터가 선택될 수 있는 확률
'''
print(np.random.choice(np.arange(10), size = 8, replace = True, p = None))
print(np.random.choice(np.array([10,40,23,14,16]), size = 3, replace = False, p = [0.1, 0.5, 0.1, 0.1, 0.2]))
print(np.random.choice(np.arange(10,100,10), size = 3, replace = True, p = [0.1,0.2,0.1,0.2,0.05,0.05,0.1,0.1,0.1]))

'''
### 난수 생성
NumPy의 random 서브패키지에는 난수를 생성하는 다양한 명령을 제공한다.
그 중 가장 간단하고 많이 사용되는 것은 다음 3가지 명령이다.

* rand: 0부터 1사이의 균일 분포
* randn: 가우시안 표준 정규 분포 (기댓값이 0, 표준편차 1)
* randint: 균일 분포의 정수 난수
rand 명령은 0부터 1사이에서 균일한 확률 분포로 실수 난수를 생성한다.
숫자 인수는 생성할 난수의 크기이다.
여러개의 인수를 넣으면 해당 크기를 가진 행렬을 생성한다.
'''
print(np.random.randn(3))
print(np.random.rand(2,3,4))
print(np.random.randint(3,30, size = (2,3,2)))
print(np.random.randint(1,10, 10))
print(np.random.rand(2,2))
print(np.random.randn(1,3))

'''
### 정수 데이터 카운팅 ###
이렇게 발생시킨 난수가 실수값이면 히스토그램 등을 사용하여 분석하면 된다.

만약 난수가 정수값이면 unique 명령이나 bincount 명령으로 데이터 값을 분석할 수 있다.
이 명령들은 random 서브패키지가 아니라 NumPy 바로 아래에 포함된 명령이다.

unique 명령은 데이터에서 중복된 값을 제거하고 중복되지 않는 값의 리스트를 출력한다.
return_counts 인수를 True 로 설정하면 각 값을 가진 데이터 갯수도 출력한다.
'''
rand = np.random.randint(1,10,20)
a = np.unique(rand) # np.unique 함수는 sort도 된다.
print(rand)
print(a) # 중복값이 제거
u, c = np.unique([1,1,2,2,2,5], return_counts = True)
print(u) # [1, 2, 5] 중복값이 제거됨
print(c) # [2, 3, 1] 1의개수, 2의개수, 5의개수
'''
np.bincount는 인덱스 숫자에 해당하는 값의 개수
아래 배열은 숫자가 0, 1, 2, 10 네 가지가 있고
0은 1개, 1은 3개, 2는 3개, 10은 1개가 있다.
따라서 리턴값은 크기가 11인 리스트,
리스트의 [0] = 1, [1] = 3, [2] = 3, [10] = 1
'''
print(np.bincount([0,1,1,2,2,1,2,10])) # [1 3 3 0 0 0 0 0 0 0 1]
