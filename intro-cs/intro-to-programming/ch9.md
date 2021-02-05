# Dictionaries

* What is a collection?
    * A collection is nice because can put more than one value in it and carry them all around in one convenient package
    * We have a bunch of values in a single "variable"
    * We do this by having more than one palce "in" the variable
    * We have ways of finding the different places in the variable

* What is not a "collection"?
    * Most of our variables have one value in them - when we put a new value in the variable - the old value is overwritten

* A story of two collections..
    * List
        * A linear collection of values that stay in order
    * Dictionary
        * A "bag" of values, each with its own label
        
* Dictionaries
    * Dictionaries are Python's most powerful data collection
    * Dictionaries allow us to do fast database-like operations in Python
    * Dictionaries have different names in different languages
        * Associative Arrays - Perl/PHP
        * Properties or Map or HashMap - Java
        * Property Bag - C# / .Net
    * Lists index their entries based on the position in the list
    * Dictionaries are like bags - no order
        * Can't index by position!
    * So we index the things we put in the dictionary with a "lookup tag"

* Comparing Lists and Dictionaries
    * Dictionaries are like lists except that they use keys instead of numbers to look up values

* Dictionary Literals (Constants)
    * Dictionary literals use curly braces and have a list of key : value pairs
    * You can make an empty dictionary using empty curly braces

* Most common name?
    * Histograms or counting occurences

* Many counters with a dictionary
    * One common use of dictionaries is counting how often we "see" something

* Dictionary tracebacks
    * It is an error to reference a key which is not in the dictionary
    * We can use the in operator to see if a key is in the dictionary

* When we see a new name
    * When we encounter a new name, we need to add a new entry in the dictionary and if this is the second or later time we have seen the name, we simply add one to the count in the dictionary under that name

* The get method for dictionaries
    * The pattern of checking to see if a key is already in a dictionary and assuming a default value if the key is not there is so common that there is a method called get() that does this for us
    * One argument of `get()` defines a default value if key does not exist without tracebacks

* Simplified counting with `get()`
    * `counts[name] = counts.get(name, 0) + 1`

* Counting words in a text
    * The general pattern to count the words in a line of text is to split the line into words, then loop through the words and use a dictionary to track the count of each word independently

* Definite loops and dictionaries
    * Even though dictionaries are not stored in order, we can write a for loop that goes through all entries in a dictionary - actually it goes through all the keys in the dictionary and looks up the values

* Retrieving lists of keys and values
    * Calling list on `dictionary.keys()`
        * List
    * Calling list on `dictionary.values()`
        * List
    * Calling list on `dictionary.items()`
        * List of tuples

* Bonus: Two Iteration Variables!
    * We loop through the key-value pairs in a dictionary using *two* iteration variables
    * Each iteration, the first variable is the key and the second variable is the corresponding value for the key
    * `for k, v in d.items():`
