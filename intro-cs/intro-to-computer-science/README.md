<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Introduction to Computer Science](#introduction-to-computer-science)
- [L1: What is Computation](#l1-what-is-computation)
- [L2: Branching and Iteration](#l2-branching-and-iteration)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# Introduction to Computer Science

OSSU recommends the **MIT 6.0001 - Introduction to Computer Science and Programming in Python course** available here:

https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/

# L1: What is Computation

* Tips for the course
    * Read problem sets before
    * Write the lecture code in class

* Topics for the course
    * Represent knowledge with data structures
    * Iteration and recursion as computational metaphors
    * Abstraction of procedures and data types
    * Organise and modularise systems using object classes and methods
    * Different classes of algorithms, searching and sorting
    * Complexity of algorithms

* What does a computer do?
    * Fundamentally:
        * Performs **calculations** a billion calculations per seconds
        * **Remembers** results: 100s of gigabytes of storage
    * What kinds of calculations?:
        * Built-in to the language
        * Ones that you **define** as the programmer
    * Computers only do what you tell them
        * Computers don't know anything!

* Types of knowledge
    * **Declarative knowledge** is statements of fact
    * **Imperative knowledge** is a recipe or "how-to"

* A numerical example
    * Square root of a number `x` is `y` such that `y*y = x`
    * Recipe for deducing square root of a number `x` (16)
        1) Start with a **guess**, `g`
        2) If `g*g` is **close enough** to `x`, stop and say `g` is the answer
        3) Otherwise make a `new guess` by averaging `g` and `x/g`
        4) Using the new guess, **repeat** process until close enough

* What is a recipe?
    1) Sequence of simple **steps**
    2) **Flow of control** process that specifies when each step is executed
    3) A means of determingin **when to stop**

    * 1 + 2 + 3 = an **algorithm**!

* Computers are machines
    * How to capture a recipe in a mechanical process
    * **Fixed program** computer
        * Calculator
    * Stored program computer
        * Machine stores and executes instructions

* Basic machine architecture
    * Memory (data)
    * Input and output
    * ALU - arithmetic logic unit (do primitive operations)
    * Control unit - program counter

* Stored program computer
    * Sequence of **instructions store** inside computer
        * Built from predifined set of primitive instructions
            1) Arithmetic and logic
            2) Simple tests
            3) Moving data
        * Special program (interpreter) **executes each instruction in order**
            * Use tests to change flow of control through sequence
            * Stop when done

* Basic primitives
    * Turing showed that you can **compute anything** using 6 primitives
        * Move left
        * Move right
        * Read
        * Write 
        * Scan
        * Do nothing

    * Modern programming languages have more convenient set of primitives
    * Can abstract methods to **create new primitives**

    * Anything computable in one language is computable in any other programming language

* Creating recipes
    * A programming language provides a set of primitive **operations**
    * **Expressions** are complex but legal combinations of primitives in a programming language
    * Expressions and computation have **values** and meanings in a programming language

* Aspects of languages
    * **Primitive constructs**
        * English: words
        * Programming language: numbers, strings, simple operators

    * **Static semantics** is which syntactically valid strings have meaning
        * English: `"I are hungry"` -> Syntactically valid but static semantic error
        * Programming language: `3.2*5` -> Syntactically valid
                                `3 + "hi"` -> Static semantic error

    * Semantics is the meaning associated with a syntactically correct string of symbols with no static semantic errors
        * English: can have many meanings `"Flying planes can be dangerous"`
        * Programming languages: have only one meaning but may not be what programmer intended

* Where things go wrong
    * **Syntactic errors**
        * Common and easily caught
    * **Static semantic errors**
        * Some languages check for these before running program
        * Can cause unpredictable behaviour
    * No semantic error but **different meaning than what programmer intended**
        * Program crashes, stops running
        * Program runs forever
        * Program gives an answer but different than expected

* Python programs
    * A program is a sequence of definitions and commands
        * Definitions evaluated
        * Commands executed by Python interpreter in a shell
    * Commands (statements) instruct interpreter to do something
    * Can be typed directly in a shell or stored ina file that is read into the shell and evaluated
        * Problem Set 0 will introduce you to these in Anaconda

* Objects
    * Programs manipulate **data objects**
    * Objects have a **type** that defines the kinds of things programs can do to them
        * Ana is a human so she can walk, speak English, etc.
        * Chewbacca is a wookie so he can walk, "MWAAAARHRHRHRH"
    * Objects are
        * Scalar (cannot be subdivided)
        * Non-scalar (have internal structure that can be accessed)

* Scalar objects
    * `int` - represent integers
    * `float` - represent real numbers
    * `bool` - represent Boolean values `True` and `False`
    * `NoneType` - special and has one value, `None`
    * can use `type()` to see the type of an object

* Type conversions (cast)
    * Can **convert object of one type to another**
    * `float(3)` converts integer `3` to float `3.0`
    * `int(3.9)` trucates float `3.9` to integer `3`
        * Gets truncated, not rounded

* Printing to console
    * To show output from code to a user use `print` command

* Expressions
    * Combine objects and operators to form expressions
    * An expression has a value, which has a type
    * Syntax for a simple expression - `<object> <operator> <object>`
    
* Operators on ints and floats
    * `i+j` -> the **sum**
    * `i-j` -> the **difference**
    * `i*j` -> the **product**
    * `i/j` -> division

    * `i%j` -> the **remainder** when `i` is divided by `j`
    * `i**j` -> `i` to the **power** of `j`

* Binding variables and values
    * Equal sign is an **assignment** of a value to a variable name
    * `pi = 3.13159`
    * `pi_approx = 22/7`
    * Value is stored in computer memory
    * Retrieve value associated with name or variable by invoking the name, by typing `pi`

* Abstracting expressions
    * Why give names to values of expressions?
    * To reuse names instead of values
    * Easier to change code later
    ```Python
    pi = 3.14159
    radius = 2.2
    area = pi*(radius*82)
    ```
        

* Programming vs math
    * In programming, you do not "solve for x"
    * An assignment is:
        * Expression on the right, evaluated to a value
        * Variable name on the left

* Changing bindings
    * Can **re-bind** variables names using new assignment statements
    * A previous value may still be stored in memory but lost the handle for it
    * Value for area does not change until you tell the computer to do the calculation again

    ```Python
    pi = 3.14159
    radius = 2.2
    area = pi*(radius*82)
    radius = radius + 1
    ```

# L2: Branching and Iteration

* Strings
    * Letters, special characters, spaces, digits
    * Enclose in **quotation marks or single quotes**
    * **Concatenate** strings
    ```Python
    hi = "hello there"

    name = "ana"

    greet = hi + name

    greeting = hi + " " + name
    ```
    * do some **operations** on a string as defined in Python docs
        * `silly = hi + " " + name * 3`

* Input/Output: `input("")`
    * Prints whatever is in the quotes
    * User types in something and hits enter
    * Binds that value to a variable
    ```Python
    text = input("Type anything... ")
    print(5*text)
    ```
    * `input` **gives you a string** so must cast if working with numbers
    ```Python
    num = int(input("Type a number... "))
    print(5 * num)
    ```

* Comparison operators on `int`, `float`, `string`
    * `i` and `j` are variable names
    * comparisons below evaluate to a boolean
    ```Python
    i > j
    i >= j
    i < j
    i <= j
    i == j # equality test, True if i is the same as j
    i != j # inequality test, True if i not the same as j
    ```
* Logic operators on bools
    * `a` and `b` are variable names (with Boolean values)
    ```Python
    not a # True if a is False
          # False if a is True
    a and b # True if both are True
    a or b # True if either or both are True
    ```

* Control flow - Branching
    * `<condition>` has a value `True` or `False`
    * Evaluate expressions in that block if `<condition>` is `True`

    ```Python
    if <condition>:
        <expression>
        <expression>
        ...
    ```

    ```Python
    if <condition>:
        ...
    else:
        <expression>
        <expression>
        ...
    ```
    
    ```Python
    if <condition>:
        ...
    elif <condition>:
        <expression>
        <expression>
        ...
    else:
        ...
    ```

* Indentation
    * Matters in Python
    * How you denote blocks of code
    ```Python
    x = float(input("Enter a number for x: "))
    y = float(input("Enter a number for y: "))
    if x == y:
        print("x and y are equal")
        if y != 0:
            print("therefore, x / y is", x/y)
    elif x < y:
        print("x is smaller")
    else:
        print("y is smaller")
    print("thanks!")
    ```

* Legend of Zelda - Lost Woods
    * Keep going right, takes you back to this same screen, stuck in a loop
    * Instead of infinite amount of if statements
    * We use a while loop

* Control flow: `while` loops
```Python
while <condition>:
    <expression>
    <expression>
    ...
```

    * <condition> evaluates to a Boolean
    * If <condition>  is True, do all the steps inside the while code block
    * Check <condition> again
    * Repeat until <condition> is False

* `while` loop example
```Python
n = input("You're in the Lost Forest. Go left or right? ")
while n == "right":
    n = input("You're in the Lost Forest. Go left or right? ")
print("You got out of the Lost Forest!")
```

* Control flow: `while` and `for` loops
    * Iterate through numbers in a sequence

```Python
# More complicated with while loop
n = 0
while n < 5:
    print(n)
    n = n+1

# Shortcut with for loop
for n in range(5):
    print(n)
```

