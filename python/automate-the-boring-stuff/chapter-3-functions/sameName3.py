def spam():
    global eggs
    eggs = 'spam' # this is affecting the global variable
    return print('hello world!')

def bacon():
    eggs = 'bacon' # this is a local variable

def ham():
    print(eggs) # this is using the global variable

eggs = 42 # setting the global variable
spam()
print(eggs)