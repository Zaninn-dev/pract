with open('chisla.txt', 'w') as file:
    while True:
        x = input()
        if x != 'end':
            file.write(str(int(x))+ '\n')
        else:
            break

with open('chisla.txt', 'r') as file:
    num = []
    for i in file.readlines():
        num.append(int(i.strip('\n')))
    print(sum(num)/len(num))