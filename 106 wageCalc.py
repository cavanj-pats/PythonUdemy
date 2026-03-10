#wageCalc.py
#calculate wages 
#

userHours = input('Enter daily hours separated by space: ')
userWage = input('Enter hourly wage: ')



userWage = float(userWage)

L1 = userHours.split()
sumHours =0

for hours in L1:
    sumHours += int(hours)

if sumHours <= 40:
    total = sumHours * userWage    
else:
    total = 40 * userWage + ((sumHours - 40) * userWage * 1.5)

print(f"Total Hours worked: {sumHours}")
print(f"Total Pay: {total}")


