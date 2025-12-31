# Program to compute U.S personal income tax (2009 rates)

status = int(input("Enter filing status (0-single, 1-married joint, 2-married separate, 3-head): "))
income = float(input("Enter taxable income: "))

tax = 0

if status == 0:  # Single
    if income <= 8350:
        tax = income * 0.10
    elif income <= 33950:
        tax = 8350 * 0.10 + (income - 8350) * 0.15
    elif income <= 82250:
        tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + (income - 33950) * 0.25
    else:
        tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + (82250 - 33950) * 0.25 + (income - 82250) * 0.28

elif status == 1:  # Married filing jointly
    if income <= 16700:
        tax = income * 0.10
    elif income <= 67900:
        tax = 16700 * 0.10 + (income - 16700) * 0.15
    else:
        tax = 16700 * 0.10 + (67900 - 16700) * 0.15 + (income - 67900) * 0.25

elif status == 2:  # Married filing separately
    if income <= 8350:
        tax = income * 0.10
    elif income <= 33950:
        tax = 8350 * 0.10 + (income - 8350) * 0.15
    else:
        tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + (income - 33950) * 0.25

elif status == 3:  # Head of household
    if income <= 11950:
        tax = income * 0.10
    elif income <= 45500:
        tax = 11950 * 0.10 + (income - 11950) * 0.15
    else:
        tax = 11950 * 0.10 + (45500 - 11950) * 0.15 + (income - 45500) * 0.25

else:
    print("Invalid filing status")

print("Your tax is:", tax)
