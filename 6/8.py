def skidka(a):
    if a < 1000:
        return'5%'
    elif a<5000:
        return '10%'
    elif a>=5000:
        return'15%'
print(skidka(6000))