* Control flow: `for` loops
```Python
for <variable> in range(<some_num>):
    <expression>
    ...
```

    * Each time through the loop, `<variable>` takes a value
    * First time, `<variable>` starts at the smallest value
    * Next time, `<variable>` gets the prev value + 1
    * etc.

* `range(start, stop, step)`
    * Default values are `start = 0` and `step = 1` and optional
    * Loop until value is `stop - 1`
    
    ```Python
    mysum = 0
    for i in range(7, 10):
        mysum += i
    print(mysum)

    mysum = 0
    for i in range(5, 11, 2):
        mysum += i
    print(mysum)
    ```

* `break` statement
    * Immediately exits whatever loop it is in
    * Skips remaining expressions in code block
    * Exits only innermost loop!

    ```Python
    while cond1:
        while cond2:
            expression_a
            break
            expression_b # Does not get evaluated
        # To here
        expression_c
    ```

* `for` vs `while` loops
    * For loops
        * **Know** number of iterations
        * Can **end early** via `break`
        * Uses a **counter**
        * **Can rewrite** a `for` loop using a `while` loop

    * While loops
        * **Unbounded** number of iterations
        * Can **end early** via `break`
        * Can use a **counter but must initialise** before loop and increment it inside loop
        * **May not be able to rewrite a `while` loop using a `for` loop

# L3: String manipulation, guess-and-check, approximations, bisection
* Strings
    * Think of as a **sequence** of case sensitive characters
    * Can compare strings with ==, >, < etc.
    * `len()` is a function used to retrieve the **length** of the string in the parentheses
    ```Python
    s = "abc"
    len(s) # Evaluates to 3
    ```

    * Square brackets used to perform **indexing** into a string to get the value at a certain index/position
    ```Python
    s = "abc"
       # 012 <- indexing always starts at 0

    s[0] # evaluates to "a"
    s[1] # evaluates to "b"
    s[2] # evaluates to "c"
    s[3] # trying to index out of bounds, error
    s[-1] # evaluates to "c"
    s[-2] # evaluates to "b"
    s[-3] # evaluates to "a"
    ```

    * Can slice strings using `[start:stop:step]`
    * If given two numbers, `[start:stop], step=1` by default
    * You can also omit number and leave just colons

    ```Python
    s = "abcdefgh"
    s[3:6] # evaluates to "def", same as s[3:6:1]
    s[3:6:2] # evaluates to "df"
    s[::] # evaluates to "abcdefgh", same as s[0:len(s):1]
    s[::-1] # evaluates to "hgfedcba" same as s[-1:(len(s)+1):-1]
    s[4:1:-2] # evaluates to "ec"
    ```

    * Strings are "**immutable**" - cannot be modified
    ```Python
    s = "hello"
    s[0] = 'y' # gives an error
    s = 'y'+s[1:len(s)] # is allowed, s bound to new object
    ```

* `for` loops recap
    * `for` loops have a **loop variable** that iterates over a set of values
    ```Python
    for var in range(4): # var iterates over values 0,1,2,3
        <expressions> # expressions inside loop executed with each value for var

    for var in range(4, 6): # var iterates over values 4,5
        <expressions>
    ```
    * `range` is a way to iterate over numbers, but a for loop variable can **iterate over any set of values**, not just numbers!

* Strings and loops
    * These do code snippets do the same thing
    * Bottom one is more "pythonic"
    ```Python
    s = "abcdefgh"
    for index in range(len(s)):
        if s[index] == 'i' or s[index] == 'u':
            print("There is an i or u")

    for char in s:
        if char == 'i' or char == 'u':
            print("There is an i or u")
    ```

* Code example: robot cheerleaders
    * Using a while loop
    ```Python
    an_letters = "aefilmorsxAEFHILMNORSX"

    word = input("I will cheer for you! Enter a word: ")
    times = int(input("Enthusiasm level (1-10): "))

    i = 0
    while i < len(word):
        char = word[i]
        if char in an_letters:
            print("Give me an " + char + "! " + char)
        else:
            print("Give me an " + char + "! " + char)
        i += 1
    print("What does that spell?")
    for i in range(times):
        print(word, "!!!")
    ```

    * Using a for loop
    ```Python
    an_letters = "aefilmorsxAEFHILMNORSX"

    word = input("I will cheer for you! Enter a word: ")
    times = int(input("Enthusiasm level (1-10): "))

    for char in word:
        if char in an_letters:
            print("Give me an " + char + "! " + char)
        else:
            print("Give me an " + char + "! " + char)
        i += 1
    print("What does that spell?")
    for _ in range(times):
        print(word, "!!!")
    ```

* Guess-and-check - cube root
```Python
cube = 8
for guess in range(abs(cube)+1):
    if guess**3 >= abs(cube):
        break:

if guess**3 != abs(cube):
    print(cube, 'is not a perfect cube')
else:
    if cube < 0:
        guess = -guess
    print('Cube root of '+str(cube)+' is '+str(guess))
```

* Approximate solutions
    * **Good enough** solution
    * Start with a guess and increment by some **small value**
    * Keep guessing if `|guess**3-cube| >= epsilon` for some **small epsilon**
    * Decreasing increment size -> slower program
    * Increasing epsilon -> less accurate answer

* Approximate solution - cube root

```Python
cube = 27
epsilon = 0.01
guess = 0.0
increment = 0.0001
num_guesses = 0
while abs(guess**3 - cube) >= epsilon and guess <= cube:
    guess += increment
    num_guesses += 1
print('num_guesses =', num_guesses)
if abs(guess**3 - cube) >= epsilon:
    print('Failed on cube root of', cube)
else:
    print(guess, 'is close to the cube root of', cube)
```
    * If cube is 10000, then we enter infinite loop (without second while condition)
    * Add check for less than cube

* Bisection search
    * Half interval each iteration
    * New guess is halfway in between

* Bisection search - cube root
```Python
cube = 27
epsilon = 0.01
num_guesses = 0
low = 0
high = cube
guess = (high + low)/2.0
while abs(guess**3 - cube) >= epsilon:
    if guess**3 < cube:
        low = guess
    else:
        high = guess
    guess = (high + low)/2.0
    num_guesses += 1
print('num_guesses =', num_guesses)
print(guess, 'is close to the cube root of', cube)
```

* Bisection search convergence
    * Search space
        * First guess: n/2
        * second guess: n/4
        * kth guess: n/2^k
    * Guess converges on the order of log2N steps
    * Bisection search works when value of function varies monotonically with input
    * Code as shown only works for positive cubes > 1 - why?
    * Challenges 
        * Modify to work with negative cubes! 
        * Modify to work with x < 1! Interval needs to be larger. 
            * Add if statement to expand interval to 0-1 if cube is between 0 and 1.

# L4: Decomposition, Abstration and Functions
    * How do we write code?
        * So far...
            * Covered language mechanisms
            * Know how to write different files for each computation
            * Each file is some piece of code
            * Each code is a sequence of instructions
        * Problems with this approach
            * Easy for small-scale problems
            * Messy for larger problems
            * Hard to keep track of details
            * How do you know the right info is supplied to the right part of the code
    * Good programming
        * More code not necessarily a good thing
        * Measure good programmers by the amount of functionality
        * Introduce **functions**
        * Mechanism to achieve **decomposition** and **abstraction**

    * Example - Projector
        * A projector is a black box
        * Don't know how it works
        * Know the interface: input/output
        * Connect any electronic to it that can communicate with that input
        * Black box somehow converts image from input source to a wall, magnifying it
        * **Abstraction idea** do not need to know how projector works to use it

    * Example - Projector
        * Projecting large image of Olympics decomposed into separate tasks for separate projectors
        * Each projector takes input and produces separate output
        * All projectors work together to produce larger image
        * **Decomposition idea**: different devices work together to achieve an end goal

    * Create structure with decomposition
        * In projector example, separate devices
        * In programming, divide code into **modules**
            * Are self-contained
            * Used to break up code
            * Intended to be reusable
            * Keep code organised
            * Keep code coherent
        * This lecture, achieve decomposition with **functions**
        * In a few weeks, achieve decomposition with **classes**

    * Suppress details with abstraction
        * In projector example, instructions for how to use it are sufficient, no need to know how to build one
        * In programming, think of a piece of code as a **black box**
            * Cannot see details
            * Do not need to see details
            * Do not want to see details
            * Hide tedious coding details
        * Achieve abstraction with **function specifications** or **docstrings**

    * Functions
        * Write reusable pieces/chunks of code, called **functions**
        * Functions are not run in a program until they are "**called**" or "**invoked**" in a program
        * Function characteristics:
            * Has a **name**
            * Has **parameters** (0 or more)
            * Has a **docstring** (optional but recommended)
            * Has a **body**
            * **Returns** something

    * How to write and call/invoke a function
    ```Python
    def is_even(i):
        """
        Input: i, a positive int
        Returns True if i is even, otherwise False
        """
        print("inside is_even")
        return i%2 == 0

    is_even(3)
    ```

    * Variable scope
        * **Formal parameter** gets bound to the value of **actual parameter** when function is called
        * New **scope/frame/environment** created when enter a function
        * **Scope** is mapping of names to objects

    * One warning if no `return` statement
        * Python returns the value **None, if no `return` given**
        * Represents absence of a value

    * Functions as arguments
        * Arguments can take on any type, even functions
    ```Python
    def func_a():
        print('inside func_a')

    def func_b(y):
        print('inside func_b')
        return y

    def func_c(z):
        print('inside func_c')
        return z()

    print(func_a())
    # None
    print(5 + func_b(2))
    # 7
    print(func_c(func_a))
    # None calls func_a
    ```

    * Scope example
        * Inside a function, **can access** a variable defined outside
        * Inside a function, **cannot modify** a variable defined outside -- can using **global variables**, but frowned upon

    ```Python
    def f(y):
        x = 1
        x += 1
        print(x)

    x = 5
    f(x)
    print(x)

    def g(y):
        print(x)
        print(x + 1)

    x = 5
    g(x)
    print(x)

    def h(x):
        x += 1

    x = 5
    h(x)
    print(x)
    # Assignment error
    ```

    * Harder scope example
        * Python Tutor is a cool tool to see how scope works

    ```Python
    def g(x):
        def h():
            x = 'abc' 
        x = x + 1
        print('g: x =', x)
        h() 
        return x

    x = 3
    z = g(x) # z = 4
    ```

