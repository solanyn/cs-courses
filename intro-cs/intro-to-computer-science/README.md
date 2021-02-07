<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Introduction to Computer Science](#introduction-to-computer-science)
- [L1: What is Computation](#l1-what-is-computation)

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

        
