#4
# 


header = ['name', 'age', 'city']
data = [ ['James', 25, 'NY'], ['Kiran', 25, 'DEL'], ['Smith', 24, 'PAR'], ['Raj', 27, 'DEL'] ]
          

# should result in three dictionaries due to header having three data elements
# a dictionary of NAMES, AGES, and CITIES

result = []
length = len(header)

for i in range(length):
    newDict = {}   # this is a new dictionary for the dataset
    for row in data:
        if row[i] not in newDict:
            newDict[row[i]] = [row]
        else:
            newDict[row[i]].append(row)

    result.append(newDict)

print("Dictionaries:")
for i in range(length):
    print('\n' + header[i])
    for key, value in result[i].items():
        print(f"{key:<10}:{value}")








