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
