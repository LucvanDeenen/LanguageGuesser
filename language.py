import math
import os

# Beschikbare talen
languages = ["NL", "EN", "FR", "DE", "ES", "RU"]

def importData(language):
    path = ""

    base = os.path.dirname(os.path.abspath(__file__)) + "/data"
    folder = os.path.join(base, language)
    files = [os.path.join(path, file) for file in os.listdir(folder)]

    dataset = []
    for path in files:
        file = open(path, 'r', encoding="utf8")
        
    print(files)

def setTrigram(characters):
    trigram = {}

    for x in characters:
        for y in characters:
            for z in characters:
                trigram[x + y + z] = 0

    return trigram

def trainGrams(data, gram):
    for i in gram:
        gram[i] += 1


characters = [chr(i) for i in range(33, 64)] # Leestekens en cijfers
characters.extend([chr(i) for i in range(91, 126)]) # Latijns alfabet
characters.extend([chr(i) for i in range(161, 171)]) # Valuta's
characters.extend([chr(i) for i in range(223, 255)]) # Speciale characters
characters.extend([chr(i) for i in range(400, 450)]) # Russische characters

trigrams = setTrigram(characters)
print(characters)

