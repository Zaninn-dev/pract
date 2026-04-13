while True:
    x = bool(input())
    if x == True:
        file = open('txt.txt','a')
        file.write(input())
        file.close()
    else:
        file = open('txt.txt','r')
        print(file.read())
        file.close()