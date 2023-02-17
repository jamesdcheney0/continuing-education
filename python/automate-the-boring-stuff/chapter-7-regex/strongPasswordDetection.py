#! python
import re
# practice project 1 for chapter 7
# write a function that uses regex to make sure the password string it is passed is strong
# strong password: 8+ characters long, contains upper and lowercase characters, and has at least one digit
# test string against multiple regex patterns to validate its strength

## First try
# re.compile(r'''
#         (\w{8,}')           #match any word-type character, and there needs to be at least 8
#         ([A-Z]+[a-z]+\d){8,}) # how to do and? I think this would look for one or more capitals to start, one or more lowercases, and one digit at the end
#         )''', reVERBOSE)

# `([A-Z]+[a-z]+\d)` matches `AAjjjjj8``, but `([A-Z]+[a-z]+\d){8,}` matches AAjjjjj8, if there are 8 instances of it back to back
# I was trying `([A-Za-z0-9]{8,})^\s` to say don't match space, but ^ says to look at the beginning for a space-type character 
#   Correct way to do it is `([A-Za-z0-9]{8,})\S`; `\S` is the != calculator  
    # does not enforce any of those requirements. a string of 8+ digits would match also
# asked the internet how to identify a character and number in a string. First commenter basically got to where I'm at on checking the length, and other folks helped clarify enforcing check for other values [here](https://stackoverflow.com/questions/7684815/regex-pattern-to-match-at-least-1-number-and-1-character-in-a-string)

## seems like `(?=.*[])` is the syntax for 'ensure string has...'
# [this](https://stackoverflow.com/questions/5142103/regex-to-validate-password-strength) forum was helpful in figuring my way to this solution 
strongishPassword = re.compile(r'''(
        ^                             # start anchor - look at the start of string and start matching
        #(?=.*[A-Za-z0-9])             # make sure string has a upper case, lower case, and number - technically, this says make sure string has one of any of these things, not one of each
        (?=.*[A-Z])             # make sure string has an upper case character
        (?=.*[a-z])             # make sure string has a lower case character
        (?=.*[0-9])             # make sure string has a digit 
        (?=.{8,})               # make sure string is 8+ characters long 
          )''', re.VERBOSE) 

text = input('Type in a password that is greater than eight characters long with at least one upper case, lower case and numeric character: ')
matches = []
if strongishPassword.search(text) == None:
    print("That's not a strongish password\n\n")
else:
    print("That is a strongish password\n\n")

print("To have a strong password, it should be long. Generally, it can't contain the name of the website the password is being created for")
longPassword = input("Try providing a password that is 24+ characters long. What the characters are doesn't matter: \n")

longPasswordChecker = re.compile(r'(?=.{24,})')
if longPasswordChecker.search(longPassword) == None:
    print("That's too short")
else: 
    print("There ya go, that's the way to do it. Hopefully it was easier to remember than random symbols throughout")






## And after that, create a strongPassphrase detector - 24 characters+ long, and includes at least a digit and special characters 