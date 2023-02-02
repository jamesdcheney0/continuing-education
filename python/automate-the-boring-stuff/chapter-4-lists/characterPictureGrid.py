# copy the grid and rotate it 90º. Have to print grid[0][0], grid[1][0] etc
# pass end keyword argument to print to not print a newline after each print() call 

grid = [['.','.','.','.','.','.'],
        ['.','0','0','.','.','.'],
        ['0','0','0','0','.','.'],
        ['0','0','0','0','0','.'],
        ['.','0','0','0','0','0'],
        ['0','0','0','0','0','.'],
        ['0','0','0','0','.','.'],
        ['.','0','0','.','.','.'],
        ['.','.','.','.','.','.']]

# prints out a grid with just the top two lines or every character in a column when `print(v)` is removed
# for v in grid: 
    # print(v)
    # for number in v:
    #     print(number)

# how to increase the index number each time. Variable for the index position that gets incremented each time, up to the limit of len(grid)-1


# quantityOfLists = 0
# listContent = 0
# for v in grid[quantityOfLists][listContent]:
#     quantityOfLists = quantityOfLists + 1
#     print(v, end='')
#     if quantityOfLists < len(grid)-1:
#         continue

# prints out `......%`
# for v in grid[len(grid)-1]:
#     print(v, end='')

# print(grid[0][0], end="")
# print(grid[1][0], end="")
# print(grid[2][0], end="")
# print(grid[3][0], end="")
# print(grid[4][0], end="")
# print(grid[5][0], end="")
# print(grid[6][0], end="")
# print(grid[7][0], end="")
# print(grid[8][0])


# print(len(grid[0]))

# looked up examples on the internet of the question. One person recommended two for loops using range 

# for j in range(len(grid[0])):
#     for i in range(len(grid)):
#         print(grid[j][i],end='')
#     print()

# I DON'T KNOW WHAT I'M DOING!
# print(len(grid))
# print(len(grid[0]))
# quantityOfLists=range(len(grid))
# listValues=range(len(grid[0]))
# for n in quantityOfLists:
#     for m in listValues:
#         print(m)
# listed 0, 1, 2, 3, 4, 5 in a column 9 times
    
# stack exchange code review
# codereview.stackexchange.com/questions/222292/character-picture-grid-exercise-automatetheboringstuff
for i in range(len(grid[0])): # `print(len(grid[0]))` returns 6 - the quantity inside each list (assumption is that they're all the same)
    for a in range(len(grid)):# `print(len(grid))` returns 9 - the length of lists - how many lists there are
        if a < len(grid)-1: # if the number of lists is less than the highest index of the list
            print(grid[a][i], end='') # print the first index first (the nested loop goes until it can't, then goes back to the big one, so the second index, which we want to change less only changes after all the first index positions have been iterated through
        else:
            print(grid[a][i]) #do that until the very last one to get rid of the % character that hangs around 

# many other commenters mentioned using zip and join
print('\n'.join(map(''.join, zip(*grid)))) # this does the same thing as the nested for loops
# zip(*grid) effectively transposes the `grid` matrix by flipping it on the main diagonal
# `''.join, zip(*grid)` then each row is joined into one string 
# `'\n'.join(map())` then the rows are joined with newlines 
# map() returns a list of the results after applying the given function. However, not recommended for production code in large projects. 