#challenge_dateTime_countMondayMonths.py

# number of months that start with Monday.

import datetime




myDate = input('Enter a date d/m/y: ')
d, m, y = myDate.split('/')
 
print(datetime.date(int(y), int(m), int(d)))

           