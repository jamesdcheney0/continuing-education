while True:
    line = input(r'> ')
    if line[0] == '#': # this matches the first character of the string passed into it - remember, strings can be considered to be a list of characters 
        continue
    if line == 'done':
        break
    print(line)
print('Done!')
