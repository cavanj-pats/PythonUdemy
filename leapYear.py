#leap year

year = int(input('Enter a year:'))

if year % 100 == 0:
    if year % 400 == 0:
        print ('Is Leap Year')
    else:
        print('Not a leap year')
elif year % 4 == 0:
    print('Is Leap Year')
else:
    print('Not a leap year')
