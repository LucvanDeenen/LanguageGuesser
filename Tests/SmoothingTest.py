gram = {'AA' : 0, 'AB' : 0.60, 'BA' : 0, 'BB' : 0}
smoothingFactor = 1 / len(gram.items())

print(gram, smoothingFactor)

for (key, value) in gram.items():
    if(value == 0):
        gram[key] += smoothingFactor

print(gram, sum(gram.values()))
