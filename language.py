from datetime import date
import os
import operator
import datetime

# Available language, data and base directory
languages = ["NL", "EN", "FR", "DE", "IT", "SWE", "RU"]
data = []
base = os.path.dirname(os.path.abspath(__file__)) + "/data"

# Characters
characters = [chr(i) for i in range(91, 126)]  # Latin Alphabet
characters.extend([chr(i) for i in range(33, 64)])  # Numbers
characters.extend([chr(i) for i in range(223, 255)])  # Special characters
characters.extend([chr(i) for i in range(161, 171)])  # Currency
characters.extend(["а", "б", "в", "г", "д", "е", "ё", "ж", "з", 
                    "и", "й", "к", "л", "м", "н", "о", "п", "р",
                    "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ",
                    "ъ", "ы", "ь", "э", "ю", "я"])  # Russian characters

# Import data function
def importData(language):
    folder = os.path.join(base, language)
    files = os.listdir(folder)
    files = [os.path.join(folder, file) for file in files]

    dataset = []
    for path in files:
        file = open(path, 'r', encoding="utf8")
        data = ""
        for line in file.readlines():
            data += line.strip() + " "
        data = data.lower().split(" ")
        data = [value for value in data if data != '']
        dataset.extend(data)

    print("{} contains: {} words".format(language, len(dataset)))
    return dataset

# Importing data
for language in languages:
    data.append(importData(language))

# Make (tri/bi)gram
def setGram(gramSize, characters):
    gram = {}

    for x in characters:
        for y in characters:
            if gramSize:
                for z in characters:
                    gram[x + y + z] = 0
            else:
                gram[x + y] = 0

    return gram

# Train grams
def trainGrams(x, data, gram):
    # Total hits
    hits = 0

    for word in data:
        # Take word and start iteration through letters (use -x to prevent out of bounds)
        for i in range(0, len(word) - x + 1, 1):
            string = ""

            # Add letters to string
            for j in range(0, x):
                string += word[i+j]

            # Check if string is in tri-/bigram
            if string in gram:
                gram[string] += 1
                hits += 1

    # add score to total hits
    for (key, value) in gram.items():
        gram[key] = value/hits

    # Smoothing
    smoothingFactor = 1 / len(gram.items())
    for (key, value) in gram.items():
        if (value == 0):
            gram[key] += smoothingFactor

    sumValue = sum(gram.values())

    for (key, value) in gram.items():
        gram[key] = value/sumValue

    return gram

# Guess language
def predict(grams, gramSize):
    sentence = input("\nFill in your sentence: ")
    sentence = sentence.lower().split()

    predictions = {}

    for i in languages:
        predictions[i] = 1

    # Calculate predictions
    for word in sentence:
        for i in range(0, len(word) - gramSize + 1, 1):
            gramString = ""
            for j in range(0, gramSize):
                gramString += word[i+j]

            for index, gram in enumerate(grams):
                predictions[languages[index]] *= gram[gramString]

    # Total of values n
    total = sum(predictions.values())

    # Output
    for key, value in predictions.items():
        print("{} has a chance of {}".format(key, value/total))

    print("\nThe predicted language is:", max(predictions.items(), key=operator.itemgetter(1))[
          0], "\n- Certainty:", predictions[max(predictions.items(), key=operator.itemgetter(1))[0]] / total)

    input("\nPress any key to try again!")
    predict(grams, gramSize)

# Start program
def setup():
    # selection
    tri = input("\nWould you like to use tri- or bigrams? (Fill in tri or bi): ")
    grams = []
    startTime = datetime.datetime.now()
    # Trigram
    if (tri == "tri"):
        print("\nSetting up grams...")

        # Make trigrams
        trigrams = [setGram(True, characters) for x in languages]
        print("Finished setting up grams!")

        # Train grams
        print("\nStarting training...")
        for index, trigram in enumerate(trigrams):
            grams.append(trainGrams(3, data[index], trigram))

        print("Done training!")

    # Bigram
    if (tri == "bi"):
        print("\nSetting up grams...")

        # Make bigrams
        bigrams = [setGram(False, characters) for x in languages]
        print("Finished setting up grams!")

        # Train grams
        print("\nStarting training...")
        for index, bigrams in enumerate(bigrams):
            grams.append(trainGrams(2, data[index], bigrams))

        print("Done training!")

    # Restart
    if (tri != "tri" and tri != "bi"):
        print("Invalid awnser!")
        setup()
        
    # Calculating time used
    endTime = datetime.datetime.now()
    timeSpend = endTime-startTime
    print("Elapsed time for making and training the grams: {}.{}".format(timeSpend.seconds,timeSpend.microseconds))

    # User input
    predict(grams, 3 if tri == "tri" else 2)

setup()
