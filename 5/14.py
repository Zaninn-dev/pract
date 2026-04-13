number='10'
spisok=[1,2,3,4,5,3]
if int(number) in spisok:
    print(f'vi est v spiske vash nomer {number} vhosdenie {spisok.index(int(number))}')
else:
    print('vas net')