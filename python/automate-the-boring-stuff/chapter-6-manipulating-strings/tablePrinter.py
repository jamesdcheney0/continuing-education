tableData = [['apples','oranges','cherries','banana'],
             ['Alice','Bob','Carol','David'],
             ['dogs','cats','moose','goose']]

def printTable():
    # takes a list of strings and displays it in a well organized table
    # right justify each column of lists
    # assume that all the inner lists will countain the same number of strings
    # find the longest string in each of the lists, so the column can be wide enough to fit all the strings
    # store the max width of each column as alist of integers
    # begin with `colWidths = [0] * len(tableData)`` to create list containing the same number of 0 values as the number of inner lists in tableData
    colWidths = [0] * len(tableData) # currently, this returns [0, 0, 0]
    # for loop through colWidths, to get the length of the longest item in each list and add that value to the index
    for i in range(len(colWidths)): # The internet recommends using ennumerate(), but I wasn't tracking how to use it, and shortly after figured how to make this work using info from [here](https://www.studytonight.com/python-howtos/how-to-choose-the-longest-string-in-a-python-list#:~:text=Example%3A%20Find%20Longest%20String%20from%20List%20using%20max()%20Function,string%20with%20the%20maximum%20length.)
        colWidths[i] = len(max(tableData[i],key=len)) # returns highest value of string in each list; returns [8, 5, 5]
        # for column in range(len(tableData[i])):
        #     for row in range(len(tableData)):
        #         print(str(tableData[column][row]).rjust(int(colWidths(row))))

    ## copied this from [here](https://stackoverflow.com/questions/34488115/automate-the-boring-stuff-chapter-6-table-printer-almost-done)
    for x in range(len(tableData[0])):
        for y in range(len(tableData)):
            print(tableData[y][x].rjust(colWidths[y]), end = ' ')
        print()
    ## Looking at the bottom of the comments, I was very close to this, but bailed probably too early
    
    # for column in range(len(tableData)):
    #     print(str(tableData[column]).rjust(colWidths[column])) #just prints the lists
    #     print('\n'.join(tableData[column])) # prints plain text of each of the elements in each of the lists 
    # for the number of lists in tableData, 3
    # print the entirety of the list from tableData, rjust() by the integer at the specified index in colWidth

    # for column in range len tabledata
    
    # for row in range len tabledata[0]
        
    # print index [0,0].rjust(colWidths[0]), index[1,0].rjust(colWidths[1]), index[2,0].rjust(colwidths[2]) 
            
    # find the largest value in `colWidths` list to find out what integer width to pass to `rjust()`
    # would I have to print each item at index[0], then index[1] etc to print columns? 
    # for i in range(len(tableData)):
    #     print(tableData[i])

    # print(str(len(tableData)) + ' length of tableData') # Counts the numbers of lists in the list (aka, counts elements of type 'list' in the list 'tableData)
    # print(str(len(tableData[0])) + ' length of tableData[0]') # counts the number of elements in the lists in the list (aka count elements of type string within elements of type list within the list tableData)

    # this suggestion from [here](https://stackoverflow.com/questions/54100637/how-to-print-list-of-lists-with-justified-text-the-integer-length-to-rjust-co) prints in the wrong direction; 4 columns of 3 rows 
    # for row in range(len(tableData)):
    #     for column in range(len(tableData[0])):
    #         print(tableData[row][column].rjust(10),end='')
    #     print('')

    # this just errors 'list index out of range
    # for column in range(len(tableData[0])):
    #     for row in range(len(tableData)):
    #         print(tableData[column][row].rjust(10),end='')
    # for i in range(len(tableData[0])):
    #     print(tableData[0][i].rjust(colWidths))
    
    # debugging
    # print(len(max(tableData[i],key=len)))
    # print(colWidths)

printTable()