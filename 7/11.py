with open('count.txt', 'r') as file:
    content = file.read()
    words = content.split()
    print(len(words))