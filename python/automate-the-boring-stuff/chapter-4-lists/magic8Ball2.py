import random

messages = ['It is certain', 
'It is decidedly so',
'Yes, definitely',
'Reply hazy try again',
'Ask again later',
'Concentrate and ask again',
'My reply is no',
'Outlook not so good',
'Very doubtful'] 
# in a list, the spaces and returns between lines don't matter, same with spacing in assignments being ignored


print(messages[random.randint(0, len(messages) - 1)])
# print list `messages` using an index of the list. `random.randint` evaluates to an int. `randint` needs a lower boundary `index[0]` and an upper boundary `index[<however-many-values-in-the-list>]`, which is obtained with `len(messages)` which identifies how long the messages list is, then subtracts one to identify the top end of the index. Since index starts at 0, it ends one value lower than the `len()`