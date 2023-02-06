1. `spam={}`
2. `spam={'foo':42}`
3. dictionary indexes are defined by the user and list indexes are based on a count from 0
4. calling `spam[foo]` on `spam = {'bar':100}` produces an error
5. `spam = {'cat':'pet', 'cow':'cattle'}` `'cat' in spam` would return true, looking for 'cat' anywhere in the dictionary and would evaluate `True`; `'cat' in spam.keys()` would look for 'cat' only in the key: side of the key:value pair and would evaluate `True`
6. `spam = {'cat':'pet', 'cow':'cattle'}` `'cat' in spam` would return true, looking for 'cat' anywhere in the dictionary and would evaluate `True`; `'cat' in spam.values()` would look for 'cat' only in the :value side of the key:value pair and would evaluate `False`
7. `spam.setdefault('color':'black')` to evaluate if the directory spam has color and if it doesn't, add that key:value pair
8. `pprint.pprint()` prints dictionary values prettily