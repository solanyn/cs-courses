# Lists

* Programming
    * Algorithms
        * A set of rules or steps used to solve a problem
    * Data structures
        * A particular way of organising data in a computer

* What is not a 'collection'
    * Most of our variables have one value in them - when we put a new value in the variable, the old value is overwritten
    
* A list is a kind of collection
    * A collection allows us to put many values in a single "variable"
    * A collection is nice because we can carry many values around in one convenient package

* List constants
    * List constants are surrounded by square brackets and the elements in the list are seperated by commas
    * A list element can be any Python object - even another list
    * A list can be empty

* We already use lists!
    * `[5, 4, 3, 2, 1]`

* Lists and definite loops - best pals
    * `for friend in friends`

* Looking inside lists
    * Just like strings we can get at any single element in a list using an index specified by square brackets

* Lists are mutable
    * Strings are "immutable" - we can change the contents of a string - we must make a new string to make any change
    * Lists are "mutable" - we can change an element of a list using the index operator

* How long is a list?
    * The `len()` funciton takes a list as a parameter and returns the number of elements in the list
    * Actually `len()` tells us the numebr of elements of any set or sequence (such as a string)

* Using the range function
    * The range function returns a list of numbers that range from zero to one less than the parameter
    * We can constructy an index loop using for and an integer iterator

* A tale of two loops
    * `for i in range(len(friends))`
        * Using index to access elements
    * `for friend in friends`
        * Get each element directly

* Concatenating lists using +
    * We can create a new list by adding two existing lists together

* Lists can be sliced using :
    * Remember: Just like in strings, the second number is "up to but not including"

* List Methods
    * `dir(list())` lists all list methods

* Building a list from scratch
    * We can create an empty list and then add elemetns using the append method
    * The list stays in order and new elements are added at the end of the list
    
* Is something in a list?
    * Python provides two operators that let you check if an item is in a list
    * These logical operators return True or False
    * They do not modify the list

* Lists are in order
    * A list can hold many items and keeps those items in the order until we do something to change the order
    * A list can be sorted (i.e., change its order)
    * The sort method (unlike in strings) means "sort yourself", doesn't return anything

* Built-in Functions and Lists
    * There are a number of functions built into Python that take lists as parameters
    * Remember the loops we built? These are much simpler.

* Loops or lists?
    * If we have a program that takes the inputs to find the average until the user types done
    * Lists will use much more memory if we have millions of numbers

* Best friends: Strings and lists
    * `string.split()` breaks a string by a character or substring and returns the result as a list
    * We can then loop through this list
    * When you do not specify a delimiter, multiple spaces are treated like one delimiter
        * Lots of spaces will still split into the words any whitespace characters, including newlines or tabs
    * You can specify what delimiter character to use in the splitting

* The double split pattern
    * Sometimes we split a line one way and then grab one of the pieces of the line and split that piece again
    * Split a line of from line in email and then take the email domain name
    * Cleaner than `find()`

* Debugging
    * Print the line before it throws a traceback
    * Print the iterations to check
    * Guardian pattern are error checks that protects a condition which could throw a possible error

