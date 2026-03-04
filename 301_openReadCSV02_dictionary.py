#openReadCSV01_dictionary.py

#challenge make each row a dictionary
#with the key being the name
#name : {empID: e, }

import csv
import pprint   #pretty print
#invoke using pprint.pprint(dictionary or whatever you want to print)

f = open('EmplSalaries.csv', 'r')
rdr = csv.DictReader(f)

row_dict = {}

for row in rdr:
    nameKey = row['Name']
    row_dict[nameKey]=row

    
print(row_dict)

f.close()



