def maxdel(a,b):
    for i in range(1,a*b):
        if a*b %i ==0:
            k=i
    return k
print(maxdel(5,6))
