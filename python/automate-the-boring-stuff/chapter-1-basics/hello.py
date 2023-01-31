# This program says hello and asks for my name. 

print('Hello world!')
print('What is your name?') # ask for user's name


myName = input()
print('It is good to meet you, ' + myName)
lenMyName = (len(myName))
print('The length of your name is: ' + str(lenMyName))
print('What is your age?') # ask for user's age
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')
