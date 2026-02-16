#challenge_dateTime_countSundaysInYear.py

# number of months that start with Monday.

from datetime import date, timedelta
import calendar

yr = int(input('Enter a four digit year: '))
count = 0
dow_FirstDay = date(yr, 1, 1).weekday()
#in a 0-6 list of weekday Sunday is 6
#determine days until Sunday

dus = 6 - dow_FirstDay 

dateFirstSunday = date(yr, 1, 1 + dus)  #this must be a sunday
count = 1 
ddate = dateFirstSunday + timedelta(days=7)
while ddate.year == yr:
    if ddate.weekday() == 6:
        count +=1
    
    #to prevent infinite loop if somehow if is false
    ddate += timedelta(days = 7)
      

print('Total count of Sundays: ', count)
           