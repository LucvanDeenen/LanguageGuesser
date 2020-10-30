import math
import os

# Beschikbare talen
languages = ["NL", "EN", "FR", "DE", "ES", "RU"]


# def importData():

characters = [chr(i) for i in range(33, 64)] # Leestekens en cijfers
characters.extend([chr(i) for i in range(91, 126)]) # Latijns alfabet
characters.extend([chr(i) for i in range(161, 171)]) # Valuta's
characters.extend([chr(i) for i in range(223, 255)]) # Speciale characters
characters.extend([chr(i) for i in range(400, 450)]) # Russische characters

def setTrigram(characters):
    trigram = {}

    for x in characters:
        for y in characters:
            for z in characters:
                trigram[x + y + z] = 0

    return trigram

trigrams = setTrigram(characters)
print(characters)
print(trigrams)

def trainGrams(data, gram):
    for i in gram:
        gram[i] += 1

