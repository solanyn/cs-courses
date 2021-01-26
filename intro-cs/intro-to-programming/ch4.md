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


