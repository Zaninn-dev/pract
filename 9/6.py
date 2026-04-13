list1 = [1,5,9,11,12,2,3,4,6]
list2 = [2,3,4,7,9,10,12,15]

ZET = sorted(list(set(list1) & set(list2)))

print(ZET)
