def fac(a):
    k=1
    for i in range(1,a+1):
        k*=i
    return k
print(fac(5))