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
