

# number of months that start with Monday.

from datetime import date

#abdul used a function and special comparison
def age(dob):
    today = date.today()
    years = today.year - dob.year
    if (today.month, today.day) < (dob.month, dob.day):
        years -= 1

    return years



myDate = input('Enter a birthday d/m/y: ')
d, m, y = myDate.split('/')
 
birthDate = date(int(y), int(m), int(d))

#tday = datetime.datetime.today()
#age = tday - birthDate
print(f"Age: {age(birthDate)} years.")


           