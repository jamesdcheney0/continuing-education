def spam():
    global eggs #calls the global var, instead of defining a local var
    eggs = 'spam' #affects the global variable

eggs = 'global'
spam()
print(eggs)