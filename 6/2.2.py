def gradus(a,b):
    if b == 'kel':
        print((a-273)*1.8+32,'fa')
        print(a-273,'ce')
    elif b == 'cel':
        print(a*1.8+32,'fa')
        print(a+273,'kel')
    elif b == 'far':
        print((a-32)/1.8,'cel')
        print((a-32)/1.8+273,'kel')
gradus(100,'cel')