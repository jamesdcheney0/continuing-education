#! python
# practice project 1 for chapter 7
# write a function that uses regex to make sure the password string it is passed is strong
# strong password: 8+ characters long, contains upper and lowercase characters, and has at least one digit
# test string against multiple regex patterns to validate its strength

re.compile(r'''
        (\w{8,}')           #match any word-type character, and there needs to be at least 8
        ([A-Z]+[a-z]+\d){8,}) # how to do and? I think this would look for one or more capitals to start, one or more lowercases, and one digit at the end
        )''', reVERBOSE)

# `([A-Z]+[a-z]+\d)` matches `AAjjjjj8``, but `([A-Z]+[a-z]+\d){8,}` matches AAjjjjj8, if there are 8 instances of it back to back
# I was trying `([A-Za-z0-9]{8,})^\s` to say don't match space, but ^ says to look at the beginning for a space-type character 
#   Correct way to do it is `([A-Za-z0-9]{8,})\S`; `\S` is the != calculator  
    # does not enforce any of those requirements. a string of 8+ digits would match also
# asked the internet how to identify a character and number in a string. First commenter basically got to where I'm at on checking the length, and other folks helped clarify enforcing check for other values [here](https://stackoverflow.com/questions/7684815/regex-pattern-to-match-at-least-1-number-and-1-character-in-a-string)

# And after that, create a strongPassphrase detector - 24 characters+ long, and includes at least a digit and special characters 