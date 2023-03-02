countList = [9, 41, 12, 3, 74, 15]

# determine largest number in a loop
largestSoFar = -1
print('Before:', largestSoFar)
for num in countList:
    if num > largestSoFar: 
        largestSoFar = num
    print("Loop:", num, largestSoFar)
print('Largest:', largestSoFar)

# determine smallest number in a list - version one
smallestSoFar = -1 # -1 is smaller than all positive integers, and putting in an arbitrary large number would cut off the range from being higher than that 
print("Before [1]:", smallestSoFar)
for num in countList:
    if smallestSoFar < smallestSoFar:
        smallestSoFar = num
    print("Loop:", num, smallestSoFar)
print("Smallest:", smallestSoFar)

# determine smallest number in a list - version two
# also a way to find greatest number 
smallest = None
print('Before [2]:', smallest)
for value in countList:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    print(smallest, value)
print('After:',smallest)

# determine smallest number in a list - version three
smallest = None
print("Before [3]:", smallest)
for num in countList:
    if smallest is None or num < smallest:
        smallest = num
    print("Loop:", num, smallest)
print("Smallest:", smallest)



# sum numbers in a loop
sum = 0
print('Before:', sum)
for num in countList:
    sum = num + sum
    print(sum, num)
print('After: ', sum)

# find the average with `sum/count`
count = 0
sum = 0
print('Before:', count, sum)
for value in countList:
    count = count + 1
    sum = value + sum
    print(count, sum, value)
print('After: ', count, sum, sum/count)

# filtering in a loop
print('Before')
for value in countList:
    if value > 20: 
        print('Large number:', value)
print('After')

# search using boolean variable
found = False
print('Before:', found)
for value in countList:
    if value == 3:
        found = True
    print(found, value)
print('After:',found)
