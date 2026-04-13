def treg(a, b ,c):
    if (a + b > c) and (a + c > b) and (b + c > a):
        return 'treg'
    
print(treg(8 , 5, 4))