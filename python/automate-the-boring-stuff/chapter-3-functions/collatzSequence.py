# I DID IT! WITHOUT EVEN CHEATING! 

def collatz():
    number = int(input('Type an integer to apply the Collatz Sequence to: '))
    while number != 1: 
        if number % 2 == 0:
            print(number // 2)
            number = number // 2
            continue
        if number % 2 == 1:
            print(3 * number + 1)
            number = 3 * number + 1
            continue


try: 
    collatz()
except ValueError: # I tried the error on TypeError originally, and it didn't catch the error. The book said to try ValueError, and when I did, it correctly printed the except statement
    print('Hey now, follow the instructions') 

# I started out with an if statement, then tried a for, then looked in the book and remembered while