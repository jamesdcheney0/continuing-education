# Copied code from ./ex-3.1.py
# Now we want to add some error handling 
import locale

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

try: 
    hours = float(input('Enter hours: '))
    rate = float(input('Enter rate:  '))
except: 
    print('Value must be an integer. Goodbye!')
    quit()

if hours > 40: 
    regPay = 40 * rate
    otPay = (hours - 40) * (rate * 1.5)
    totalPay = regPay + otPay
    print("Regular Pay:  ","$"+str(locale.format_string('%.2f',regPay, True)))
    print("Overtime Pay: ","$"+str(locale.format_string('%.2f',otPay, True)))
    print("Total Pay:    ","$"+str(locale.format_string('%.2f',totalPay, True)))
    # locale.format_string formats numbers with 2 following floating point digits and adds a comma, which is what the f"{}" thing did in the previous ones
    # I'd be interested to figure out how to google how to get the returns to line up nicely without just adding spaces to the string. It works, but I feel like there's a better way to do that 
    # there's also a thing called babel that prints out fancy numbers. It was too complicated for me to want to get into https://babel.pocoo.org/en/latest/api/numbers.html#babel.numbers.format_currency
else: 
    pay = hours * rate
    print("Regular Pay:","$"+str(locale.format_string('%.2f',pay, True))) #adds commas to numbers with four digits or more 

# locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
# print(locale.format_string('%.2f',totalPay, True))