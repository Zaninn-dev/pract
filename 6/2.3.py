def poli(text: str):
    txt = text.lower().strip()
    return txt == txt[::-1]
print(poli(' lol'))