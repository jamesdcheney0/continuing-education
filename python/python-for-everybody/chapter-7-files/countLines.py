# Count lines
fhand = open('mbox-short.txt') #fhand = file handle mnemonic 
count = 0
for line in fhand:
    count = count + 1
print('Line Count:', count) # prints 'Line Count: 1910'

# read the *whole* file
fhand = open('mbox-short.txt') # can't use the same fhand for every block. Not sure why. I specifically tried to have just the one at top, and didn't get results. 
inp = fhand.read()
print(len(inp)) #prints the number of characters: 94626 
print(inp[:20])

# search through file
# search beginning of the line
fhand = open('mbox-short.txt')
for line in fhand:
    if line.startswith('From:'):
        # print(line) #prints every new line along with the results, so in the output, there's a carriage return between every email address that is returned 
        print(line.strip())
    # negative version that returns the same result 
    # if not line.startswith('From:'):
        # continue
    # print(line.strip())

# search anywhere in the line
fhand = open('mbox-short.txt')
for line in fhand: 
    line = line.rstrip() #does the same thing as including it in the print statement, but this is how he showed in his video, so I wanted to include it at least once 
    if not '@uct.ac.za' in line:
        continue
    print(line)

# prompt for file name & count lines starting with specific string
# fname = input('Enter the file name:  ')
# fhand = open(fname)
# count = 0
# for line in fhand:
#     if line.startswith('Subject:'):
#         count = count + 1
# print('There were',count,'subject lines in',fname)

# do the same as 34-41, but with error handling - bad handling won't work unless those lines are commented 
fname = input('Enter the file name:  ')
try: 
    fhand = open(fname)
except:
    print('Cannot find file', fname)
    quit() #terminate program silently; can only use continue in loops 
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print('There were',count,'subject lines in',fname)