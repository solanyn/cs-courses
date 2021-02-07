- [Course Information](#introduction-to-programming)
- [Chapter 1 - Why Program?](#chapter-1---why-program-)
- [Chapter 2 - Variables, Expressions and Statements](#chapter-2---variables--expressions-and-statements)
- [Conditionals](#conditionals)
- [Functions](#functions)
- [Loops and Iteration](#loops-and-iteration)
- [Strings](#strings)
  * [More string operations](#more-string-operations)
- [Files](#files)
- [Lists](#lists)
- [Dictionaries](#dictionaries)
- [Tuples](#tuples)
  * [Tuples are like lists](#tuples-are-like-lists)
  * [but... Tuples are "immutable"](#but-tuples-are--immutable-)
  * [Things not to do with tuples](#things-not-to-do-with-tuples)
  * [A tale of two sequences](#a-tale-of-two-sequences)
  * [Tuples are more efficient](#tuples-are-more-efficient)
  * [Tuples and assignment](#tuples-and-assignment)
  * [Tuples and Dictionaries](#tuples-and-dictionaries)
  * [Tuples are comparable](#tuples-are-comparable)
  * [Sorting lists of tuples](#sorting-lists-of-tuples)
  * [Using `sorted()`](#using--sorted---)
  * [Sort by values instead of key](#sort-by-values-instead-of-key)
  * [Top 10 most common words](#top-10-most-common-words)
  * [Even shorter version](#even-shorter-version)
- [Regular Expressions](#regular-expressions)
  * [Regular Expressions](#regular-expressions-1)
  * [Understanding Regular Expressions](#understanding-regular-expressions)
  * [The Regular Expression Module](#the-regular-expression-module)
  * [Using re.search() like find()](#using-research---like-find--)
  * [Using re.search() like startswith()](#using-research---like-startswith--)
  * [Wild-card characters](#wild-card-characters)
  * [Fine-tuning your match](#fine-tuning-your-match)
  * [String parsing examples](#string-parsing-examples)
  * [The double split pattern](#the-double-split-pattern)
  * [Regex version](#regex-version)
  * [Even cooler regex version](#even-cooler-regex-version)
  * [Escape character](#escape-character)
  * [Summary](#summary)
- [Networked Programs](#networked-programs)
  * [Transport Control Protocol (TCP)](#transport-control-protocol--tcp-)
  * [TCP Connections / Sockets](#tcp-connections---sockets)
  * [TCP Port Numbers](#tcp-port-numbers)
  * [Common TCP Ports](#common-tcp-ports)
  * [Sockets in Python](#sockets-in-python)
  * [Application protocols](#application-protocols)
  * [HTTP - Hypertext Transfer Protocol](#http---hypertext-transfer-protocol)
  * [HTTP](#http)
  * [What is a protocol?](#what-is-a-protocol-)
  * [Getting data from the server](#getting-data-from-the-server)
  * [Internet standards](#internet-standards)
  * [Accurate hacking in the movies](#accurate-hacking-in-the-movies)
  * [An HTTP Request in Python](#an-http-request-in-python)
  * [About characters and strings](#about-characters-and-strings)
  * [ASCII](#ascii)
  * [Representing simple strings](#representing-simple-strings)
  * [Unicode](#unicode)
  * [Multi-Byte Characters](#multi-byte-characters)
  * [Two kinds of strings in Python](#two-kinds-of-strings-in-python)
  * [Python3 and Unicode](#python3-and-unicode)
  * [Python Strings to Bytes](#python-strings-to-bytes)
  * [Using urllib in Python](#using-urllib-in-python)
  * [Like a file...](#like-a-file)
  * [Reading web pages](#reading-web-pages)
  * [What is web scraping?](#what-is-web-scraping-)
  * [Why scrape?](#why-scrape-)
  * [Scraping web pages](#scraping-web-pages)
  * [The easy way - Beautiful Soup](#the-easy-way---beautiful-soup)
  * [Summary](#summary-1)
- [Using Web Services](#using-web-services)
  * [Data on the Web](#data-on-the-web)
  * [Sending Data across the "Net"](#sending-data-across-the--net-)
  * [Agreeing on a "Wire Format"](#agreeing-on-a--wire-format-)
  * [XML](#xml)
  * [eXtensible Markup Language](#extensible-markup-language)
  * [XML Terminology](#xml-terminology)
  * [XML Basics](#xml-basics)
  * [Whitespace](#whitespace)
  * [XML "Elements" (or Nodes)](#xml--elements---or-nodes-)
  * [XML as a Tree](#xml-as-a-tree)
  * [XML as Paths](#xml-as-paths)
  * [XML Schema](#xml-schema)
  * [XSD XML Schema (W3C spec)](#xsd-xml-schema--w3c-spec-)
  * [XSD Structure](#xsd-structure)
  * [JavaScript Object Notation](#javascript-object-notation)
  * [Service Oriented Approach](#service-oriented-approach)
  * [Multiple Systems](#multiple-systems)
- [Web Services](#web-services)
  * [Application Program Interface](#application-program-interface)
  * [API Security and Rate Limiting](#api-security-and-rate-limiting)
- [Python Objects](#python-objects)
  * [Warning](#warning)
  * [Review of Programs](#review-of-programs)
  * [Object Oriented](#object-oriented)
  * [Object](#object)
  * [Definitions](#definitions)
  * [Terminology: Class](#terminology--class)
  * [Terminology: Instance](#terminology--instance)
  * [Terminology: Method](#terminology--method)
  * [A sample class](#a-sample-class)
  * [Playing with dir() and type()](#playing-with-dir---and-type--)
  * [Try dir() with a String](#try-dir---with-a-string)
  * [Object Lifecycle](#object-lifecycle)
  * [Many instances](#many-instances)
  * [Inheritance](#inheritance)
  * [Terminology: Inheritance](#terminology--inheritance)
  * [Definitions](#definitions-1)
  * [Summary](#summary-2)
- [Relational Databases and SQLite](#relational-databases-and-sqlite)
  * [Random access](#random-access)
  * [Relational databases](#relational-databases)
  * [Terminology](#terminology)
  * [SQL](#sql)
  * [Web Applications w/ Databases](#web-applications-w--databases)
  * [Database Administrator](#database-administrator)
  * [Database Model](#database-model)
  * [Common Database Systems](#common-database-systems)
  * [SQLite Browser](#sqlite-browser)
  * [Let's make a database!](#let-s-make-a-database-)
  * [SQL: Insert](#sql--insert)
  * [SQL: Delete](#sql--delete)
  * [SQL: Update](#sql--update)
  * [Retrieving Records: Select](#retrieving-records--select)
  * [Sorting with ORDER BY](#sorting-with-order-by)
  * [This is not too exciting (so far)](#this-is-not-too-exciting--so-far-)
  * [Complex Data Models and Relationships](#complex-data-models-and-relationships)
  * [Database Design](#database-design)
  * [Building a data model](#building-a-data-model)
  * [For each "piece of info"](#for-each--piece-of-info-)
  * [Representing Relationships in a Database](#representing-relationships-in-a-database)
  * [Relational Power](#relational-power)
  * [The JOIN Operation](#the-join-operation)
  * [Many-to-many to Relationships](#many-to-many-to-relationships)
  * [Complexity enables speed](#complexity-enables-speed)
  * [Additional SQL Topics](#additional-sql-topics)
  * [Summary](#summary-3)
- [Retrieving and visualising data](#retrieving-and-visualising-data)
  * [Multi-step data analysis](#multi-step-data-analysis)
  * [Many data mining technologies](#many-data-mining-technologies)
  * ["Personal Data Mining"](#-personal-data-mining-)
  * [GeoData](#geodata)
  * [Page Rank](#page-rank)
  * [Web crawler](#web-crawler)
  * [Process](#process)
  * [Web crawling policy](#web-crawling-policy)
  * [robots.txt](#robotstxt)
  * [Google Architecture](#google-architecture)
  * [Search Indexing](#search-indexing)
  * [Mailing Lists - Gmane](#mailing-lists---gmane)
  * [Warning: This dataset is > 1GB](#warning--this-dataset-is---1gb)

# Introduction to Programming
OSSU recommends the Python for Everybody course available here:
https://www.py4e.com/lessons

# Chapter 1 - Why Program?

* Computers want to be helpful
    * Built for one purpose - to do some things for us
    * Need to speak their language to describe what we want done

* Programmers Ancticipate Needs
    * iPhone applications are a market
    
* Users vs. Programmers
    * Users see computers as a set of tools - word processor, spreadsheet etc

* Why be a programmer?
    * To get some task done
        * We start with this
    * To produce something for others to use - job
        * Add guestbook to a website
        * Needs a little more training

* What is Code? Software? A Program?
    * A sequence of stored instructions
        * It is a little piece of our intelligence in the computer
        * We figure something out then we encode it and then give it to someone else to save them the time and energy of figuring it out
    * A piece of creative art - particularly when we do a good job on user experience

* Programs for Humans
    * Macarena
        * Effectively a set of instructions
    * Humans are good at correcting errors
        * Computers are not and are extremely literal
    * We have to be really precise in our instructions
        * Computers can't compenensate when we make small mistakes
        
* Programs for Python
    * Counting the most frequent word in a sentence
    * Can't easily solve the problem as human

* Hardware Architecture
    * Why hardware architecture?
        * Understand what our resources are
    * Definitions
        * CPU
            * Central Processing Unit
            * Asks many times per seconds, what do you want me to do next?
            * Through the pins, we feed it instructions
            * We can't talk to it directly, so we store it in the RAM
            * Not that smart, but very very fast
        * RAM
            * Random Access Memory
            * Where our instructions are stored
                * We write the instructions
            * Instructions disappear when power is off
            * Temporary storage
            * **We are here**
        * Secondary Storage
            * Permanent storage
            * Files, applications and things live here

* Python as a Language
    * Early Learner: Syntax Errors
        * Need to learn Python language so we can communicate our instructions to Python.
    * What do we say?
        * Elements of Python
            * Vocabulary / Words - Variables and Reserved words
            * Sentence structure - valid syntax patterns
            * Story structure - constructing a program for a purpose

        * Interactive vs. Script
            * Interactive - type directly to Python one line at a time and it responds
            * Script - Enter a sequence of statements into a file using a text editor and tell Python to execute the statements in the file

        * Program Steps or Program Flow
            * Program is a sequence of steps to be done in order
            * Steps can be conditional (can be skipped)
            * Sometimes steps or groups of steps is to be repeated
            * Sometimes store a set of steps to be used over and over as needed several places throughout the program

        * Conditional 
            * If statements
        * Repeated
            * Iteration statements

# Chapter 2 - Variables, Expressions and Statements

* Constants
    * Fixed values are called constants

* Reserved Words
    * Cannot use reserved words as variable names / identifiers

* Variables
    * Choose names of variables
    * Change the contents of a variable in a later statement

* Python Variable Name Rules
    * Must start with a letter or underscore _
    * Must consist of letters, numbers and underscores
    * Case Sensitive

* Mnemonic Variable Names
    * Since we are given a choice in how we choose our variable names, there is a bit of 'best practive'
    * Name variables to help us remember what we intend to store in them (memory aid)
    * Can be confusing since well-named variables often sound so good that they must be keywords

* Sentences or Lines
    * Assignment statements
        * Assign a value to a variable using the assignment statement
    * Expression statements
        * Numeric Expressions
            * Addition + 
            * Subtraction -
            * Multiplication *
            * Division /
            * Power **
            * Remainder %
        * Order of Evaluation
            * Parenthesis
            * Power
            * Multiplication
            * Addition
            * Left to right
    * What does "Type" Mean?
        * In Python variables, literals, and constants have a "type"
    * Type Matters
        * Some operations are prohibited
        * Python knows what "type"
        * You cannot "add 1" to a string
        * Can ask Python what type something is by using the `type()` function
    * Several Types of Numbers
        * Float
        * Integer
    * Type conversions
        * Integer will be implicitly converted to float in an expression with a float and integer
        * Can control this with built in functions `int()` and `float()`
    * Integer Division
        * Integer division produces a floating point result
    * String Conversions
        * Convert from string to float or int
        * Error is string does not contain numeric characters
    * User Input
        * We can instruct Python to pause and read data from the user using the input() function
        * The input() function returns a string
    * Converting User Input
        * If we want to read a number from the user, we must convert it from a string to a number using a type conversion function
    * Comments in Python
        * Anything after a `#` is ignored by Python
        * Why comment?
            * Describe what is going to happen in a sequence of code
            * Document who wrote the code or other ancilliary information
            * Turn off a line of code - perhaps temporarily

            

# Conditionals

* Conditional Steps
    * Check something that make a decision depending on the condition
* Comparison Operator
    * Boolean expressions using comparison operators evaluate to True / False or Yes / No
    * Comparison operators look at variables but do not change the variables

* Indentation
    * Increase indent after an if statement or for statement (after :)
    * Maintain indent to indicate scope
    * Blank lines are ignored - they do not affect indentation
    * Reduce indentation back to the level of the if statement or for statement to indicate the end of the block

* Mixing tabs and spaces will result on indentation errors even if everything looks fine

* Two-way Decisions with else
    * if-else statements
    * One or two the branches will run but in no case will both of the branches run

* Multi-way
    * elif statements
    * Run one and skip the other two, only runs one path until condition is satisfied
    * Order matters
    * Can have no else statement

* Multi-way Puzzles
    * Careful with expressions, only runs until it sees Falses, does not look further ahead

* Try / Except Structure
    * Surround a dangerous section of code with try and except
    * If the code in the try works - the except is skipped
    * If the code in the try fails - it jumps to the except section
    * If errors occur outside the try-exception structure, execution stops
    * Doesn't come back to the code if exception occurs
    * Careful with usage for this reason



# Functions

* Store and reuse 
    * We don't like to repeat ourselves
    * To do with reliability
    * `def` is a new keyword
    * Defining functions does not actually run any code, it stores code
    * Invoking it will run 

* Python functions
    * Two types of functions
        * Built in functions that are part of functions `print()`, `int()`, `float()`
        * Functions that we define ourselves and then use
    * We treat the built-in function names as "new" reserved words ie. avoid them as variable names

* Function Definition
    * Function is a reusable that takes arguments as input, does some computation and then returns a result or results
    * We define a function using the def reserved word
    * We call or invoke the function by using the function name, parentheses, and arguments in an expression

    * eg. `big = max('Hello world')` 

* Type conversions
    * When you put an integer and floating point in an expression, the integer is implicitly coverted to a float
    * You can control this with the built-in functions int() and float()

* Building our own functions
    * We create a new function by using the def keyword followed by optional parameters in parentheses
    * We indent the body of the function
    * This defines the function but does not execute the body of the function
    * Only stores and remembers!

* Definitions and uses
    * Once we have dfined a function we can call or invoke it as many times as we like
    * This is the store and reuse pattern

* Arguments
    * An argument is a value we pass into the function as its input when we call the function
    * We use arguments so we can direct the function to do different kinds of work when we call it at different times
    * We put the arguments in parentheses after the name of the function

* Parameters
    * A parameter is a variable which we use in the function definition. It is a "handle" that allows the code in the function to access the argumentts for a particular function invocation

* Return values
    * Often a function will take its arguments, do some computation and return a value to be used as the value of the function call in the calling expression. The return keyword is used for this.
    * A fruitful function is one that produces a result or return value
    * The return statement ends the function execution and "sends back" the result of the function

* Arguments, Parameters, and Results
    * Somewhere in the max function there is a return

* Multiple Parameters / Arguments
    * We can define more than one parameter in the function definition
    * We simply add more arguments when we call the function
    * We match the number and order of arguments and parameters

* Void (non-fruitful) functions
    * When a function does not return a value, we call it a "void" function
    * Functions that return values are "fruitful" functions
    * Void functions are "not fruitful"

* To function or not to function...
    * Organise your code into "paragraphs" - capture a complete thought and "name it"
    * Don't repeat yourself - make it work once and then reuse it
    * If something gets too long or complex, break it up into logical chunks and put those chunks in functions
    * Make a library of common stuff that you do over and over - perhaps share this with your friends...



# Loops and Iteration

* Repeated Steps
    * Loops (repeated stpes) have iteration variables that change each time through a loop. Often these iteration variables go through a sequence of numbers.
    * An infinite loop. If we did nothing with iteration variable.
    * What is the loop doing. Nothing. Acts as if statement.

* Breaking out of a loop
    * The break statement ends the current loop and jumps to the statement immediately following the loop
    * It is like a loop test that can happen anywhere in the body of the loop
    
* Finishing an Iteration with continue
    * The continue statement ends the current iteration and jumps to the top of the loop and starts the next iteration.
    * Goes back to top and asks condition again

* Indefinite Loops
    * While loops are called "indefinite loops" because they keep going until a logical condition becomes False
    * The loops we have seen so far are pretty easy to examine to see if they will terminate or if they will be "infinite loops"
    * Sometimes it is a little harder to be sure if a loop will terminate

* Definite Loops
    * Quite often we have a list of items of the lines in a file - effectively a finite set of things
    * We can write a loop to run the loop once for each of the items in a set using the Python `for` construct
    * These loops are called "definite loops" because they execute an exact number of times
    * We say that "definite loops iterate through members of a set"

* A Simple Definite Loop
    * ```for i in [5, 4, 3, 2, 1]:
    		print(i)
	print('Blastoff!')```
    * A definite loop with strings
        * `for friend in friends: ...`
    * Definite loops (for loops) have explicit iteration variables that change each time through a loop. These iteration variables move through the sequence or set.

* Looking `in`
    * The iteration variable "iterates" through the sequence (ordered set)
    * The block (body) of code is executed once for each value in the sequence
    * The iteration variable moves through all of the values in the sequence

* Loop Idioms: What we do in loops
    * Counting in a loop
    	* To count how many times we execute a loop, we introduce a counter variable that starts at 0 and we add one to it each time through the loop
    * Summing in a loop
    	* To add up a value we encounter in a loop, we introduce a sum variable that starts at 0 and we add the value to the sum each time through the loop
    * Finding the average in a loop
        * An average just combines the counting and the sum patterns and divides when the loop is done.
    * Filtering in a loop
    	* We use an if statement in the loop to catch/filter the values we are looking for.
    * Search using a boolean variable
        * If we just want to search and know if a value was found, we use a variable that starts at False and is set to True as soon as we find what we are looking for.
    * How to find the smallest value
        * To find the largest value we change the comparison operator such that it assigns the larger value to the variable we capture.

* The "is" and "is not" operators
    * Python has an is operator that can be used in logical expressions
    * Implies "is the same as"
    * Similar to, but stronger than ==
    	* Only checks for equivalence in value 0 == 0.0 (True) but 0 is 0.0 (False)
    * `is not` also is a logical operator
    * Use only on `None` and boolean checks

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

 

# Files
* File processing
    * A text file can be thought of as a sequence of lines

* Using `open()`
    * `handle = open(filename, mode)`
    * returns a handle use to manipulate the file
    * filename is a string
    * mode is optional and should be `r` if we are planning to read the file and `w` if we are going to write to the file

* What is a handle?
    * Interface to file
    * Not file itself

* The newline character
    * Represented as a `\n`
    * One character

* File processing
    * A text file has newlines at the end of each line

* File handle as a sequence
    * File handle open for read can be treated as a sequence of strings where each line in the file is a string in the sequence
    * We can use the for statement to iterate through a sequence
    * Remember a sequence is an ordered set

* Counting lines in a file
    * Open a file read-only
    * Use a for loop to read each line
    * Count the lines and print out the number of lines

* Reading the whole file
    * We can read the whole file (newlines and all) into a single string.
    * Call `handle.read()` where handle is the object returned by `open('file.txt')`

* Searching through a file
    * We can put an if statement in our for loop to only print lines that meet some criteria

* OOPS!
    * What are all these blank lines doing here?
    * Each line from the file has a newline at the end
    * The print statement adds a newline to each line

* Searching through a file (fixed)
    * We can strip the whitespace from the right-hand side of the string using `rstrip()` from the string library
    * The newline is considered a "whitespace" and is stripped

* Skipping with continue
    * We can conveniently skip a line by using the continue statement

* Using in to select lines
    * We can look for a string anywhere in a line as our selection criteria

* Dealing with bad file names
    * In try except when catching exception, call `quit()` to silently terminate the Python program


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

# Tuples

## Tuples are like lists
* Tuples are another kind of sequence that funcitons much like a list - they have elements which are indexed starting at 0
* List functions work the same way as list - max, min

## but... Tuples are "immutable"
* Unlike a list, once you create a tuple, you cannot alter its contents - similar to a string

## Things not to do with tuples
* `x.sort()`
* `x.append()`
* `x.reverse()`

## A tale of two sequences
* `dir(list())`
    * Many list manipulation methods
* `dir(tuple())`
    * None, only count and index

## Tuples are more efficient
* Since Python does not have to build tuple structures to be modifiable, they are simpler and more efficient in terms of memory use and performance than lists
* So in our program when we are making "temporary variables" we prefer tuples over lists

## Tuples and assignment
* We can also put a tuple on the left-hand side of an assignment statement
* We can even omit the parenthesis
* `a, b = (1, 2)`

## Tuples and Dictionaries
* The `items()` method in dictionaries returns a list of (key, value) tuples

## Tuples are comparable
* The comparison operators work with tuples and other sequences. If the first item is equal, Python goes on to the next element, and so on, until it finds elements that differ.

## Sorting lists of tuples
* We can take advantage of the ability to sort a list of tuples to get a sorted version of a dictionary
* First we sort the dictionary by the key using `items()` method and `sorted()` function

```Python
>>> d = {('a': 10), ('c', 22), ('b', 1)}
>>> d.items()
dict_items([('a', 10), ('c', 22), ('b', 1)])
>>> sorted(d.items())
[('a', 10), ('b', 1), ('c', 22)]
```

## Using `sorted()`
* We can do this even more directly using the built-in function `sorted` that takes a sequence as a parameter and returns a sorted sequence

```Python
>>> d = {'a':10, 'b':1, 'c':22}
>>> t = sorted(d.items())
>>> t
[('a', 10), ('b', 1), ('c', 22)]
>>> for k, v in sorted(d.items()):
...     print(k, v)
...
a 10
b 1
c 22
```

## Sort by values instead of key
* If we could construct a list of tuples of the form (value, key) we could sort by value
* We can do this with a for loop that creates a list of tuples

```Python
>>> c = {'a':10, 'b':1, 'c':22}
>>> tmp = list()
>>> for k, v in c.items():
...     tmp.append( (v, k) )
...     
>>> print(tmp)
[(10, 'a'), (22, 'c'), (1, 'b')]
>>> tmp = sorted(tmp, reverse=True)
>>> print(tmp)
[(22, 'c'), (10, 'a'), (1, 'b')]
```

## Top 10 most common words
```Python
fhand = open('romeo.txt')
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

lst = list()
for key, val in counts.items():
    newtup = (val, key)
    lst.append(newtup)

lst = sorted(lst, reverse=True)

for val, key in lst[:10]:
    print(key, val)        
```

## Even shorter version
```Python
>>> c = {'a':10, 'b':1, 'c':22}
>>> print(sorted([(v, k) for k, v in c.items()]))
[(1, 'b'), (10, 'a'), (22, 'c')]
```

List comprehension creates a dynamic list. In this case we make a list of reversed tuples and then sort it.



# Regular Expressions

## Regular Expressions
In computing, a regular expression, also referred to as "regex" or "regexp", provides a consise and flexible means for matching strings of text, such as particular characters, words, or patterns of characters. A regular expression is written in a formal language that can be interpreted by a regular expression processor.

Really clever "wild card" expressions for matching and parsing strings

## Understanding Regular Expressions
* Very powerful and quite cryptic
* Fun once you understand them
* Regular expressions are a language unto themselves
* A langauge of "marker characters" - programming with characters
* It is kind of an "old school" language - compact

## The Regular Expression Module
* Before you can use regular expressions in your program, you must import the library using `import re`
* You can use `re.search()` to see if a string matches a regular expression, similar to using the `find()` method of strings
* You can use `re.findall()` to extract portions of a string that match your regular expression, similar to a combination of `find()` and slicing: `var[5:10]`

## Using re.search() like find()
```Python
# Using find()
hand = open('mbox-short.txt')
for line in hand:
    if line.find('From: ') >= 0:
        print(line)

# Using re.search()
import re

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('From: ', line):
        print(line)
```

## Using re.search() like startswith()
```Python
# Using startswith()
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if line.startswith('From: '):
        print(line)

# Using re.search()
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From: ', line):
        print(line)
```

We fine-tune what is matched by adding special characters to the string

## Wild-card characters
* The dot character matches any character
* If you add the asterisk character, the character is "any number of times"

```
X-Sieve: CME Sieve 2.3
X-DSPAM-Result: Innocent
X-DSPAM-Confidence: 0.8475
X-Content-Type-Message-Body: text/plain
```

`^X.*:` yields the above. 

- `^` matches the start of the line
- `.` matches any character
- `*` many times (of the previous modifier)

Yields find lines that start with `X` followed by any character, many times followed by `:`

## Fine-tuning your match
* Depending on how "clean" your data is and the purpose of your application, you may want to narrow your match down a bit

`X-\S+:` yields: find all lines that start with `X-` followed any non-whitespace character one or more times followed by `:`

## String parsing examples
```Python
>>> data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
>>> atpos = data.find('@')
print(atpos)
21
>>> sppos = data.find(' ', atpos)
print(sppos)
31
>>> host = data[atpos+1:sppos]
>>> print(host)
uct.ac.za
```

Extracting a host name - using find and string slicing

## The double split pattern
Sometimes we split a line one way, and then grab one of the pieces of the line and split that piece again

```Python
# From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

words.line.split() # stephen.marquard@uct.ac.za
email = words[1] # ['stephen.marquard', 'uct.ac.za']
pieces = email.split('@') # 'uct.ac.za'
print(pieces[1])
```

## Regex version

```Python
import re
line = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
y = re.findall('@([^ ]*)', line)
print(y)

['uct.ac.za']

```

`@(c[^ ]*)` yields find all expressions that start with `@` and following that character match any number of non-blank characters 

## Even cooler regex version
```
import re
line = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
y = re.findall('^From .*@([^ ]*)', line)
print(y)
```

## Escape character
* If you want a special regular expression character to just behave normally (most of the time) you just prefix it with `\`

```Python
>>> import re
>>> x = 'We just received $10.00 for cookies.'
>>> y = re.findall('\$[0-9.]+', x)
>>> print(y)
['$10.00']
```

`\$[0-9.]+`
- `\$` A real dollar sign
- `[0-9.]` A digit or period
- `+` At least one or more (need this because it needs to extend to the following numbers)

## Summary
* Regular expressions are a cryptic but powerful language for matching strings and extracting elements from those strings
* Regular expressions have special characters that indicate intent

# Networked Programs
* Quick introduction to how the network works

## Transport Control Protocol (TCP)
* Built on top of IP (Internet Protocol)
* Assumes IP might lose some data - stores and retransmits data if it seems to be lost
* Handles "flow control" using a transmit window
* Provides a nice reliable pipe

## TCP Connections / Sockets

"In computer networking, an internet socket or network socket is an endpoint of a bidirectional inter-process comunication flow across an Internet Protocol-based computer network, such as the internet"

## TCP Port Numbers
* A port is an application-specific or process-specific software communications endpoint
* It allows multiple networked applications to coexist on the same server
* There is a list of well-known TCP port numbers

## Common TCP Ports
* Telnet (23) - Login
* SSH (22) - Secure Login
* HTTP (80)
* etc

## Sockets in Python
* Python has built-in support for TCP Sockets

```Python
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org'), 80) # host, port
```

## Application protocols
* Since TCP (and Python) gives us a reliable socket, what do we want to do with the socket? What problem do we want to solve?
* Application protocols
    * Mail
    * World wide web

## HTTP - Hypertext Transfer Protocol
* The dominant Application Layer Protocol on the Internet
* Invented for the web - to retrieve HTML, Images, Documents, etc
* Extended to be data in addition to documents - RSS, Web Services, etc..
* Basic Concept
    - Make a connection
    - Request a document
    - Retrieve a document
    - Close the connection

## HTTP
* The HyperText Transfer Protocol is the set of rules to allow browsers to retrieve web documents from servers over the internet

## What is a protocol?
* A set of rules that all parties follow so we can predict each other's behaviour
* And not bump into each other
    * On two-way roads in USA, drive on the right-hand side of the road
    * On two-way roads in the UK, drive on the left-hand side of the road

## Getting data from the server
* Each user the clicks on an anchor tag with an href= value to switch to a new page, the browser makes a connection to the web server and issues a "GET" request - to GET the content of the page at the specified URL
* The server returns the HTML document to the browser which formats and displays the document to the user.

## Internet standards
* The standards for all the internet protocols (inner workings) are developed by an organisation
* Internet engineering task force
* www.ietf.org
* Standards are called "RFCs" - "Request for Comments"

## Accurate hacking in the movies
* Matrix Reloaded
* Bourne Ultimatum
* Die Hard 4
* ...

## An HTTP Request in Python
```Python
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
mysock.send(cmd)

while True:
    mysock.recv(512)
    if len(data) < 1:
        break:
    print(data.decode())
mysock.close()
```

Returns headers/metadata and a break between the actual text or content with the headers.

## About characters and strings
* ASCII

## ASCII
* Standardised character set for latin character

## Representing simple strings
* Each character is represented by a number between 0 and 256 stored in 8 bits of memory
* We refer to 8 bits of memory as a "byte" of memory - (i.e. my disk drive contains 3 Terabytes of memory)
* The `ord()` function tells us the numeric value of a simple ASCII character

## Unicode
* Computers can store and understand a much larger character set now

## Multi-Byte Characters
* To represent the wide range of characters computers must handle we represent characters with more than one byte
    * UTF-16 - Fixed length - Two bytes
    * UTF-32 - Fixed length - Four bytes
    * UTF-8 - 1-4 bytes
        * Upwards compatible with ASCII
        * Automatic detection between ASCII and UTF-8
        * UTF-8 is recommended practice for encoding data to be exchanged between systems

## Two kinds of strings in Python
* In Python 3, all strings are Unicode

## Python3 and Unicode
* In Python 3, all strings internally are UNICODE
* Working with string variables in Python programs and reading data from files usually "just works"
* When we talk to a network resource using sockets or talk to a database we have to encode and decode data (usually to UTF-8)

## Python Strings to Bytes
* When we talk to an external resource like a network socket we sends bytes, so we need to encode Python 3 strings into a given character encoding
* When we read data from an external resource, we must decode it based on the character set so it is properly represented in Python 3 as a string
* Encode when send, decode when receiving from network

## Using urllib in Python
* Since HTTP is so common, we have a library that does all the socket work for us and makes web pages look like a file

```Python
import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())
```

* Contains no headers! Use a different method in the library to retrieve the headers

## Like a file...

```Python
import urllib.request, urllib.parse, urllib.error

counts = dict()
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)
```

## Reading web pages
* Will have html tags when retrieved as a text file

## What is web scraping?
* When a program or script pretends to be a browser and retrieves web pages, looks at those web pages, extracts information, and then looks at more web pages
* Search engines scrape web pages - we call this "spidering the web" or "web crawling"

## Why scrape?
* Pull data - particularly social data - who links to who?
* Get your own data back out of some system that has no "export capability"
* Monitor a site for new information
* Spider the web to make a database for a search engine

## Scraping web pages
* There is some controversy about web page scraping and some sites are a bit snippy about it
* Republishing copyrighted information is not allowed
* Violating terms of service is not allowed

## The easy way - Beautiful Soup
* You could do string searches the hard way
* Or use the free software library called Beautiful Soup

## Summary
* Sockets
* Application protocols 
* HTTP is a simple yet powerful protocol
* Python has good support for sockets, HTTP and HTML parsing

# Using Web Services

## Data on the Web
* With the HTTP Request/Response well understood and well supported, there was a natural move toward exchanging data between programs using these protocols
* We needed to come up with an agreed way to represent data going between applications and across networks
* There are two commonly used formats: XML and JSON

## Sending Data across the "Net"
* So many programs, all different langauges
* How do we send standardised protocol for data?
* "Wire protocol" - what we send on the "wire"

## Agreeing on a "Wire Format"
* XML
* JSON

## XML
* Marking up data to send across the network

## eXtensible Markup Language
* Primary purpose is to help information systems share structured data
* It started as a simplified subset of the Standard Generalized Markup Language (SGML) and is designed to be relatively human-legible

## XML Terminology
* Tags indicate the beginning and ending of elements
* Attributes - Keyword/value pairs on the opening tag of XML
* Serialize / De-Serialize - Convert data in one program into a common format that can be stored and/or transmitted between systems in a programming language-independent manner

## XML Basics
* Start tag <person> 
    * name whatever you want
* End tag
* Text content
* Attribute
* Self closing tag

## Whitespace
* Line ends do not matter
* White space is generall discarded on text elements
* We indent only to be readable
    * Sent compacted

## XML "Elements" (or Nodes)
* Simple element
    * Contains data
* Complex element
    * Includes child tags

## XML as a Tree
* Can be thought of as a tree

## XML as Paths
* Can be thought of paths
* Coming up with ways to walk through and parse XML data

## XML Schema
* Describing a "contract" as to what is acceptable XML
* Description of the legal format of an XML document
* Expressed in terms of constraints on the structure and content of documents
* Often used to specify a "contract" between systems - "My system will only XML that conforms to this particular Scheme."
* If a particular piece of XML meets the specification of the Schema - it is said to "validate"

## XSD XML Schema (W3C spec)
* We will focus on the World Wide Web Consortium (W3C) version
* It is often called "W3C" because "Schema" is considered generic
* More commonly it is called XSD because the file names end in .xsd

## XSD Structure
* xs:element
* xs:sequence
* xs:complexType

## JavaScript Object Notation
* Douglas Crockford - "Discovered" JSON
* Object literal notation in JavaScript
* JSON represents data as nested "lists" and "dictionaries"

## Service Oriented Approach
* Most non-trivial web applications use services
* They use services from other applications
    * Credit Card Charge
    * Hotel Reservation systems
* Services publish the "rules" applications must follow to make use of the service (API)

## Multiple Systems
* Initially - two systems cooperate and split the problem 
* As the data/service becomes useful - multiple applications want to use the information / application

# Web Services

## Application Program Interface
The API itself is largely abstract in that it specifies an interface and controls the behaviour of the objects specified in that interface. The softwarte that provides the functionality described by an API is said to be an "implementation" of the API. An API is typically defined in terms of the programming language used to build an application.

## API Security and Rate Limiting
* The compute resources to run these APIs are not "free"
* The data provided by these APIs is usually valuable
* The data providers might limit the number of requests per day, demand an API "key", or even charge for usage
* They might change the rules as things progress...



# Python Objects

## Warning
* This lecture is very much about definitions and mechanics for objects
* This lecture is a lot more about "how it works" and less about "how you use it"
* You won't get the entire picture until this is all looked at in the context of a real problem
* So please suspend disbelief and learn technique for the next 50 or so slides..

## Review of Programs
* Input, process and output
* Series of steps

## Object Oriented
* A program is made up of many cooperating objects
* Instead of being the "whole program" - each object is a little "island" within the program and cooperatively working with other objects
* A program is made up of one or more objects working together - objects make use of each other's capabilities

## Object
* An object is a bit of self-contained Code and Data
* A key aspect of the Object approach is to break the problem into smaller understandable parts (divide and conquer)
* Objects have boundaries that allow us to ignore un-needed detail
* We have been using objects all along:
    - String Objects
    - Integer Objects
    - Dictionary Objects
    - List Objects

* Program has some input
* Data moves between objects
* Data/code has their own boundaries
* Don't have to worry about the inside eg. lists and dictionaries

## Definitions
* Class - a template - Dog
* Method or Message - A defined capability of a class
* Field or attribute - A bit of data in a class - length
* Object or Instance - A particular instance of a class - Lassie


## Terminology: Class
A pattern (exemplar) of a class. The class of Dog defines all possible dogs by listing the characteristics and behaviours they can have; the object Lassie is one particular dog, with particular versions of the characteristics. A Dog has fur; Lassie has brown-and-white fur.

## Terminology: Instance
One can have an instance of a class or a particular object. The instance is the actual object created at runtime. In programmer jargon, the Lassie object is an instance of the dog class. The set of values of the attributes of a particular object is called its state. The object consists of state and behaviour that's defined in the object's class.

**Object and instance are often used interchangeably**

## Terminology: Method
An object's abilities. In language, methods are verbs. Lassie, being a Dog, has the ability to bark. So bark() is one of Lassie's methods. She may have other methods as well, for example sit() or eat() or walk() or save_timmy(). Within the program, using a method usually affects only one particular object; all Dogs can bark, but you need only one particular dog to do the barking.

## A sample class
`class` is a reserved word  

```Python
class PartyAnimal: # This is the template for making PartyAnimal objects
    x = 0 # Each PartyAnimal object has a bit of data.

    def party(self):
        self.x = self.x + 1
        print("so far", self.x)

an = PartAnimal() # Construct a PartyAnimal object and store in `an`
an.party()
# So far 1
an.party()
# So far 2
an.party()
# So far 3
```

## Playing with dir() and type()
* The `dir()` command lists capabilities
* Ignore the ones with underscores - these are used by Python itself
* The rest are real operations that the object can perform
* It is like type() - it tells us something *about* a variable

## Try dir() with a String
* We see all the string methods and the underscore methods
* We can use dir() to find the capabilities of our newly created class

## Object Lifecycle
* Objects are created, used and discarded
* We have special blocks of code (methods) that get called
    * At the moment of creation (constructor)
    * At the moment of destruction (destructor)
* Constructors are used a lot
* Destructors are seldom used

```Python
class PartyAnimal:
    x = 0

    def __init__(self):
        print('I am constructed')

    def party(self):
        self.x += 1
        print('So far', self.x)

    def __del__(self):
        print('I am destructed', self.x)

an = PartyAnimal()
# I am constructed
an.party()
# So far 1
an.party()
# So far 2
an = 42 
# I am destructed 2

print('an contains', an)
```

Constructor and destructor are optional

Constructors can have additional parameters. These can be used to set up instance variables for the particular instance of the class (i.e. for the particular object)

## Many instances
* We can create lots of objects - the class is the template for the object
* We can store each distinct object in its own variable
* We call this having multiple instances of the same class
* Each instance has its own copy of the instance variables


## Inheritance
* When we make a new class - we can reuse an existing class and inherit all the capabilities of an existing class and then add our own little bit to make our new class
* Another form of store and reuse
* Write once - reuse many times
* The new class (child) has all the capabilities of the old class (parent) - and then some more

## Terminology: Inheritance
'Subclasses' are more specialised versions of a class, which inherit attributes and behaviours from their parent classes, and can introduce their own.

## Definitions
* Class
    - A template
* Attribute
    - A variable within a class
* Method
    - A function within a class
* Object
    - A particular instance of a class
* Constructor
    - Code that runs when an object is created
* Inheritance
    - The ability to extend a class to make a new class


## Summary
* Object oriented programming is a very structured approach to code reuse
* We can group data and functionality together and create many independent instances of a class

# Relational Databases and SQLite

## Random access
* When you can randomly access data..
* How can you layout data to be most efficient?
* Sorting might not be the best idea

## Relational databases
Relational databases model data by storing rows and columns in tables. The power of the relational database lies in its ability to efficiently retrieve data from those tables and in particular where there are multiples and the relationships between those tables involved in the query.  

## Terminology
* Database - contains many tables 
* Relation (or table) - contains tuples and attributes
* Tuple (or row) - a set of fields that generally represents an "object" like a person or a music track
* Attribute (also column or field) - one of possibly many elements of data corresponding to the object represented by the row

## SQL
* Structured Query Language is the language we use to issue commands to the database
    * Create a table
    * Retrieve some data
    * Insert data
    * Delete data

## Web Applications w/ Databases
* Application Developer - Builds the logic for the application, the look and feel of the application - monitors the application for problems
* Database Administrator - Monitors and adjusts the database as the program runs in production
* Often both people participate in the building of the "Data model"

## Database Administrator
A database administrator (DBA) is a person responsible for the design, implemenetation, maintenance, and repair of an organisation's database. The role includes the development and design of database strategies, monitoring and improving database performance and capacity, and planning for future expansion requirements. They may also plan, coordinate, and implement security measures to safeguard the database.

## Database Model
* A database model or database schema is the structure or format of a database, described in a formal language supported by the database management system. In other words, a "database model" is  the application of a data model when used in conjunction with a database management system.

## Common Database Systems
* Three major Database Management Systems in wide use
    * Oracle - Large, commercial, enterprise-scale, very very tweakable
    * MySQL - Simpler but very fast and scalable - commercial open source
    * SQLServer - Very nice - from Microsoft (also Access)
* Many other smaller projects, free and open source
    * HSQL, SQLite, Postgres, MariaDB

## SQLite Browser
* SQLite is a very popular database - it is a free and fast and small
* SQLite Browser allows us to directly manipulate SQLite files
* SQLite is embedded in Python and a number of other languages

## Let's make a database!

## SQL: Insert
* The insert statement inserts a row into a table

```SQL
INSERT INTO Users (name, email) VALUES ('Kristin', 'kf@umich.edu')
```

## SQL: Delete
* Deletes a row in a table based on a selection criteria

```SQL
DELETE FROM Users WHERE email='ted@umich.edu'
```

## SQL: Update
* Allows the updating of a field with a where clause

```SQL
UPDATE Users SET name='Charles' WHERE email='csev@umich.edu'
```

## Retrieving Records: Select
* The select statement retrieves a group of records - you can either retrieve all the records or a subset of the records with a WHERE clause

```SQL
SELECT * FROM Users

SELECT * FROM Users WHERE email='csev@umich.edu'
```

## Sorting with ORDER BY
* You can add an ORDER BY clause to SELECT statements to get the results sorted in ascending or descending order

```SQL
SELECT * FROM Users ORDER BY email

SELECT * FROM Users ORDER BY name DESC
```

## This is not too exciting (so far)
* Tables pretty much look like big fast programmable spreadsheets with rows, columns, and commands
* The power comes when we have more than one table and we can exploit the relationships between the tables

## Complex Data Models and Relationships
* Next lesson

## Database Design
* Database design in an art form of its own with particular skills and experience
* Our goal is to avoid the really bad mistakes and design clean and easily understood databases
* Others may performance tune things later
* Database design starts with a picture...

## Building a data model
* Drawing a picture of the data objects for our application and then figuring out how to represent the objects and their relationships
* Basic Rule: Don't put the same string data in twice - use a relationship instead
* When there is one thing in the "real world" there should be one copy of that thing in the database

## For each "piece of info"
* Is the column an object or an attribute of another object?
* Once we define objects, we need to define the relationships between objects

## Representing Relationships in a Database
* Foreign keys

## Relational Power
* By removing the replicated data and replacing data and replacing it with references to a single copy of each but of data we build a "web" of information that the relational database can read through very quickly - even for very large amounts of data
* Often when you want some data it comes from a number of tables linked by these foreign keys

## The JOIN Operation 
* The JOIN operation links across several tables as part of a select operation
* You must tell the JOIN how to use the keys that make the connection between the tables using an ON clause

## Many-to-many to Relationships
* Sometimes we need to model a relationship that is many-to-many
* We need to add a "connection" table with two foreign keys
* There is usually no seperate primary key

## Complexity enables speed
* Complexity makes speed possible and allows you to get very fast results as the data size grows
* By normalising the data and linking it with integer keys, the overall amount of data which the relational database must scan is far lower than if the data were simply flattened out
* It might seem like a tradeoff - spend some time designing your database os it continues to be fast when your application is a success

## Additional SQL Topics 
* Indexes improve access performance for things like string fields
* Constraints on data - (cannot be NULL, etc..)
* Transactions - allow SQL operations to be grouped and done as a unit

## Summary
* Relational databases allow us to scale to very large amounts of data
* The key is to have one copy of any data element and use relations and joins to link the data to multiple
* This greatly reduces the amount of data which must be scanned when doing complex operations across large amounts of data
* Database and SQL design is a bit of an art form

# Retrieving and visualising data

## Multi-step data analysis
* Bring everything together
* Use two databases
    * Collect raw data
    * Clean and store data

## Many data mining technologies
* Hadoop
* Spark
* Redshift

## "Personal Data Mining"
* Our goal is to make you better programmers - not to make you data mining experts

## GeoData
* Makes a Google Map from user entered data
* Uses the Google Geodata API
* Caches data in a database to avoid rate limiting and allow restarting
* Visualised in a browser using the Google Maps API

## Page Rank
* Write a simple web page crawler
* Compute a simple version of Google's Page Rank algorithm
* Visualise the resulting network

## Web crawler
* A web crawler is a computer program that browses the world wide web in a methodical, automated manner. Web crawlers are mainly used to create a copy of all the visited pages for later processing by a search enginer that will index the downloaded pages to provide fast searches.

## Process
* Retrieve a page
* Look through the page for links
* Add the links to a list of "to be retrieved" sites
* Repear...

## Web crawling policy
* A selection policy that states which pages to download
* A re-visit policy that states when to check for changes to the pages
* A politeness policy that states how to avoid overloading websites
* A parallelisation policy that states how to coordinate distributed web crawlers

## robots.txt
* A way for a web site to communicate with web crawlers
* An informal and voluntary standard
* Sometimes folks make a "Spider Trap" to catch "bad" spiders

## Google Architecture
* Web crawling
* Index Building
* Searching

## Search Indexing
Search engine indexing collects, parses and stores data to facilitate fast and accurate information retrieval. The purpose of storing an index is to optimise speed and performance in finding relevant documents for a search query. Without an index, the search engine would scan every document in the corpus, which would require considerable time and computing power.

## Mailing Lists - Gmane
* Crawl the archive of a mailing list
* Do some analysis/cleanup
* Visualise the data as word cloud and lines

## Warning: This dataset is > 1GB
* Do not point this application at gmane.org and let it run
* There is no rate limits - these are cool folks
* Use dr-chucks version
* `http://mbox.dr-chuck.net/sakai.devel/4/5`


