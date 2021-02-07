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


