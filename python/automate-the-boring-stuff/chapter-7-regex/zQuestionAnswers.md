1. `re.compile()` creates regex objects
2. raw strings are often used to create regex objects so that special characters don't have to be escaped
3. `search()` returns a `Match` object
4. to get the strings from the `Match` object, have to call `group()` or `groups()` on it (or the variable it was assigned to)
5. in the regex created from `r'(\d\d\d)-(\d\d\d-\d\d\d\d)'`, `.group()` would return nothing (would need to run `.groups()`),. `.group(1)` would return whatever matches `(\d\d\d)` and `.group(2)` would return whatever matches `(\d\d\d-\d\d\d\d)`
6. to match actual () and . and not interpret them as regex symbols, escape with `\(`, `\)`, `\.`
7. `findall()` returns a list of strings if there are no groups in the regex object. It returns a list of typles if there are groups
8. in regex, `|` signifies 'or'
9. in regex, `?` can indicate either an optional match (e.g. `(wo)?`) or nongreedy for `(.*?)` or `{3}?`
10. `*` means any - zero or more; `+` means at least one or more
11. `{3}` looks for a specific quantity of matches, `{3,5}` looks for a range of 3-5 matches
12. `\d`, `\w`, `\s` represent decimal, character, or space matches - respectively
13. `\D`, `\W`, `\S` represent anything that is NOT decimal, character, or space matches - respectively
14. `re.IGNORECASE` can be passed as second argument to `re.compile()` to cause the regex string to be case insensitive
15. `.` regularly matches all characters but newlines. if `re.DOTALL` is passed as second argument to `re.compile()`, it will match all characters *including* newlines
16. `.*` matches all characters in a string - up to, but not including newlines (assuming `re.DOTALL` isn't passed) - greedily. `.*?` matches all characters in a string - with the same caviat - nongreedily
17. a character class to match all numbers and lowercase letters would be `[0-9a-z]`
18. if `numRegex = re.compile(r'\d+')`, `numRegex.sub('X', '12 drummers, 11 pipers, five rings, 3 hens')` will return `('12','11','3')` - answer w/o checking cli. Oh, missed `.sub()` which substitutes `'X'` for any matches of numbers. Actually returns `'X drummers, X pipers, five rings, X hens'`
19. `re.VERBOSE` allows the use of multi-line strings and comments within a regex. Needs `'''` before and after, per python multiline string vocabulary 
20. write a regex that matches a number w commas for every three digits: \d{,3}?,
    - three decimals, followed by a comma, as many times as desired
    - needs to be 1 to 3 decimals, at the front, optionally followed by a comma and exactly three numbers at the end
    - `re.compile(^\d{1,3}(,\d{3})*$)`
        - start with 1-3 decimals, followed by zero or more groups at the end, containing three decimals
21. write a regex that matches the full name of someone whose last name is Nakamoto
    - assume that the first name that comes before it will always be one word that begins with a capital letter
        - match on only capitals w `[A-Z]`
            - `re.compile(r'([A-Z]{1}\d+) ([A-Z]{1}\d+)$')` - I'm overcomplicating this
            - `re.compile(r'([A-Z]{1}\d+) (Nakamoto)$')` - doesn't work. returns None when `Satoshi Nakamoto` sent to it 
            - looked on stackoverflow for identifying title case [here](https://stackoverflow.com/questions/36553272/how-to-write-a-regex-to-match-title-case-sentence-ex-i-love-to-work)
                - `re.compile(r'^[A-Z][a-z]+\s [Nakamoto]')` - didn't work; looked up the answer in the back of the book
                - `re.compile(r'^[A-Z][a-z]+\sNakamoto')` - I was on the way here. Clearly, plain text is matched within the `''` by default. Didn't need anything special to identify it. 
                    - `[A-Z]` match a single character from A-Z that's capitalized
                    - `[a-z]+` match one or more characters from a-z that are lowercase
                    - `\s` match a space-type character 
                    - `Nakamoto` match `Nakamoto` exactly
22. Write a regex that matches a sentence where the first word is either Alice, Bob, or Carol, second word is either eats, pets, or throws, and third word is apples, cats, or baseballs, and the sentence ends with a period. Regex should be case insensitive
    - `re.compile(r'(alice|bob|carol)\s(eats|pets|throws)\s(apples,cats,baseballs)\.', re.IGNORECASE)` - caveman brain converted the last group to using commas and not pipes
        - used a regex tester/debugger: https://regex101.com/
    - `re.compile(r'(alice|bob|carol)\s(eats|pets|throws)\s(apples|cats|baseballs)\.', re.IGNORECASE)`
