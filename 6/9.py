def soverch(a):
    k=0
    for i in range(1,a):
        if a % i ==0:
            k+=i
    if k ==a:
        return 'soverch'
print(soverch(28))