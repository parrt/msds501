# How to read code

So far we have focused on designing programs and writing Python code. This is the key creative process but, in order to write code, programmers must be able to read code written by others. (Or even code written by us years later.) We read code in order to:

* **Gain new experience**. Just as in natural language where we learn to speak by listening to others, we learn programming techniques by recognizing cool patterns in the code of others.
* **Find and adapt code snippets**. We can often find hints or solutions to a coding problem through code snippets found via Google search or at [StackOverlow](https://stackoverflow.com/).  Be careful here you do not violate copyright laws or, in the case of student projects, academic honesty rules.
* **Discover the behavior of library functions or other shared code**.   The complete behavior of a library function is not always clear from the name or parameter list.  Looking at the source code for that function is the best way to understand what it does. The code **is** the documentation. While we're discussing library functions, let me highlight a golden rule: *You should never ever ask your fellow programmers about the details of parameters and return values from library functions.* You can easily discover this yourself using "jump to definition" in PyCharm or by searching on the web.
* **Uncover bugs, in our code or others' code**. All code has bugs, particularly code we just wrote that has not been tested exhaustively. As part of the coding process, we are constantly bouncing around, reading our existing code base to make sure everything fits together.

The purpose of this document is to explain how exactly a programmer reads code. Our first clue comes from the fact that we are not computers, hence, we should not read code like a computer, examining one symbol after the other. Instead, we're going to look for key elements and code patterns. 

This is what we do when reading sentences in a foreign language. For example, my French is pretty bad so, when reading a French sentence, I have to consciously ask *who is doing what to whom*. In practice, that means identifying the subject, the verb, and the object. From these key elements, I try to imagine the thought patterns in the mind of the author.  I am essentially trying to reverse the process followed by the author.

In the programming world, the process goes like this: A programmer might think "convert prices to a new list by dividing by 2", which they convert to the "map" pseudocode and finally to a Python `for` loop.  When reading that loop code, our job is to reverse the process and imagine the original goal of the author.  

That's why you should emphasize clarity when writing code, so that reading the code more easily leads the reader to your intentions.  There is an excellent quote (by [John F. Woods](https://groups.google.com/forum/#!msg/comp.lang.c++/rYCO5yn4lXw/oITtSkZOtoUJ) I think) that summarizes things well:

> Always code as if the person who ends up maintaining your code will be a violent psychopath who knows where you live.

Let's dig through some examples, trying to identify the patterns.

when looking at a program for the first time

scan through the table of contents, the list of function definitions

when looking at a main program or a function:

look for the loops
