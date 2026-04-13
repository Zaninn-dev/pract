def phib(n):
    k,m = 0,1
    for _ in range(n):
        print(k)
        k,m = m , k+m
phib(10)