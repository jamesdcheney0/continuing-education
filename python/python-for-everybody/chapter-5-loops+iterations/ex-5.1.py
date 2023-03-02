# enter a series of values, until 'done' is provided, then provide the sum, count, and average
num = 0
tot = 0.0
while True: 
    sval=input('Enter a number: ')
    if sval == 'done':
        break
    try: 
        fval = float(sval)
    except:
        print('Invalid input')
        continue
    print(fval)
    num = num + 1
    tot = tot + fval


# print('ALL DONE')
print('Total:', tot, 'Count:', num, 'Average:', tot/num)