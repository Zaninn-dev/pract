def asd(a):
    k=0
    if a <= 10**9:
        while a != 0:
            s = a%10
            a= a //10
            k += s
        return(k)
    else:
        print(1)
print(asd(15223))