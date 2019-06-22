# 순열
# n개 중 r개를 뽑아 나열 : nPr
def running_team(n, r):
    # To-do
    res = 1
    for i in range(n-r+1, n+1) :
        res *= i
        print(i)


    return res


print(running_team(5, 2))
