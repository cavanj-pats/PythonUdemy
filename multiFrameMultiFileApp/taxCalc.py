#taxApp.py

bracketMax = 99999999   #address this somehow in the calc. if income is greater than this....

#calculate taxes based on filing status and expected income
def calculate_tax(grossIncome, standardDeduction, brackets):
    #CALC the Adjusted gross income using filing status to determine standard deduction
    taxable_income = max(0, grossIncome - standardDeduction)

    total_tax = 0.0
    previous_threshold = 0

    for threshold, rate in brackets:
        if taxable_income > threshold:
            taxable_in_bracket = threshold - previous_threshold

            total_tax += taxable_in_bracket * rate
            previous_threshold = threshold
        else:
            #need to calculate the last brackets tax
            taxable_in_bracket = taxable_income - (previous_threshold + 1)
            total_tax += taxable_in_bracket * rate
            break

    return taxable_income, total_tax







if __name__ == "__main__":
    #get the user filing status
    #get the users anticipated income
    gross_income = float(input("Enter gross income: "))

    #develop for mfj for now
    standard_deduction = 32200

    #each bracket - upper limit, tax rate
    mfj_brackets = [
        (24800, 0.10),
        (100800, 0.12),
        (211400, 0.22),
        (403550, 0.24),
        (512450, 0.32),
        (768700, 0.35),
        (bracketMax,0.37)
    ]

    taxable, total = calculate_tax(gross_income,standard_deduction, mfj_brackets)

    print(f"Taxable Income: {taxable}, total tax due: {total}")
    print(f"Effective Tax Rate tax / gross: {total / gross_income * 100:.2f} %")

    