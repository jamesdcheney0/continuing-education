def spam():
    eggs = 31337

spam()
# print(eggs)

# eggs in local scope doesn't affect eggs in global scope

# Traceback (most recent call last):
#   File "/Users/jamescheney/Documents/1000-hours/python/automate-the-boring-stuff/chapter-3-functions/consider.py", line 5, in <module>
#     print(eggs)
# NameError: name 'eggs' is not defined
