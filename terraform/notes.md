# Built-in Functions
## Numeric Functions
- abs(): gives absolute value of given number
- floor(): returns closest whole number that is <= to given value
- log(x,y): returns logarithm of a given number 
- ceil(): rounds up to nearest whole number
- min(): takes one or more numbers & returns the smallest number from the set
- max(): takes one or more numbers & returns the largest number from the set
- parseint(): parses given string as a representation of an int in specified base (e.g. base 2, 10, 16, etc) and returns result
    - e.g. `parseint("100", 10) == 100`: translate 100 in base 10
    - e.g. `parseint("FF", 16) == 255`: translate FF in hex to an int
    - e.g. `parseint("1011111011101111", 2) == 48879`: translate binary string
- pow(x,y): calculates an exponent by raising first argument to the power of the second argument
- signum(): determines sign of a number (e.g. negative, zero, positive) w -1, 0, or 1

## String Functions
- chomp("str"): removes newline characters at end of str
- format("str"): produces string by formatting a number of other values according to specification string
    - e.g. `format("There are %d lights", 4)` returns 'There are 4 lights'
- formatlist("str", list): produces a list of string by formatting other values according to spec string
    - e.g. `formatlist("Hello, %s!", ["Valentina", "Ander", "Olivia", "Sam"])` returns
            [
                "Hello, Valentina"
                "Hello, Ander"
                "Hello, Olivia"
                "Hello, Sam"
            ]
- indent("str"): adds a given number of spaces to beginning of all lines but the first in a multiline string
- join("<operator>", [list]): produces a string by concatenating all elements of a list of string w <operator>
- lower("str"): converts all cased letters in string to lowercase
- upper("str"): converts all cased letters in string to uppercase
- regex("str"): applies regex to a string & returns matching substrings
- regexall("str"): applies regex to a string & returns list of all matches
- replace("str"): replaces given string for another given substring & replaces each occurence w given replacement string
    - e.g `replace("hello world", "/w.*d/", "everybody)` returns `'hello everybody'`
- split("<separator>","string"): produces a list by dividing string with <separator>
- strrev("string"): reverses characters in a string
- substr("str",<offset>,<len>): extract a substring from string by offset & length
    - e.g. `subset("hello world", 1, 4)` returns `ello`
- title("str"): converts first letter in each word in string to uppercase
- trim("str", "<characters>"): removes specified characters from start & end of string
    - e.g. `trim("!?Hello?!", "!?")` returns `Hello`
- trimprefix("str", "<prefix>"): removes specified <prefix> from start of string
- trimsuffix("str", "<suffix>"): removes specified <suffix> from end of string
- trimspace("str"): removes whitespace from start & end of string

## Collection functions
- alltrue([<bool>, <bool>]): returns true if all elements in collection are `true` or `"true"`
- anytrue([<bool>, <bool>]): returns true if any element in collection are `true` or `"true"`
- chunklist([<list>], <chunk>): splits a single list into fixed-size chunks, returning a list of lists
    - e.g. `chunklist(["a", "b", "c", "d", "e"], 2)`
    [ 
        [
            "a",
            "b"
        ]
        ...
    ]
- coalesce(): takes any number of arguments and returns the first one that isn't null or an emptry string
    - e.g. `coalesce("","a","b")` returns `a`
- coalescelist([]): takes any number of list arguments and returns the first one that isn't empty 
- compact([]): takes a list of strings and returns a new list w empty string elements removed
- concat([],[]): takes two or more lists and combines them into a single list
- contains([],<value>): determines whether a given list or set contains a given single <value> as one of it's elements; returns `true` or `false`
- distinct([]): takes a list and returns a new list w any duplicate elements removed 
- element([],<int>): retrieves a single element from a list
    - e.g. `element(["a", "b", "c"], 3)` returns `a` - index value 3 doesn't exist, so it wrapped back around to the beginning
