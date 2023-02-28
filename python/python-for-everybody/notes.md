# Chapter 2: Variables, expressions, and statements
- constants: value that doesn't change, e.g. `1`, `'hello world'`
- reserved words
- variables: named place in memory where data stored & retrieved later 
    - variables are assigned constants
        - e.g., `x = 12.1` can be said 'the variable `x`, using the assignment statement, is assigned to the constant `12.1`'
- mnemonic variable names
    - name variables to help remember what's meant to be stored 
    - keep in mind, python doesn't care about variable names and can't/won't interpret a difference based on the name assigned 
- assignment statement
    - evaluates the entire right side of the statement, then processes the left side 
- expressions
    - numeric expressions: +, -, *, /, ** (raise to power), % (remainder)
    - order of evaluation: follows PEMDAS + left to right for 'MD' and 'AS'
- type: difference between kinds of data 
    - concatenate: put together 
        - `+` between constants of the same type
    - type() [function]: check type of a constant or variable 
    - python3 division always provides a floating point number, regardless if the result could be an int 

# Chapter 3: Conditional Execution 
- comparison operators: <, <=, ==, >=, >, !=
- turn off tabs, and have IDE do 4 spaces instead of 1 tab
- `try` and `except`
    - anticipate when code might return a traceback and do something about it 
    - take a piece of code that might break, so `try` the code, and if it fails, then go to `except`
    - avoid overusing it; only put lines that could 'blow up' in it, and avoid multiple lines that could blow up to best nested within

# Chapter 4: Functions
- `def`: keyword to create function block
    - e.g. `def <function_name>(<optional_parameters>)`:
    - invoke function with `<function_name>()` and pass in necessary arguments 
- argument: value passed into function as its input when function is called
    - dynamically passed in when function is called 
- parameter: variable to use in function definition
    - statically defined when function is defined
- `return`: value that should be given after the function completes - the 'residual value' that occurs from the running of the function
    - better for a function to return a string rather than actually do the `print()`ing
- void functions: when a function doesn't return a value 

# Chapter 5: Loops & Iterations 
- `while` loop: (indefinite loop)
    - iteration variable: changes, so that the loop doesn't iterative forever 
    - zero-trip loops: not necessarily meant to run if the iteration variable is not the correct value 
    - `break` to get out of a loop. Continues to the line after the loop block 
    - `continue` says to finish the iteration and start at the top of the loop 
    - longer, more complex loops can be more challenging to see if a loop will be infinite 
- `for` loop: (definite loop)
    - runs a finite number of values, generally defined in a list 
    - `for <iteration variable> in <value>:`
    - manages the iteration variable without a bespoke statement incrementing it 
- loop idioms - how to construct loops 
    - making 'smart' loops
        - computers have to iterate once at a time. Have to figure out how to process the data, do something with it, and move on. Look at e.g. in ./python-for-everybody/exercise-5/largestNumber.py
