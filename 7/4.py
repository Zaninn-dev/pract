names = ["Kirk", "Popa", "Epstein", "Kirill"]
filename = "names.txt"

with open(filename, "w") as file:
    for name in names:
        file.write(name + "\n")

with open(filename, "r") as file:
    content = file.read() 
    print(content)
