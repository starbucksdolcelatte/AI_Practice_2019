# 계차수열
# 계차수열은 수열 an이 있을 때, 매 항마다 더해지는 값들이 수열을 이룰 때,
# 매 항마다 더해지는 수열 bn을 계차수열이라고 부른다.
# 수열 an의 초항이 a, 더해지는 계차수열이 bn일 때 an은 다음과 같다.
# an = a + b1 + b2 + b3 + ... + bn-1

def seqDiff(a, b, n):
    # To-do
    return a + sum(b[:n-1])


print(seqDiff(1, [1, 2, 3, 4, 5], 3))
