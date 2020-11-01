languages = ['NL', 'EN']
predictions = {'NL': 1, 'EN': 1}
grams = {"NL" : {'HEL': 0.1, 'HOI': 0.9, 'BEN': 0.9}} 
grams["NL"] = 

for index, gram in enumerate(grams):
    print('gram: ',gram)
    print(gram.items())
    print()

word = input("Fill in a word: ")

for i in range(0, len(word) - 3 + 1):
    string = ""
    for j in range(0, 3):
        string += word[i+j]
    
    for index, gram in enumerate(grams):
        predictions[languages[index]] *= gram[string]

print(predictions)
