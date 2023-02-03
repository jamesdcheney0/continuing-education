import pprint

message = 'a quick brown fox jumped over the lazy dog A QUICK BROWN FOX JUMPED OVER THE LAZY DOG'
count={}

for character in message:
    count.setdefault(character,0)
    count[character] = count[character] + 1

pprint.pprint(count) # prints the dictionary in a column instead of rows 
print(pprint.pformat(count)) # prints a string of the dictionary