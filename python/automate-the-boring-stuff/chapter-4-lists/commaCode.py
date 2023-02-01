# write a function that takes a list value as an argument and returns a string with all the items separated by a command and a space with and inserted before the last item 
# e.g. `spam = ['apples','bananas','tofu','cats']` should evaluate to 'apples, bananas, tofu, and cats'

# grabbed a list input example from here https://pynative.com/python-accept-list-input-from-user/
# by default, python converts input() into a string, then the list is made from that string, and each element of that string.

def lister():
    newList = input('type a string with no spaces to populate a list ')
    print(newList)
    newString = newList[0]
    for item in newList[1:-1]:
        newString = newString + ', ' + item 
    print(newString + ', and ' + newList[-1])

# tried example from 'Input a list using a list comprehension' and newString had type int, and item had type string
def lister2():
    n = int(input("Enter the size of the list "))
    newList = list(int(num) for num in input("Enter the list items separated by space ").strip().split())[:n]
    print(newList)
    newString = newList[0]
    for item in newList[1:-1]:
        print(type(newString))
        print(type(item))
        # newString = newString + ', ' + item 
    print(newString + ', and ' + newList[-1])

# tried example from 'Get a list of strings as an input from a user' and got this. Slightly cleaner than lister()
def lister3():
    newList = input('type in values separated by a space to populate a list: ')
    newList = newList.split(" ")
    newString = newList[0]
    for item in newList[1:-1]:
        newString = newString + ', ' + item 
    print(newString + ', and ' + newList[-1])

lister3()