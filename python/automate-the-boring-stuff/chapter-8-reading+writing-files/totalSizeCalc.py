import os

os.dir

totalSize = 0 
for filename in os.listdir('/Users/jamescheney'):
    totalSize = totalSize + os.path.getsize(os.path.join('/Users/jamescheney',filename))

print(totalSize)