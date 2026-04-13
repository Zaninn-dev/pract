def pred(min, max, a):
    if a in range(min, max):
        return "pred"
    else:
        return "ne pred"
    
print(pred(-5, 5, 10))