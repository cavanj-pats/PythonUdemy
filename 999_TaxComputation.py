#999_TaxComputation.py


#married filing jointly
#income over   $100k

form1040 = dict()



income = int(input('Enter line 15 taxable income: '))

#for married filing jointly.

if income >=100000 and income <=206700:
    tax =  (income * 0.22) - 10172
elif income >206700 and income < 394600:
    tax = (income * 0.24) - 14306
elif income > 394600 and income <= 501050:
    tax = (income * 0.32) - 45874
elif income > 501050 and income <= 751600:
    tax = (income * 0.35) - 60905.50
elif income > 751600:
    tax = (income * 0.37) - 75937.50
else:
    tax = income * .12 #this is not correct


print(f"For income: {income} your tax due is: {tax}")