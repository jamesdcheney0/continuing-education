#! Python3
# pw.py: an insecure Password Manager Project

PASSWORDS = {'email': 'B1%AtzGOKKVQ*g$!%%N9',
             'blog': 'rnzlNexz^In5IyXF79J!',
             'luggage': '12345'}

import sys, pyperclip # had to install this via pip3 before being able to import it
if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1] # first command line argument is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)