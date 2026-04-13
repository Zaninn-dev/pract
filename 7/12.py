max_9 = 0
max_10 = 0
max_11 = 0

with open('results.txt', 'r') as file:
    for line in file.readlines():
        parts = line.split()
        if not parts:
            continue
            
        grade = int(parts[2])
        score = int(parts[3])
        
        if grade == 9:
            if score > max_9:
                max_9 = score
        elif grade == 10:
            if score > max_10:
                max_10 = score
        elif grade == 11:
            if score > max_11:
                max_11 = score

print(max_9, max_10, max_11)
