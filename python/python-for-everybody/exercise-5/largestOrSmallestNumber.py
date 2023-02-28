largestSoFar = -1
print('Before:', largestSoFar)
for num in [3, 41, 12, 9, 74, 15]:
    if num > largestSoFar: 
        largestSoFar = num
    print("Loop:", num, largestSoFar)
print('Largest:', largestSoFar)

smallest = None
print("Before:", smallest)
for num in [3, 41, 12, 9, 74, 15]:
    if smallest is None or num < smallest:
        smallest = num
    print("Loop:", num, smallest)
print("Smallest:", smallest)