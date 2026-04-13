from random import randint

with open('data.txt', 'w') as file:
    for _ in range(5):
        file.write(str(randint(1, 1000)) + '\n') 

with open('data.txt', 'r') as file:
    num = []
    for i in file.readlines():
        num.append(int(i.strip('\n')))
    print(sum(num))