# L5: Tuples, Lists, Aliasing, Mutability and Cloning
    * Tuples
        * An ordered sequence of elements, can mix element types
        * Cannot change element values, **immutable** (like strings!)
        * Represented with parentheses

    ```Python
    te = ()
    t = (2, "mit", 3)
    t[0] # 2
    (2, "mit", 3) + (5, 6) # (2, "mit", 3, 5, 6)
    t[1:2] # Slice tuple, evaluates to ("mit",)
    t[1:3] # Slice tuple, evaluates to ("mit",3)
    len(t) # 3
    t[1] = 4 # Gives error, can't modify object
    ```

        * Conveniently used to swap variable values
        ```Python
        # Doesn't work
        x = y
        y = x

        # Works
        temp = x
        x = y
        y = temp

        # Simultaneous assignment
        (x, y) = (y, x)
        ```
        * Used to **return more than one value** from a function
        ```Python
        def quotient_and_remainder(x, y):
            q = x // y
            r = x % y
            return (q, r)

        (quot, rem) = quotient_and_remainder(4,5)
        ```
    * Manipulating tuples
        * Can **iterate** over tuples
        ```Python
        def get_data(aTuple):
            nums = ()
            words = ()
            for t in aTuple:
                nums = nums + (t[0], )
                if t[1] not in words:
                    words = words + (t[1], )
            min_n = min(nums)
            max_n = max(nums)
            unique_words = len(words)
            return (min_n, max_n, unique_words)
        ```

    * Lists
        * **Ordered sequence** of information, accessible by index
        * A list is denoted by **square brackets**, []
        * A list contains **elements**
            * Usually homogenous (ie, all integers)
            * Can contain mixed types (not common)
        * list elements can be changed so a list is **mutable**

    * Indices and ordering
    ```Python
    a_list = []
    L = [2, 'a', 4, [1,2]]
    len(L)
    # 4
    L[0]
    # 2
    L[2] + 1
    # 5
    L[3]
    # [1,2]
    L[4]
    # Error
    i = 2
    L[i-2]
    # 'a'
    ```

    * Changing elements
        * Lists are **mutable**
        * Assigning to an element at an index changes the value

        ```Python
        L = [2, 1, 3]
        L[1] = 5
        ```
        * L is now `[2, 5, 4]`, note that this is the **same object**

    * Iterating over a list
        * Compute the **sum of elements** of a list
        * Common pattern, iterate over list elements
        ```Python
        total = 0
        for i in range(len(L)):
            total += L[i]

        print(total)

        total = 0
        for i in L:
            total += i
        print(total)
        ```
        * Notice:
            * List elements are indexed `0` to `len(L) - 1`
            * `range(n)` goes from `0` to `n-1`
        
    * Operations on lists - add
        * **Add** elements to end of list with `L.append(element)`
        * **Mutates** the list!
        ```Python
        L = [2,1,3]
        L.append(5)
        # [2, 1, 3, 5]
        ```
        * What is the dot?
            * Lists are Python objects, everything in Python is an object
            * Objects have data
            * Objects have methods and functions
            * Access this information by `object_name.do_something()`
            * Will learn more about these later

        * To combine lists together use **concatenation**, + operator, to give you a new list
        * **Mutate** list with `L.extend(some_list)`

        ```Python
        L1 = [2,1,3]
        L2 = [4,5,6]
        L3 = L1 + L2
        # L3 is [2,1,3,4,5,6] L1, L2 unchanged!
        L1.extend([0,6])
        # L1 mutated to [2,1,3,0,6]
        ```

    * Operations on lists - remove
        * Delete element at a **specific index** with `del(L[index])`
        * Remove element at **end of list** with `L.pop()`, returns the removed element
        * Remove a **specific element** with `L.remove(element)`
            * Looks for the element and removes it
            * If element occurs multiple times, removes first occurrence
            * If element not in list, gives an error
        ```Python
        L = [2, 1, 3, 6, 3, 7, 0]
        L.remove(2)
        # Mutates L = [1,3,6,3,7,0]
        L.remove(3)
        # Mutates L = [1,6,3,7,0]
        del(L[1])
        # Mutates L = [1,3,7,0]
        L.pop()
        # Returns 0 and mutates L = [1,3,7]
        ```

    * Convert lists to strings and back
        * Convert **string to list** with `list(s)`, returns a list with every character from `s` an element in `L`
        * Can use `s.split()`, to **split a string on a character** parameter, splits on spaces if called without a parameter
        * Use `''.join(L)` to turn a **list of characters into a string**, can give a character in quotes to add char between every element
        ```Python
        s = "I<3 cs"
        # s is a string
        list(s)
        # returns ['I', '<', '3', ' ', 'c', 's']
        s.split('<')
        # returns ['I', '3 cs']
        L = ['a', 'b', c']
        ''.join(L)
        # 'abc'
        '_'.join(L)
        # 'a_b_c'
        ```
    * Other list operations
        * `sort()` and `sorted()`
        * `reverse()`
        * and many more (check docs!)
        ```Python
        L = [9,6,0,3]
        sorted(L)
        # Returns sorted list, L not mutated
        L.sort()
        # Mutates L = [0, 3, 6, 9]
        L.reverse()
        # Mutates L = [9,6,3,0]
        ```

    * Mutation, aliasing, cloning
    * Lists in memory
        * Lists are **mutable**
        * Behave differently than immutable types
        * Is an object in memory
        * Variable name points to object
        * Any variable points to object
        * Any variable pointing to that object is affected
        * Key phrase to keep in mind when working with lists is **side effects**

    * An analogy
        * Attributes of a person
            * Singer, rice
        * He is known by many names
        * All nicknames point to the **same person**
            * Add new attribute to **one nickname**
            * ... **all his nicknames** refer to old attributes AND all new ones
    * Aliases
        * `hot` is an **alias** for `warm` - changing one changes the other!
        * `append()` has a side effect

    * Cloning a list
        * Create a new list and **copy every element** using `chill = cool[:]`

    * Sorting lists
        * Calling `sort()` **mutates** the list, returns nothing
        * Calling `sorted()` **does not mutate** lsit, must assign result to a variable

    * Lists of lists of lists of....
        * Can have **nested** lists
        * Side effects still possible after mutation

    * Mutation and iteration
        * **Avoid** mutating a list as you are iterating over it
        * `L1` is `[2,3,4]` not `[3,4]` Why?
            * Python uses an internal counter to keep track of index it is in the loop
            * Mutating changes the list length but Python doesn't update the counter
            * Loop never sees element 2
            * Seems like, generally, clone first then iterate and modify one

