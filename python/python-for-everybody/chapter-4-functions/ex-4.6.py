# Copied code from ./ex-3.2.py
# now to define a function for `computepay` - not necessary for a program this small, 
# but might as well! Also, simplified the statements down to just a single pay statement 
import locale

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')


def computepay(hours, rate):
    try: 
        fHours = float(hours)
        fRate = float(rate)
    except: 
        print('Value must be an integer. Goodbye!')
        quit()

    if fHours > 40: 
        regPay = 40 * fRate
        otPay = (fHours - 40) * (fRate * 1.5)
        pay = regPay + otPay
    else: 
        pay = fHours * fRate
    return pay # when the function is assigned a variable, then the function provides the constant of the defined variable w/n the function, and the variable can be used outside of the function 


hours = input('Enter hours: ')
rate = input('Enter rate:  ')
pay = computepay(hours, rate)
print("Pay:", "$"+str(locale.format_string('%.2f',pay, True)))
