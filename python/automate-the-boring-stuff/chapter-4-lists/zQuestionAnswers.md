1. [] indicates a list
2. `spam[2] = 'hello'` to assign 'hello' to third value on a list
3. `spam = ['a','b','c','d']`; `spam[int('3' * 2)/11]` evaluates to `d`. For some reason it was evaluating to 3.0 and throwing an error. `spam[int(int('3'*2)/11)]` worked to provide `d` though
4. `spam[-1]` evaluates to `d`
5. `spam[:2]` evaluates to `['a','b']`
6. `bacon = [3.14,'cat',11,'cat',True]`; `bacon.index('cat')` evaluates to `1`
7. `bacon.append(99)` evaluates to `[3.14,'cat',11,'cat',True, 99]`
8. `bacon.remove('cat')` evaluates to `[3.14,11,'cat',True, 99]`
9. concatenation: `+=`, `-=`; replication: `*=`
10. `append()` adds to the end of a list; `insert()` adds a new value at a specific index
11. `del <listName>[<indexValue>]` and `<listName>.remove(<stringValue>)` are the two ways to remove values from lists
12. list and string values are similar in that they're both treated as a list, and able to print off the values at specific indexes
13. lists and tuples are most siginficantly different in that tuples are immutable and lists are mutable
14. `myTuple = (42,)` to assign a single value to a tuple
15. convert a list to a tuple: `tuple(myList)`; convert a tuple to a list `list(myTuple)`
16. values that contain list 'values' actually contain list references! 
17. `copy.copy()` used to change the reference value of a list, `copy.deepcopy()` used to copy list references when there's lists of lists