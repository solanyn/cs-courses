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