# L6: Recursion, dictionaries
    * Last time
        * Tuples - immutable
        * Lists - mutable
        * Aliasing, cloning
        * Mutability side effects

    * Recursion
        * Recursion is the process of repeating items in a self-similar way - Wikipedia
        * "Mise en abyme" or "Droste effect"
            * Picture in picture effect 

    * What is recursion?
        * Algorithmically: a way to design solutions to problems by **divide-and-conquer** or **decrease-and-conquer**
            * Reduce a problem to simpler versions of the same problem
        * Semantically: a programming technique where a **function calls itself**
            * In programming, goal is to NOT have infinite cursion
                * Must have **1 or more base cases** that are easy to solve
                * Must solve the same problem on **some other input** with the goal of simplifying the larger problem input

    * Iterative algorithms so far
        * Looping constructs (`while` and `for` loops) lead to **iterative** algorithms
        * Can capture computation in a set of **state variables** that update on each iteration through loop

    * Multiplication - Iterative Solution
        * "Multiply `a * b`" is equivalent to "add `a` to itself `b` times"
            * `a + a + a + a ... + a`
        * Capture **state** by
            * An **iteration** number (`i`) starts at b
                * `i` <- `i-1` and stop when 0

            * A current **value of computation** (`result`)
                * `result` <- `result + a`

    ```Python
    def mult_iter(a, b):
        result = 0
        while b > 0: 
            result += a
            b -= 1
        return result
    ```

    * Multiplication - recursive solution
        * **Recursive step**
            * Think how to reduce a problem to a **simpler/smaller version** of same problem

        * **Base case**
            * Keep reducing problem until reach a simple case that can be **solved directly**
            * when b = 1, a*b = a

    ```Python
    def mult(a, b):
        if b == 1:
            return a
        else:
            return a + mult(a, b-1)
    ```
    * Factorial
        * `n! = n*(n-1) * (n-2) * (n-3) * ... * 1`
        * For what `n` do we know the factorial?
            * When n = 1 
            ```Python
            if n == 1:
                return 1
            ```

        * How to reduce problem? Rewrite in terms of something simpler to reach base case

    * Recursive function scope example
    ```Python
    def fact(n):
        if n == 1:
            return 1
        else:
            return n*fact(n-1)

    print(fact(4))
    ```
    * Iteration vs Recursion
    ```Python
    def factorial_iter(n):
        prod = 1
        for i in range(1, n+1):
            prod += i
        return prod

    def factorial(n):
        if n == 1:
            return 1
        else:
            return n*factorial(n-1)
    ```

        * Recursion may be simpler, more intuitive
        * Recursion may be efficient from programmer POV
        * Recursion may not be efficient from computer POV

    * Inductive reasoning
        * How do we know that our recursive code will work?
        * `mult_iter` terminates because b is initially positive and decreases by 1 each time around loop; thus must eventually become less than 1
        * In the case of `mult(a, b)`

    * Example of induction
        * 0 + 1 + 2 + 3 + ... + n = (n(n+1))/2
        * Proof:
            * If n = 0, then LHS is 0 and RHS is 0*1/2 = 0, so true
        * Assume true for some k, then need to show that
            * 0 + 1 + 2 + ... + k + (k + 1) = ((k+1)(k+2))/2
            * LHS is k(k+1)/2 + (k+1) by assumption that property holds for problem of size k
            * This becomes, by algebra, ((k+1)(k+2))/2
    * Relevance to code?
        * Same logic applies
        ```Python
        def mult(a, b):
            if b == 1:
                return a
            else:
                return a + mult(a, b-1)
        ```

        * Base case, we can show that `mult` must return correct answer
        * For recursive case, we can assume that `mult` correctly returns an answer for problems of size smaller than, then by the addition step, it must also return a correct answer for problem of size b

    * Towers of Hanoi
        ```Python
        def printMove(fr, to):
            print('move from ' + str(fr) + ' to ' + str(to))

        def Towers(n, fr, to, spare):
            if n == 1:
                printMove(fr, to)
            else:
                Towers(n-1, fr, spare, to)
                Towers(1, fr, to, spare)
                Towers(n-1, spare, to, fr)
        ```

    * Recursion with multiple base cases
        * Fibonacci numbers
            * Leonardo of Pisa (aka Fibonacci) modeled the following challenge
                * Newborn pair of rabbits (one female, one male) are put in a pen
                * Rabbits mate at age of one month
                * Rabbits have a one month gestation period
                * Assume rabbits never die, that female always produces one new pair (one male, one female) every month from its second month on.
                * How many female rabbits are there at the end of one year?

    * Fibonacci
        * After one month (call it 0) - 1 female
        * After second month - still 1 female (now pregnant)
        * After third month - two females, one pregnant, one not
        * In general, females(n) = females(n-1) + females(n-2)
            * Every female alive at month n-2 will produce one female in month n;
            * These can be added those alive in month n-1 to get total alive in month n
    
    ```Python
    def fib(x):
        """assumes x an int >= 0
           returns Fibonacci of x"""
        if x == 0 or x == 1:
            return 1
        else:
            return fib(x-1) + fib(x-2)
    ```
    * Recursion on non-numerics
        * How to check if a string of characters is a palindrome, i.e., reads the same forwards and backwards
            * "Able was I, ere I saw Elba" - attributed to Napoleon
            * "Are we not drawn onward, we few drawn onward to new era?" - attributed to Anne Michaels

    * Solving recursively?
        * First convert the string to just characters, by stripping out punctuation, and converting uppercase to lower case
        * Then
            * Base case: a string of length 0 or 1 is a palindrome
            * Recursive case:
                * If first character matches last character, then is a palindrome if middle section is a palindrome

    * Example
        * 'Able was I, ere I saw Elba' -> 'ablewasiereisawelba'
        * `isPalindrome('ablewasiereisawelba')` is same as
            * `'a' == 'a'` and `isPalindrome('blewasiereisawelb')`
    ```Python
    def isPalindrome(s):
        
        def toChars(s):
            s = s.lower()
            ans = ''
            for c in s:
                if c in 'abcdefghijklmnopqrstuvwxyz':
                    ans = ans + c
            return ans

        def isPal(s):
            if len(s) <= 1:
                return True
            else:
                return s[0] == s[-1] and isPal(s[1:-1])

        return isPal(toChars(s))
    ```

    * How to store student info
        * So far, can store using separate lists for every info
        ```
        names = ['Ana', 'John', 'Denise', 'Katy']
        grade = ['B', 'A+', 'A', 'A']
        course = [2.00, 6.0001, 20.002, 9.01]
        ```
        * A **separate list** for each item
        * Each list must have the **same length**
        * Info stored across lists at **same index**, each index refers to info for a different person

    * A better and cleaner way - a dictionary
        * Nice to **index item of interest directly** (not always int)
        * Nice to use **one data structure**, no separate lists

    * A Python dictionary
        * Store pairs of data
            * key
            * value
    ```Python
    my_dict = {}
    grades = {'Ana':'B', 'John':'A+', 'Denise':'A', 'Katy':'A'}
    ```

    * Dictionary lookup
        * Similar to indexing into a list
        * **Looks up** the **key**
        * **Returns** the **value** associated with the key
        * If key isn't found, get an error
    
    * Dictionary operations
        * **Add** an entry
        `grades['Sylvan'] = 'A'`
        * **Test** if key in dictionary
        `'John' in grades # returns True`
        * **Delete** entry
        `del(grades['Ana'])`
        * Get an **iterable that acts like a tuple of all keys**
        `grades.keys()`
        * Get an **iterable that acts liek a tuple of all values**
    * `list` vs `dict`
        * List
            * **Ordered** sequence of elements
            * Look up elements by an integer index
            * Indices have an **order**
            * Index is an **integer**
        * Dict
            * **Matches** "keys" to "values"
            * Look up one item by another item
            * **No order** is guaranteed
            * Key can be any **immutable** type

    * Creating a dictionary
    ```Python
    def lyrics_to_frequencies(lyrics):
        myDict = {}
        for word in lyrics:
            if word in myDict:
                myDict[word] += 1
            else:
                myDict[word] = 1
        return myDict
    ```

    * Using the dictionary
    ```Python
    def most_common_words(freqs):
        values = freqs.values()
        best = max(values)
        words = []
        for k in freqs:
            if freqs[k] == best:
                words.append(k)
        return (words, best)
    ```

    * Leveraging dictionary properties
    ```Python
    def words_often(freqs, minTimes):
        result = []
        done = False
        while not done:
            temp = most_common_words(freqs)
            if temp[1] >= minTimes:
                result.append(temp)
                for w in temp[0]:
                    del(freqs[w])
            else:
                done = True
        return result

    print(words_often(beatles, 5))
    ```

    * Fibonacci with a dictionary
        * Do **lookup first** in case already calculated the value
        * **Modify dictionary as progress through function calls

        ```Python
        def fib_efficient(n, d):
            if n in d:
                return d[n]
            else:
                ans = fib_efficient(n-1, d) + fib_efficient(n-2, d)
                d[n] = ans
                return ans

        d = {1:1, 2:2}
        print(fib_efficient(6, d))
        ```
        * Known as memoization