- index([],<value>): finds the element index for a given value in a list
    - e.g. `index(["a", "b", "c"], "b")` returns `1`
- flatten([],[]): takes a list and replaces any elements that are lists with a flattened sequence of the list contents (turns multiple lists into one list)
- keys({}): takes a map and returns a list containing the *keys* from that map
- values({}): takes a map and returns a list containing the *values* of the elements in the map
- length(<value>): determines the length of a given list, map, or string. List counts values within list, map counts number of key:value pairs, string counts number of characters 
- lookup({},<key>, <default-value>): retrieves the value of a single element from a map, given its <key>. If the given <key> does not exist, the given <default-value> is returned
    - e.g. `lookup({a="ay", b="bee"}, "a", "what?")` returns `ay`
    - e.g. `lookup({a="ay", b="bee"}, "c", "what?")` returns `what?`
- matchkeys([],[],[]): constructs a new list by taking a subset of elements from one list whose indexes match the corresponding indexes of values in another list
    - e.g. `matchkeys(["i-123","i-abc","i-def"], ["us-west", "us-east", "us-east"], ["us-east"])` returns `["i-abc", "i-def"]`
- merge({}, {}): takes an arbitrary number of maps or objects, and returns a single map or object that contains a merged set of elements from all arguments. For duplicates, seems to return the value of the last occurence
    - e.g. `merge({a="b", c="d"}, {e="f", c="z"})` returns `{"a" = "b", "c" = "z", "e" = "f"}
- one([]): takes a list, set, or tuple value w either zero or one elements. If collection is empty, one() returns null. Otherwise, one returns the first element. If there are two or more elements, then one will return an error 
- range(<int>): generates a list of numbers using a start value, a limit value, and a step value (not all required)
    - e.g. `range(3)` returns `[0,1,2]`
- reverse([]): takes a sequence and produces a new sequence of the same length with all of the same elements as the given sequence but in reverse order
    - e.g. `reverse([1,2,3])` returns `[3,2,1]`
- setintersection([],[],[]): takes multiple sets and produces a single set containing only the elements that all of the given sets have in common; computes the intersection of the sets 
    - e.g. `setintersection(["a", "b"], ["b", "c"], ["b", "d"])` returns `["b"]`
- setproduct([],[]): finds all possible combinations of elements from given sets by computing the Cartesian product
    - e.g. `setproduct(["development", "staging", "production"], ["app1", "app2"])` returns `[["development","app1"],["development", "app2"]...]`
- setsubtract([],[]): returns a new set containing the elements from the first set that are not present in the second set; computes the relative complement of the first set in the second set 
    - e.g. `setsubtract(["a", "b", "c"], ["a', "c"])` returns `["b"]`
- setunion([],[]): takes multiple sets and produces a single set containing the unique elements from all the given sets
    - e.g `setunion(["a", "b"], ["b", "c"], ["d"])` returns `["d","b","c","a"]`
- slice([],<int>,<int>): extracts some consecutive elements from w/n a list
    - e.g. `slice(["a", "b", "c", "d"], 1, 3)` returns `["b","c"]` 
- sort([]): takes a list of strings and returns a new list with those strings sorted lexicographically (accounts for longer strings and can compare to shorter strings. pretty complicated concept)
    - e.g. `sort(["e", "d", "a", "x"])` returns `["a","b","e","x"]`
- sum([]): takes a list or set of numbers and returns the sum of those numbers. Can be int or float
- transpose({}): takes a map of lists of strings and swaps the keys and values to produce a new map of lists and strings
    - e.g. `transpose({"a" = ["1", "2"], "b" = ["2", "3"]})` returns `{ "1" = ["a"], "2" = ["a", "b"]...}`
- zipmap([],[]): constructs a map from a list of keys and a corresponding list of values
    - e.g. `zipmap(["a", "b"], [1, 2])` returns `{"a" = 1, "b" = 2}`