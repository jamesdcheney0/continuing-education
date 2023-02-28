# Copied code from ../exercise-2/ex-2.3.pay
# Now we want to account for overtime
hours = float(input('Enter hours: '))
rate = float(input('Enter rate: '))
if hours > 40: 
    regPay = 40 * rate
    otPay = (hours - 40) * (rate * 1.5)
    totalPay = regPay + otPay
    print("Regular Pay:",f"{regPay:,}")
    print("Overtime Pay:",f"{otPay:,}")
    print("Total Pay: ", f"{totalPay:,}")
else: 
    pay = hours * rate
    print("Regular Pay:",f"{pay:,}") #adds commas to numbers with four digits or more 

