#openCSVWriteList.py

#make a list of apple trees

import csv
trees = [('Variety', 'NumTrees', 'NumBearing', 'YearPlanted'),
         ('Honeycrisp', 3, 3, 2016),('Macoun', 1, 1, 2016),('Liberty', 2, 2, 2017),
         ('SnappyMac', 1, 0, 2023), ('Johnagold', 2, 0, 2023), ('Gala', 1, 1, 2016),
         ('Grand Gala', 1, 1, 2016),('Rome', 1, 1, 2016), ('Empire', 2, 1, 2021), ('Fuji', 1, 1, 2016)]

f = open('appleTrees.csv', 'w', newline='')  #will expect \n if we don't do this.  then it will put a new lline that is blank
wrtr = csv.writer(f)

for t in trees:
    wrtr.writerow(t)


f.close()

###################  FOr writing dictionary data to csv file  ##########

f = open('CSVDict.csv','w', newline='')
#wrtr = csv.writer(f)   # just use standard writer to see what it does
fields = ['Variety', 'qty', 'qty bearing', 'year planted']
wrtr = csv.DictWriter(f, fields)
wrtr.writeheader()  #already provided fields

for d in treesdata:
    wrtr.writerow(d)   #it just took keys.  it did not take values



f.close()