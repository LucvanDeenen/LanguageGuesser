word = input("Fill in a word: ")

print('Making trigram without + 1: ')
for i in range(0, len(word) - 3):
    string= ""
    for j in range(0, 3):
        string += word[i+j]
    print(i, string)

print('\nMaking trigram with + 1: ')
for i in range(0, len(word) - 3 + 1):
    string= ""
    for j in range(0, 3):
        string += word[i+j]
    print(i, string)