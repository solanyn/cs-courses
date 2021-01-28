# Strings
* String Data Type
    * A string is a sequence of characters
    * A string literal uses quotes 'Hello' or "Hello"
    * For strings, + means "concatenate"
    * When a string contains numbers, it is still a string
    * We can convert numbers in a string into a number using `int()`

* Reading and Converting
    * We prefer to read data in using strings and then parse and convert the data as we need
    * This gives us more control over error situations and/or bad user input
    * Raw input numbers must be converted from strings

* Looking inside strings
    * WE can get at any single character in a string using an index specified in square brackets
    * The index value must be an integer and starts at zero
    * The index value can be an expression that is computed

* A character too far
    * You will get a Python error if you attempt to index beyond the end of a string
    * So be careful when constructing index values and slices

* Strings have length
    * The built-in function `len` gives us a length of a string

* Looping through strings
    * Using a while statement and an interation variable, and the len function, we can construct a loop to look at each of the letters in a string individually
    * A definite loop using a for statement is much more elegant
    * The iteration variable is completely taken care of by the for loop

* Looping and counting
    * Can count the number of letters in a string by looping the string

* Looking deeper into in
    * The iteration variable "iterates" through the sequence (ordered set)
    * The block (body) of code is executed once for each value in the sequence
    * The iteration variable moves through all of the values in the sequence

## More string operations
* Slicing strings
    * We can also look at any continuous section of a string using a colon operator
    * The second number is one beyond the end of the slice - "up to but not including"
    * If the second number is beyond the end of the string, it stops at the end
    * If we leave off the first number or the last number of the slice, it is assumed to be the beginning or end of the string respectively
* String concatenation
    * When the + operator is applied to strings it means concatenation

* Using in as a logical operator
    * The in keyword can also be used to check to see if one stirng is "in" another string
    * The in expression is a logical expression that returns True or False and can be used in an if statement
    
* String comparison
    * Lexographically greater than or less than
    * Deterministic way to sort strings
    * Depends on character set of computer

* String library
    * Python has a number of string functions which are in the string library
    * These functions are already built into every string - we invoke them by appending the function to the string variable
    * These functions do not modify the original string, instead they return a new string that has been altered
    * `string.lower()`
    * `dir(string)` shows all the string methods available

* Searching a string
    * We use the `find()` finds the first occurrence of the substring
    * `find()` finds the first occurrence of the substring
    * If the substring is not found, `find()` returns -1
    * Remember that string position starts at zero

* Making everything UPPER CASE
    * You can make a copy of a string in lower case or upper case
    * Often when we are searching for a string using `find()` we first convert the string to lower case so we can search a string regardless of case

* Search and replace
    * The replace function is like a "search and replace" operation in a word processor
    * It replaces all occurrences of the search string with the replacement string

* Stripping whitespace
    * Sometimes we want to take a string and remove whitespace at the beginning and/or end
    * `lstrip()` and `rstrip()` remove the whitespace at the left or right
    * `strip()` removes both beginning and ending whitespace

* Prefixes
    * `'Hello'.startswith('H')` is true

* Two kinds of strings
    * In Python 3, all strings are unicode

 