# L7: Testing, debugging, exceptions and assertions 
    * We aim for high quality - An analogy with soup
        * You are making soup but bugs keep falling in from the ceiling. What do you do?

    * Programming so far...
        * Expectations are different from reality

    * Defensive programming
        * Write **specifications** for functions
        * **Modularize** programs
        * Check **conditions** on inputs/outputs (assertions)

    * Testing/Validation
        * **Compare** input/output pairs to specification
        * "It's not working!"
        * "How can I break my program?"

    * Debugging
        * **Study events** leading up to an error
        * "Why is it not working?"
        * "How can I fix my program?"

    * Classes of tests
        * Unit testing
            * Validate each piece of program
            * **Testing each function** sepearately
        * Regression testing
            * Add test for bugs as you find them
            * **Catch reintroduced** errors that were previously fixed
        * Integration testing
            * Does **overall program** work?
            * Tend to rush to do this 

    * Testing approaches
        * **Intuition** about natural boundaries to the problem
        ```Python
        def is_bigger(x, y):
            """ Assumes x and y are ints
            Returns True is y is less than x, else False """
        ```
            * Can you come up with some natural partitions?
        * If no natural partitions, might do **random testing**
            * Probability that code is correct increases with more tests
            * Better options below
        * **Black box testing**
            * Explore paths through specification
        * **Glass box testing**
            * Explore paths through code

    * Black box testing
    ```Python
    def sqrt(x, eps):
        """ Assumes x, eps floats, x >= 0, eps > 0
        Returns res such that x-eps <= res*res <= x+epx"""
    ```

        * Designed **without looking** at the code
        * Can be done by someone other than the implementer to avoid some implementer **biases**
        * Testing can be **reused** if implementation changes
        * **Paths** through specification
            * Build test cases in different natural space partitions
            * Also consider boundary conditions (empty lists, singleton list, large numbers, small numbers)

    * Glass box testing
        * **Use code** directly to guide design of test cases
        * Called **path-complete** if every potential path through code is tested at least once
        * What are some **drawbacks** of this type of testing?
            * Can go through loops arbitrarily many times
            * Missing paths
        * Guidelines
            * Branches
            * For loops
            * While loops

        ```Python
        def abs(x):
            """ Assumes x is an int
            Returns x if x>=0 and -x otherwise"""
            if x < -1:
                return -x
            else:
                return x
        ```
        * A path-complete test suite could **miss a bug**
        * Path-complete test suite: 2 and -2
        * but abs(-1) incorrectly returns -1
        * Should still test boundary cases

    * September 9, 1947
        * Mark II Aiken Relay Computer
        * First actual case of bug found
    * Debugging steps
        * **Study** program code
            * Don't ask what is wrong
            * Ask how did I get the unexpected result
            * Is it part of a family?
        * **Scientific method**
            * Study available data
            * Form hypothesis
            * Repeatable experiments
            * Pick simplest input to test with

    * Error messages - easy
        * Trying to access beyond the limits of a list
        * Trying to convert an inappropriate type
        * Referencing non-existent variable
        * Mixing data types without appropriate coercion
        * Forgetting to close parenthesis, quotation, etc.

    * Logic errors - hard
        * **Think** before writing new code
        * **Draw** pictures, take a break
        * **Explain** the code to
            * Someone else
            * Rubber ducky

    * Do's and Don't's
        * Don't
            * Write entire program
            * Test entire program
            * Debug entire program
            * Change code
            * Remember where bug was or what change you made
            * Panic
        * Do
            * Write a function
            * Test the function, debug the function
            * Write a function
            * Test the function, debug the function
            * *** Do integration testing ***
            * Backup code
            * Change code
            * Write down potential bug in a comment
            * Test code
            * Compare new version with old version
        
    * Other types of exceptions
        * Already seen common error types:
            * `SyntaxError`: Python can't parse program
            * `NameError`: Local or global name not found
            * `AttributeError`: Attribute reference fails
            * `TypeError`: Operand doesn't have correct type
            * `ValueError`: Operand type okay, but value is illegal
            * `IOError`: IO system reports malfunction (e.g. file not found)

    * Dealing with exceptions
        * Python code can provide **handlers** for exceptions
        ```Python
        try:
            a = int(input("Tell me one number:"))
            b = int(input("Tell me another number:"))
            print(a/b)
        except:
            print("Bug in user input.")
        ```

        * Exceptions **raised** by any statement in body of **`try`** are **handled** by the **`except`** statement and execution continues with the body of the `except` statement
    * Handling specific exceptions
        * Have **seperate `except` clauses** to deal with a particular type of exception
    
    * Other exceptions
        * `else`:
            * Body of this is executed when execution of associated `try` body **completes with no exceptions**
        * `finally`:
            * Body of this is **always executed** after `try`, `else` and `except` clauses, even if they raised another error or executed a `break`, `continue` or `return`
            * Useful for clean-up code that should be run no matter what else happened (e.g. close a file)

    * What to do with exceptions?
        * What to do when encounter an error?
        * **Fail silently**
            * Substitute default values or just continue
            * Bad idea! User gets no warning
        * Return an **"error" value**
            * What value to choose
            * Complicates code having to check for a special value
        * Stop execution, **signal error** condition
            * In Python, **raise an exception**
            `raise Exception("descriptive string")`

    * Example: Raising an exception
    ```Python
    def get_ratios(L1, L2):
        """ Assumes: L1 and L2 are lists of equal length of numbers
            Returns: a list containing L1[i]/L2[i]"""
        ratios = []
        for index in range(len(L1)):
            try:
                ratios.append(L1[index]/L2[index])
            except ZeroDivisionError:
                ratios.append(float('nan'))
            except:
                raise ValueError('get_ratios called with bad arg')

        return ratios
    ```
    
    * Example of exceptions
        * Assume we are **given a class list** for a subject: each entry is a list of two parts
            * A list of first and last name for a student
            * A list of grades on assignments
        * Create a **new class list**, with name, grades and an average

    * Example code
    ```Python
    class_list = [[['peter', 'parker'], [80.0, 70.0, 85.0]], [['bruce', 'wayne'], [100.0, 80.0, 74.0]]]

    def get_stats(class_list):
        new_stats = []
        for elt in class_list:
            new_stats.append(elt[0], elt[1], avg(elt[1]))
        return new_stats

    def avg(grades):
        return sum(grades)/len(grades)
    ```

    * Error if no grade for a student
        * If one or more students **don't have any grades**, get an error
        * Get `ZeroDivisionError: float division by zero` because try to `return sum(grades)/len(grades)`

    * Option 1: Flag the error by printing a message
        * Decide to **notify** that something went wrong with a msg
        ```Python
        def avg(grades):
            try:
                return sum(grades)/len(grades)
            except ZeroDivisionError:
                print('warning: no grades data')
        ```
        * Running on some test data gives
        ```Python
        >>> warning: no grades data
        >>> [[['bruce', 'wayne'], [10.0, 8.0, 74], 13.83333334]],   ...
        >>> , [['deadpool'], [], None]
        ```

    * Option 2: Change the policy
        * Decide that a student with no grades gets a **zero**
        ```Python
        def avg(grades):
            try:
                return sum(grades)/len(grades)
            except ZeroDivisionError:
                print('wrning: no grades data')
                return 0.0
        ```
        * Running on some test data gives
        ```Python
        >>> warning: no grades data
        >>> [[['peter', 'parker'], [10.0, 5.0, 85.0], 15.41666666]], ...
        >>> , ['deadpool'], [], 0.0]
        ```

    * Assertations
        * Want to be sure that **assumptions** on state of computation are as expected
        * Use an **`assert` statement** to raise an `AssertationError` exception if assumptions not met
        * An example of good **defensive programming**

    * Example
    ```Python
    def avg(grades):
        assert not len(grades) == 0, 'no grades data'
        return sum(grades)/len(grades)
    ```
        * Raises an `AssertationError` if it is given an empty list for grades
        * Otherwise runs ok

    * Assertations as defensive programming
        * Assertations don't allow a programmer to control response to unexpected conditions
        * Ensure that **execution halts** whenever an expected condition is not met
        * Typically used to **check inputs** to functions, but can be used anywhere
        * Can be used to **check outputs** of a function to avoid propagating bad values
        * Can make it easier to locate a source of a bug

    * Where to use assertations?
        * Goal is to spot bugs as soon as introduced and make clear where they happened
        * Use as a **supplement** to testing
        * Raise **exceptions** if users supplies **bad data input**
        * Use **assertations** to
            * Check **types** of arguments or values
            * Check that **invariants** on data structures are met
            * Check **constraints** on return values
            * Check for **violations** of constraints on procedure (e.g. no duplicates in a list)

