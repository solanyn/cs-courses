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


