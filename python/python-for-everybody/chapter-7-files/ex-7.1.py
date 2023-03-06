fh = open('mbox-short.txt') #short for file handle

for line in fh:
    # print(line) #doing it just like this, every line is printed AND every newline is printed; in the file, all the lines are one after another, but when printing like this, there's a newline between each line
    print(line.strip().upper()) #whitespace has to be stripped to display normally (`.rstrip()` could also be used). Apparently two methods can be called just like that. It returns a 'shouted' version of the file with proper spacing 