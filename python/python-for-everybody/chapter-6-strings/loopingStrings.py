fruit = 'banana'
# indefinite loop not preferred 
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index = index + 1

# definite loops are more elegant and the preferred option
for letter in fruit: #python doesn't know what `letter` means aside from a random value that receives the values of `fruit`. While loops capture index values, for loops seem to grab the values at the indexes 
    print(letter)
    # if index number isn't needed, then this is great; can just as easily get an iteration variable from a for loop 
    # the less code written, the fewer opportunities to make a mistake 