# L8: Object Oriented Programming
    * Objects
        * Python supports many different kinds of data
            * `1234`
            * `3.14159`
            * `"Hello"`
            * `[1, 5, 7, 11, 13]`
            * `{"CA": "California", "MA": "Massachusetts"}`
        * Each is an **object**, and every object has:
            * a **type**
            * an internal **data representation** (primitive or composite)
            * a set of procedures for **interaction** with the object
        * An object is an **instance** of a type
            * `1234` is an instance of an `int`
            * `"hello"` is an instance of a string

    * Object oriented programming (OOP)
        * **EVERYTHING IN PYTHON IS AN OBJECT** (and has a type)
        * Can **create new objects** of some type
        * Can **manipulate objects**
        * Can **destroy objects**
            * Explicitly using `del` or just "forget" about them
            * Python system will reclaim destroyed or inaccessible objects - called "garbage collection"

    * What are objects?
        * Objects are **a data abstraction** that captures...
        
        1. An **internal representation**
            * Through data attributes
        2. An **interface** for interacting with object
            * Through methods (aka procedures/functions)
            * Defines behaviours but hides implementation

    * Example: [1,2,3,4] has type list
        * How are lists **represented internally**? Linked list of cells
        * How to **manipulate** lists?
            * `L[i], L[i:j], +`
            * `len(), min(), max(), del(L[i])`
            * `L.append(), L.extend(), L.count(), L.index(), L.insert(), L.pop(), L.remove(), L.reverse(), L.sort()`
        * Internal representation should be private
        * Correct behaviour may be compromised if you manipulate internal representation directly

    * Creating and using your own types with classes
        * Make a distinction between **creating a class** and **using an instance** of the class
        * **Creating** the class involves
            * Defining the class name
            * Defining class attributes
            * For example, someone wrote code to implement a list class

        * **Using** the class involves
            * Creating new **instances** of objects
            * Doing operations on the instances
            * For example, `L=[1,2]` and `len(L)`

    * Define your own types
        * Use the `class` keyword to define a new type

        ```Python
        class Coordinate(object):
            #define attributes here
        ```

        * Similar to `def`, indent code to indicate which statements are part of the **class definition**
        * The word `object` means that `Coordinate` is a Python object and **inherits** all its attributes (inheritance next lecture)
            * `Coordinate` is a subclass of `object`
            * `object` is a superclass of `Coordinate`

    * What are attributes?
        * Data and procedures that "**belong**" to the class
        * **Data attributes**
            * Think of data as other objects that make up the class
            * For example, a coordinate is made up of two numbers
        * **Methods** (procedural attributes)
            * Think of methods as functions that only work with this class
            * How to interact with the object
            * For example you can define a distance between two coordinate objects but there is no meaning to a distance between two list objects

    * Defining how to create an instance of a class
        * First we have to define **how to create an instance** of object
        * Use a **special method called `__init__`** to initialise some data attributes

    ```Python
    class Coordinate(object):
        def __init__(self, x, y):
            self.x = x
            self.y = y
    ```

    * Actually creating an instance of a class
    ```Python
    c = Coordinate(3, 4)
    origin = Coordinate(0, 0)
    print(c.x)
    print(origin.x)
    ```
        * Data attributes of an instance are called **instance variables**
        * Don't provide argument for `self`, Python does this automatically

    * Define a method for the `Coordinate` class
    ```Python
    class Coordinate(object):
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def distance(self, other):
            x_diff_sq = (self.x - other.x)**2
            y_diff_sq = (self.y - other.y)**2
            return (x_diff_sq + y_diff_sq)**0.5
    ```
        * Other than `self` and dot notation, methods behave just like other functions (take params, do operations, return)

    * How to use a method
    ```Python
    def distance(self, other):
        # code here
    ```
        * Using the class:
            * Conventional way
            ```Python
            c = Coordinate(3,4)
            zero = Coordinate(0,0)
            print(c.distance(zero))
            ```

            * Equivalent to
            ```Python
            c = Coordinate(3,4)
            zero = Coordinate(0,0)
            print(Coordinate.distance(c,zero))
            ```

    * Print representation of an object
    ```Python
    >>> c = Coordinate(3,4)
    >>> print(c)
    <__main__.Coordinate object at 0x7fa918510488>
    ```
        * **Uninformative print representaion by default
        * Define a **__str__ method** for a class
        * Python calls the `__str__` method when used with `print` on your class object
        * You choose what it does! Say that when we print a `Coordinate` object, want to show
        ```Python
        >>> print(c)
        <3,4>
        ```

    * Defining your own print method
    ```Python
    class Coordinate(object):
        def __init__(self, x, y):
            self.x = x
            self.y = y
        ...
        def __str__(self):
            return "<"+str(self.x)+","+str(self.y)+">"
    ```

    * Wrapping your head around types and classes
        * Can ask for the type of an object instance
        ```Python
        >>> c = Coordinate(3,4)
        >>> print(c)
        <3,4>
        >>> print(type(c))
        <class __main__.Coordinate>
        ```
        * This makes sense since
        ```Python
        >>> print(Coordinate)
        <class __main__.Coordinate>
        >>> print(type(Coordinate))
        <type 'type'>
        ```
        * Use `isinstance()` to check if an object is a `Coordinate`
        ```Python
        >>> print(isinstance(c, Coorindate))
        True
        ```

    * Special operators
        * +, -, ==, <, >, len(), print and many others
        * Like `print`, can override these to work with your class
        * Define them with double underscores before/after
        ```Python
        __add__(self, other) # -> self + other
        __sub__(self, other) # -> self - other
        __eq__(self, other) # -> self == other
        __lt__(self, other) # -> self < other
        __len__(self) # -> len(self)
        __str__(self) # -> print(self)
        ```

# L9: Python Classes and Inheritance
    * Implementing the class vs. Using the class
        * Write code from two different perspectives
        * **Implementing** a new object type with class
            * **Define** the class
            * Define **data attributes** (WHAT IS the object)
            * Definte **methods** (HOW TO use the object)
        * **Using** the new object type in code
            * Create **instances** of the object type
            * Do **operations** with them

    * Class definition of an object type vs. Instance of a class
        * Class name is the **type**, `class Coordinate(object)`
        * Class if defined generically
            * Use `self` to refer to some instance while defining the class, `(self.x - self.y)**2`
            * `self` is a parameter to methods in class definition
        * Class defines data and methods **common across all instances**
        * Instance is **one specific** object, `coord = Coordinate(1,2)`
        * Data attribute values vary between instances, `c1 = Coordinate(1,2), c2 = Coordinate(3,4)`
            * `c1` and `c2` have different data attribute values `c1.x` and `c2.x` because they are different objects
        * Instance has the **structure of the class**

    * Why use OOP and classes of objects?
        * Mimic real life
        * Group different objects part of the same type

    * How to define a class (recap)
    ```Python
    class Animal(object):
        def __init__(self, age):
            self.age = age
            self.name = None
    ```
    * Getter and Setter methods
    ```Python
    class Animal(object):
        def __init__(self, age):
            self.age = age
            self.name = None
        def get_age(self):
            return self.age
        def get_name(self):
            return self.name
        def set_age(self, newage):
            self.age = newage
        def set_name(self, newname=""):
            self.name = newname
        def __str__(self):
            return "animal:" + str(self.name) + ":" + str(self.age)
    ```
        * **Getters and setters** should be used outside of class to access data attributes

    * An instance and dot notation (recap)
        * Instantiation creates an **instance of an object**
        `a = Animal(3)`
        * **Dot notation** used to access attributes (data and methods) though it is better to use getters and setters to access data attributes
        ```Python
        a.age
        a.get_age()
        ```

    * Information hiding
        * Author of class definition may **change data attribute** variable names
        ```Python
        class Animal(object):
            def __init__(self, age):
                self.years = age
            def get_age(self):
                return self.years
        ```

        * If you are **accessing data attributes** outside the class and class **definition changes**, may get errors
        * Outside of class, use getters and setters instead instead use `a.get_age()` NOT `a.age`
            * Good style
            * Easy to maintain code
            * Prevents bugs

    * Python not great at information hiding
        * Allows you to **access data** from outside class definition `print(a.age)`
        * Allows you to **write to data** from outside class definition `a.age = 'infinite'`
        * Allows you to **create data attributes** for an instance from outside class definition `a.size = "tiny"`
        * It's **not good style** to do any of these!

    * Default arguments
        * **Default arguments** for formal parameters are used if no actual argument is given
        `def set_name(self, newname=""): ...`
        * Default argument used here
        ```Python
        a = Animal(3)
        a.set_name()
        print(a.get_name()
        ```
        * Argument passed in is used here
        ```Python
        a = Animal(3)
        a.set_name("fluffy")
        print(a.get_name())
        ```

    * Hierarchies
        * Everything is an animal
        * Person, cat and rabbit are all animals with common attributes but with more specialised attributes
        * Student is type of person

    * Hierarchies
        * **Parent class** (super class)
        * **Child class** (subclass)
            * **Inherits** all data and behaviours of parent class
            * **Add** more **info**
            * **Add** more **behaviour**
            * **Override** behaviour

    * Inheritance: Parent class
    ```Python
    class Animal(object):
        def __init__(self, age):
            self.age = age
            self.name = None
        def get_age(self):
            return self.age
        def get_name(self):
            return self.name
        def set_age(self, newage):
            self.age = newage
        def set_name(self, newname=""):
            self.name = newname
        def __str__(self):
            return "animal:" + str(self.name) + ":" + str(self.age)
    ```       
    * Inheritance: Subclass
    ```Python
    class Cat(Animal):
        def speak(self):
            print("meow")
        def __str__(self):
            return "cat:"+str(self.name)+":"+str(self.age)
    ```
        * Add new functionality with `speak()`
            * Instance of type `Cat` can be called with new methods
            * Instance of type `Animal` throws error if called with `Cat`'s new method
        * `__init__` is not missing, uses the `Animal` version

    * Class variables and the `Rabbit` subclass
        * **Class variables** and their values are shared between all instances of a class

    ```Python
    class Rabbit(Animal):
        tag = 1
        def __init__(self, age, parent1=None, parent2=None):
            Animal.__init__(self, age)
            self.parent1 = parent1
            self.parent2 = parent2
            self.rid = Rabbit.tag
            Rabbit.tag += 1
    ```
        * `tag` used to give **unique id** to each new rabbit instance

    * Special method to compare two `Rabbits`
        * Decide that two rabbits are equal if they have the **same two parents**
    ```Python
    def __eq__(self, other):
        parents_same = self.parent1.rid == other.parent1.rid \
                       and self.parent2.rid == other.parent2.rid

        parents_opposite = self.parent2.rid == other.parent1.rid
                           and self.parent1.rid == other.parent2.rid
        return parents_same or parents_opposite
    ```
        * Compare ids of parents since **ids are unique** (due to class var)
        * Note you can't compare objects directly
            * For example with `self.parent1 == other.parent1`
            * This calls the `__eq__` method over and over until call it on `None` and gives an `AttributeError` when it tries to do `None.parent1`

