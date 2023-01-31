print('What is your name?')
name = input()
print('How old are you?')
age = int(input())

if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')
elif age > 100:
    print('You are not Alice, grannie') ## The order of clauses matter! The first one that evaulates 'True' will run its clause
elif age > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire.')