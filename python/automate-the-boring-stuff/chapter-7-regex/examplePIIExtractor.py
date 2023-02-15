#! python3
# examplePIIExtractor | phoneAndEmail.py - finds phone numbers and email addresses on the clipboard


# use pyperclip
import pyperclip, re

# Find all phone numbers and email addresses in the text
# Create two regexes, 
# one for matching phone numbers 
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))               # area code (optional)
    (\s|-|\.)?                      # separator (optional)
    (\d{3})                         # first three digits
    (\s|-|\.)                       # separator
    (\d{4})                         # last four digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension
    )''',re.VERBOSE)

# and one for matching email addresses
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+   # username
    @                   # @ symbol
    [a-zA-Z0-9.-]+      # domain name
    (\.[a-zA-Z]{2,4})   # dot-something
    )''',re.VERBOSE)

# Get the text off the clipboard
# Find all matches, not just the first match, of both regexes
text = str(pyperclip.paste())
matches=[]
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else: 
    print ('No phone numbers or email addresses found.')


# Paste them onto the clipboard
# neatly format the matched strings into a single string to paste


# Display some kind of message if no matches were found in the text 