# L10: Understanding Program Efficiency, Part 1
    * Want to understand efficiency of programs
        * How can we reason about an algorithm in order to predict the amount of time it will need to solve a problem of a particular size?
        * How can we relate choices in algorithm design to the time efficiency of the resulting algorithm?
            * Are there fundamental limits on the amount of time we will need to solve a particular problem?

        * Computers are fast and getting faster - so maybe efficient programs don't matter?
            * But data sets can be very large (e.g. in 2014, Google served 30,000,000,000,000 pages, covering 100,000,000 GB - how long to search brute force?)
            * Thus, simple solutions may simply not scale with size in acceptable manner
        * How can we decide which option for program is most efficient?

    * How to evaluate the efficiency of programs
        * Measure with a **timer**
        * **Count** the operations
        * Abstract notion **order of growth**
            * Will argue that this is the most appropriate way of assessing the impact of choices of algorithm in solving a problem; and in measuring the inherent difficulty in solving problem

    * Timing a program
        * Use time module
        * Recall that importing means to bring in that class into your own file

    ```Python
    import time

    def c_to_f(c):
        return c*9/5 + 32

    t0 = time.clock() # start clock
    c_to_f(100000) # call function
    t1 = time.clock() - t0 # stop clock
    print("t =", t, ":", t1,"s,")
    ```

    * Timing programs is inconsistent
        * GOAL: to evaluate different algorithms
        * Running time **varies between algorithms** 
        * Running time **varies between implementations** 
        * Running time **varies between computers**
        * Running time is **not predictable** based on small inputs

        * Time varies for different inputs but cannot really express a relationship between inputs and time

    * Counting operations
        * Assume these steps take **constant time**:
            * Mathematical operations
            * Comparisons
            * Assignments
            * Accessing objects in memory

        * Then count the number of operations executed as function of size of input

    * Counting operations is better, but still...
        * GOAL: to evaluate different algorithms
        * Count **depends on algorithm**
        * Count **depends on implementations**
        * Count **independent of computers**
        * No clear definition of **which operations** to count

        * Count varies for different inputs and can come up with a relationsip between inputs and the count

    * Different inputs change how the program runs
        * A fucnction that searches for an element in a list
        ```Python
        def search_for_elmt(L, e):
            for i in L:
                if i == e:
                    return True
            return False
        ```
    * Best, average, worst cases
        * Suppose you are given a list `L` of some length `len(L)`
        * **Best case**: minimum running time over all possible inputs of a given size, `len(L)`
            * Constant for `search_for_elmt`
            * First element in any list
        * **Average case**: average running time over all possible inputs of a given size, `len(L)`
            * Practical measure
        * **Worst case**: maximum running time over all possible inputs of given size, `len(L)`
            * Linear in length of list for `search_for_elmt`
            * Must search entire list and not find it

    * Exact steps vs O()
    ```Python
    def fact_iter(n):
        """assumes n an int >= 0"""
        answer = 1
        while n > 1:
            answer *= n
            n -= 1
        return answer
    ```
        * Computes factorial
        * Number of steps: **1 + 5n + 1**
        * Worst case asymptotic complexity: O(n)
            * Ignore additive constants
            * Ignore multiplicative constants
    
    * Simplification examples
        * Drop constants and multiplicative factors
        * Focus on **dominant terms**

    * Types of orders of growth
        * Constant
        * Linear
        * Quadratic
        * Logarithmic
        * n log n
        * Exponential

    * Analysing programs and their complexity
        * **Combine** complexity classes
            * Analyse statements inside functions
            * Apply some rules, focus on dominant term
        * **Law of Addition** for O():
            * Used with **sequential** statements
            * O(f(n)) + O(g(n)) is O(f(n) + g(n))
            * For example,
            ```Python
            for i in range(n):
                print('a')
            for j in range(n*n):
                print('b')
            ```
            is O(n) + O(n*n) = O(n+n**2) = O(n**2) because of dominant term

    * Complexity classes
        * O(1) denotes constant running time
        * O(log n) denotes logarithmic running time
        * O(n) denotes linear running time
        * O(n log n) denotes log linear running time
        * O(n**c) denotes polynomial running time (c is a constant)
        * O(C**n) denotes exponential running time (c is a constant being raised to a power based on size of input)

    * Linear search on **unsorted** list
    ```Python
    def linear_search(L, e):
        found = False
        for i in range(len(L)):
            if e == L[i]:
                found = True
                # return True speeds up a little but speed up doesn't impact worst case case
        return found
    ```
        * Must look through all elements to decide it's not there

    * O(len(L)) for the loop * O(1) to test if e == L[i]
        * O(1 + 4n + 1) = O(4n + 2) = O(n)

    * Constant time list access
        * If list is all ints
            * ith element at
                * base * 4 + i
        * If list is heterogeneous
            * Indirection
            * References to other objects
    
    * Linear search on **sorted** list
    ```Python
    def search(L, e):
        for i in range(len(L)):
            if L[i] == e:
                return True
            if L[i] > e:
                return False
        return False
    ```
        * Must only look until reach a number greater than e
        * O(len(L)) for the loop * O(1) to test if e == L[i]
        * Overall complexity is **O(n) - where n is len(L)**
        * **NOTE:** order of growth is same, though run time may differ for two search methods

    * Linear complexity
        * Searching a list in sequence to see if an element is present
        * Add characters of a string, assumed to be composed of decimal digits
        ```Python
        def addDigits(s):
            val = 0
            for c in s:
                val += int(c)

            return val
        ```
        * **O(len(s))**

    * Quadratic complexity
        * Determine if one list is subset of second, i.e., every element of first, appears in second (assume no duplicates)
        ```Python
        def isSubset(L1, L2):
            for e1 in L1:
                matched = False
                for e2 in L2:
                    if e1 == e2:
                        matched = True
                        break
                if not matched:
                    return False
            return True
        ```
        * Outer loop executed len(1) times
        * Each iteration will execute inner loop up to len(L2) times, with constant number of operations
        * O(n**2) worst case where lists are same length

        * Find intersection of two lists, return a list with each element appearing only once
        ```Python
            def intersect(L1, L2):
                tmp = []
                for e1 in L1:
                    for e2 in L2:
                        if e1 == e2:
                            tmp.append(e1)
                res = []
                for e in tmp:
                    if not(e in res):
                        res.append(e)
                return res
        ```

        * First nested Loop takes len(L1)*len(L2) steps
        * Second loop takes at most len(L1) steps
        * Determining if element in list might take len(L1) steps

# L11: Understanding Program Efficiency, Part 2
    * Constant complexity
        * Complexity independent of inputs
        * Very few interesting algorithms in this class, but can often have pieces that fit this class
        * Can have loops or recursive calls, but ONLY IF number of iterations of calls independent of size of input

    * Bisection search
        1. Pick an index `i`, that divides list in hald
        2. Ask if `L[i] == e`
        3. If not, ask if `L[i]` is larger or smaller than `e`
        4. Depending on answer, search left or right half `L` for `e`

    * A new version of a divide-and-conquer algorithm
        * Break into smaller version of problem (smaller list), plus some simple operations
        * Answer to smaller version is answer to original problem
        
    * Bisection search complexity analysis
        * Finish looking through list when 1=n/2**i
        * So i = log n
        * Complexity of recursion is **O(log n) - where n is len(L)

    * Bisection search implementation 1
    ```Python
    def bisect_search1(L, e):
        if L == []:
            return False
        elif len(L) == 1:
            return L[0] == e
        else:
            half = len(L)//2
            if L[half] > e:
                return bisect_search1(L[:half], e)
            else:
                return bisect_search1(L[half:], e)

    ```
        * Slicing the list returns a copy of the list!!

    * Complexity of first bisection search method
        * **Implementation 1 - bisect_search1**
            * O(log n) bisection search calls
                * On each recursive call, size of range to be searched is cut in half
                * If original range is of size n, in worst case fown to range of size 1 when n/(2^k) = 1; or when k = log n
            * O(n) for each bisection search call to copy list
                * This is the cost to set up each call, so do this for each level of recursion
            * O(log n) * O(n) -> **O(n log n)**
            * If we are really careful, note that length of list to be copied is also halved on each recursive call
                * Turns out that total cost to copy is **O(n)** and this dominates the log n cost due to the recursive calls

    * Bisection search alternative
        * Still reduce size of problem by factor of two on each step
        * But just keep track of low and high portion of list to be searched
        * Avoid copying the list
        * Complexity of recursion is again **O(log n) - where n is len(L)**
    
    * Bisection search implementation 2
    ```Python 
    def bisect_search2(L, e):
        def bisect_search_helper(L, e, low, high):
            if high == low:
                return L[low] == e
            mid = (low + high)//2
            if L[mid] == e:
                return True
            elif L[mid] > e:
                if low == mid: #nothing left to search
                    return False
                else:
                    return bisect_search_helper(L, e, low, mid - 2)
        if len(L) == 0:
            return False:
        else:
            return bisect_search_helper(L, e, 0, len(L) - 1)
    ```

    * Logarithmic complexity
    ```Python 
    def intToStr(i):
        digits = '0123456789'
        if i == 0:
            return '0'
        result = ''
        while i > 0:
            result = digits[i % 10] + result
            i = i//10
        return result
    ```
        * Only have to look at loop as no function calls
        * Within while loop, constant number of steps
        * How many times through loop?
            * How many times can one divide by 10
            * **O(log(i))

    * O() for iterative factorial
    ```Python
    def fact_iter(n):
        prod = 1
        for i in range(1, n+1):
            prod *= i
        return prod
    ```
        * Overall **O(n)** - n times round lopos, constant cost each time

    * O() for recursive factorial
    ```Python 
    def fact_recur(n):
        """ assume n >= 0 """
        if n <= 1:
            return 1
        else:
            return n*fact_recur(n - 1)
    ```

        * Computes factorial recursively
        * If you time it, may notice that it runs a bit slower than iterative version due to function calls
        * Still **O(n)** because the number of function calls is linear in n, and constant effort to set up call

    * Log-linear complexity
        * Many practical algorithms are log-linear
        * Very commonly used log-linear algorihtm is merge sort
        
    * Polynomial complexity
        * Most common polynomial algorithms are quadratic, i.e., complexity grows with square of size of input
        * Commonly occurs when we have nested loops or recursive function calls
        * Saw this last time

    * Complexity of Towers of Hanoi
        * Let t_n denote time to solve tower or size n
        * t_n = 2t_n-1 + 1
        *     = 2(2t_n-2 + 1) + 1
        *     = 4(2t_n-3 + 1) + 2 + 1
        *     ...
        *     = 2^k * t_n-k + 2^k-1 + .. 4 + 2 + 1
        *     = 2^n-1 + 2n-2 + ... + 4 + 2 + 1
        *     = 2^n - 1
        * So order of growth is **O(2^n)**

    * Exponential complexity
        * Given a set of integers (with no repeats), want to generate the collection of all possible subsets - called the power set
        * {1, 2, 3, 4} would generate
            * {}, {1}, {2}, {3}, {4}, {1, 2}, ..., {1,2,3,4}
        * Order doesn't matter

    * Power set - Concept
        * We want to generate the pwoer set of integers from 1 to n
        * Assume we can generate power set of integers from 1 to n-1
        * Then all of those subsets elong to bigger power set (choosing not include n); and all of those subsets with n added to each of them also belong to the bigger power set (choosing to include n)

    ```Python
    def gen Subsets(L):
        res = []
        if len(L) == 0:
            return [[]] # list of empty list
        smaller = genSubsets(L[:-1]) # All subsets without last element
        extra = L[-1:] # Create a list of just last element
        new = []
        for small in smaller:
            new.append(small+extra) # For all smaller solutions, add one with last element
        return smaller+new
    ```
        * Assuming append is constant time
        * Time includes time to solve smaller proble, plus time needed to make a copy of all elements in smaller problem
        * But important to think about size of smaller
        * Know that for a set of size k there are 2^k cases
        * Let t_n denote time to solve problem of size n
        * Let s_n denote size of solution for problem size n
        * t_n = t_n-1 + s_n-1 + c (where is some constant number of operations)
        * t_n = t_n-1 + 2^n-1 + c
        *     = t_n-2 + 2_n-2 + c + 2^n-1 + c
        *     = t_n-k + 2^n-k + ... + 2^n-1 + kc
        * 1 + 2^2 + nc
        * Thus computing power set is **O(2^n)**

    * Complexity classes
        * O(1) - code does not depend on size of problem
        * O(log n) - reduce problem in half each time through process
        * O(n) - simple iterative or recursive problem
        * O(n log n) - will see next time
        * O(n^c) - nested loops or recursive calls
        * O(c^n) - multiple recursive calls at each level

    * Complexity of iterative Fibonacci
    ```Python
    def fib_iter(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            fib_i = 0
            fib_ii = 1
            for i in range(n-1):
                tmp = fib_i
                fib_i = fib_ii
                fib_ii = tmp + fib_ii
            return fib_ii
    ```
        * Best case: O(1)
        * Worst case: O(1) + O(n) + O(1) => **O(n)**

    * Complexity of recursive Fibonacci
    ```Python
    def fib_recur(n):   
        """ assumes n an int >= 0 """
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fib_recur(n-1) + fib_recur(n-2)
    ```

