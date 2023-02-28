#! python3
# playing around with code examples from the video

rawstr = input('Enter a number: ')
try:
    ival = int(rawstr)
except: 
    ival = print('enter an integer or float')

# if ival > 0:
#     print('Nice work')
# else:
#     print('Not a number')

print(type(ival),ival)