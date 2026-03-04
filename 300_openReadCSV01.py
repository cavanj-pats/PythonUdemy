#openReadCSV01.py

# i wouild think abdul has a much more graceful way to find min and max salary person.
# my technique,  move back to start of file, re-establish the reader, 
# move next.  THen iterate through.  when row matches min or max, pluck out the name.

import csv

f = open('EmplSalaries.csv', 'r')
csv_reader = csv.reader(f)

next(csv_reader)   #bypass the header row so we can calculate salaries

salaries=[]
for row in csv_reader:
    salaries.append(int(row[2]))
    #print(int(row[2]))

print(salaries)
print('Min', min(salaries))
print('Max', max(salaries))

#whose salaries are min and whose are max is a challenge

minrow = salaries.index(min(salaries))
maxrow = salaries.index(max(salaries))

#name of person with min salary
f.seek(0)     #move back to start of file
csv_reader = csv.reader(f)   #reset the reader to the start of the file
next(csv_reader)  #move off the header row
idx = 0   #0 based because we reference the list of salaries 
trigger = 0
for row in csv_reader:
    if idx == minrow:
        print('Name of Min Salary Person', row[1])
        trigger += 1
    elif idx == maxrow:
        print('Name of Max Salary Person', row[1])
        trigger += 1

    idx +=1  #add one to index
    if trigger == 2:   #found both min and max no need to keep iterating
        break


    f.close()
    