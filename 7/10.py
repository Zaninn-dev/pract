with open('text.txt', 'r') as file:
    str_1 = str(file.readline())
    list_1 = str(file.readline()).split(" ")
    str1 = str_1.replace(str(list_1[0]),str(list_1[1]))

with open('info.txt', 'w') as file:
    file.write(str1)
