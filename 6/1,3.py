def glasn(text):
    gl = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
    count = 0
    for i in text:
        if i in gl:
            count += 1
    return count
print(glasn('жопа'))