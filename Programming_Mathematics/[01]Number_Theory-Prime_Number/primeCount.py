def primeCount(n):
    # To-do
    n += 1
    l = [True for _ in range(n)]
    l[0] = False
    l[1] = False
    for i in range(2, n):
        if (l[i] == True):
            j = 2
            while (i*j < n):
                l[i*j] = False
                j += 1
    return sum(l)
    pass


print(primeCount(10))
