#challenge_dateTime_countMondayMonths.py

# number of months that start with Monday.

from datetime import date
import calendar

yr = int(input('Enter a four digit year: '))
count = 0
for i in range(1,13):
    if date(yr, i, 1).weekday() == 0:
        count +=1
        print ('Month: ', calendar.month_name[i])

print('Total count of Months: ', count)
           