# L12: Searching and Sorting
    * Searching algorithms
        * Linear search
            * **Brute force search (aka British Museum algorithm)
            * List does not have to be sorted
        * Bisection search
            * List **MUST be sorted** to give correct answer
            * Saw two different implementations of the algorithm

    * Linear search on **unsorted** list: recap
    ```Python
    def linear_search(L, e):
        found = False
        for i in range(len(L)):
            if e == L[i]:
                found = True
        return found
    ```
        * Must look through all elements to decide it's not there
        * O(len(L)) for the loop * O(1) to test if e == L[i]
        * Overall complexity is **O(n) - where n is len(L)**

    * Linear search on **sorted** list: recap
    ```Python
    def search(L, e):
        for i in range(len(L)):
            if L[i] == e:
                return True
            if L[i] > e:
                return False
        return False
    ```
        * Better in terms of average case
        * But still O(n)

    * Bisection search implementation: recap
    ```Python
    def bisect_search2(L, e);
        def bisect_search_helper(L, e, low, high):
            if high == low:
                return L[low] == e
            mid = (low + high) // 2
            if L[mid] == e:
                return True
            elif L[mid] == e:
                if low == mid:
                    return False
                else:
                    return bisect_search_helper(L, e, low, mid - 1)
            else:
                return bisect_search_helper(L, e, mid+1, high)
        if len(L) == 0:
            return False
        else:
            return bisect_search_helper(L, e, 0, len(L) - 1)
    ```

    * Searching a sorted list -- n is len(L)
        * Using **linear search**, serach for an element is **O(n)**
        * Using **binary search**, can search for an element in **O(log n)**
            * Assumes the **list is sorted**!
        * When does it make sense to **sort first then search**?
            * SORT + O(log n) < O(n) => SORT < O(n) - O(log n)
            * When sorting is less than O(n)

        * **NEVER TRUE**!

    * Amortized cost -- n is len(L)
        * Why bother sorting first?
        * In some cases, may **sort a lit once** then do **many searches**
        * **AMORTIZE cost** of the sort over many searches
        * SORT + K*O(log n) < K*O(n)
            * for large K, **SORT time becomes irrelevant**, if cost of sorting is small enough

    * Monkey sort
        * Permutation sort/bogo sort

    * Complexity of bogo sort
    ```Python
    def bogo_sort(L):
        while not is_sorted(L):
            random.shuffle(L)
    ```
        * Best case: **O(n) where n is len(L)** to check if sorted
        * Worst case: O(?) it is **unbounded** if really unlucky

    * Bubble sort
        * **Compare consecutive pairs** of elements
        * **Swap elements** in pairs such that smaller is first
        * When reach end of list, **start over** again
        * Stop when **no more swaps** have been made
        * Largest unsorted element always at end after pass, so at most n passes

    * Complexity of bubble sort
    ```Python
    def bubble_sort(L):
        swap = False
        while not swap:
         swap = True
        for j in range(1, len(L)):
            swap = False
            temp = L[j]
            L[j] = L[j-1]
            L[j-1] = temp
    ```
        * Inner for loop is for doing the **comparisons**
        * Outer while loop is for doing **multiple passes** until no more swaps

    * Selection sort
        * First step
            * Extract **minimum element**
            * **Swap it** with element at **index 0**

        * Subsequent step
            * In remaining sublist, extract **minimum element**
            * **Swap it** with the element at **index 1**

        * Keep the left portion of the list sorted
            * At i'th step, **first i elements in list are sorted**
            * All other elements are bigger than first i elements

    * Analysing selection sort
        * Loop invariant
            * Given prefix of list L[0:i] and suffic L[i+1:len(L)], then prefix is sorted and no element in prefix is larger than smallest element in suffix
                1. Base case: prefix empty, suffix whole list - invariant true
                2. Induction step: move minimum element from suffix to end of prefix. Since invariant true before move, prefix sorted after append
                3. When exit, prefix is entire list, suffix empty, sorted

    * Complexity of selection sort
    ```Python
    def selection_sort(L):
        suffixSt = 0
        while suffixSt != len(L):
            for i in range(suffixSt, len(L)):
                if L[i] < L[suffixSt]:
                    L[suffixSt], L[i] = L[i], L[suffixSt]
            suffixSt += 1
    ```
        * Outer loop executes len(L) times
        * Inner loop len(L) - i times
        * Complexity of selection sort is **O(n**2) where n is len(L)**

    * Merge sort
        * Divide and conquer
        * **Split list in half** until have sublists of only 1 element

    * Merging sublists step
    ```Python
    def merge(left, right):
        result = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(left[i])
                j += 1
        while i < len(left):
            result.append(left[i])
            i += 1
        while j < len(right):
            result.append(right[j])
            j += 1
        return result
    ```

    * Complexity of merging sublists step
        * Go through two lists, only one pass
        * Compare only **smallest elements in each sublist**
        * O(len(left) + len(right)) copies elements
        * O(len(longer list)) comparisons
        * **Linear in length of the lists**

    * Merge sort algorithm -- recursive
    ```Python
    def merge_sort(L):
        if len(L) < 2:
            return L[:]
        else:
            middle = len(L) // 2
            left = merge_sort(L[:middle])
            right = merge_sort(L[middle:])
            return merge(left, right)
    ```
        * **Divide list** successively into halves
        * Depth-first such that **conquer smallest pieces down one branch** first before moving to larger pieces
       
    * Complexity of merge sort
        * At **first recursion level**
            * n/2 elements in each list
            * O(n) + O(n) = O(n) where n is len(L)
        * At **second recursion level**
            * n/4 elements in each list
            * Two merges -> O(n) where n is len(L)
        * Each recursion level is O(n) where n is len(L)
        * **Dividing list in half** with each recursive call
            * O(log(n)) where n is len(L)
        * Overall complexity is **O(n log(n)) where n is len(L)**


    * What do computer scientists do?
        * They think computationally
            * Abstractions, algorithms, automated execution
        * Just like the three r's: reading, 'riting, and 'rithmetic - computational thinking is becoming a fundamental skill that every well-educated person will need

    * The three A's of computational thinking
        * Abstractions
            * Choosing the right abstractions
            * Operating in multiple layers of abstraction simultaneously
            * Defining the relationships between abstraction layers

        * Automation
            * Think in terms of mechanising out abstractions
            * Mechanisation is possible - because we have precise and exacting notations and modelsl and because there is some "machine" that can interpret our notations
        
        * Algorithms
            * Language for describing automated processes
            * Also allows abstraction of details

