# How to read code

So far we have focused on designing programs and writing Python code. This is the key creative process but, in order to write code, programmers must be able to read code written by others. (Or even code written by us years later.) 

## Why read code?

We read code in order to:

* **Gain new experience**. Just as in natural language where we learn to speak by listening to others, we learn programming techniques by recognizing cool patterns in the code of others. Code is how programmers communicate and you will need to quickly understand the code I build in class.
* **Find and adapt code snippets**. We can often find hints or solutions to a coding problem through code snippets found via Google search or at [StackOverlow](https://stackoverflow.com/).  Be careful here you do not violate copyright laws or, in the case of student projects, academic honesty rules.
* **Discover the behavior of library functions or other shared code**.   The complete behavior of a library function is not always clear from the name or parameter list.  Looking at the source code for that function is the best way to understand what it does. The code **is** the documentation. While we're discussing library functions, let me highlight a golden rule: *You should never ever ask your fellow programmers about the details of parameters and return values from library functions.* You can easily discover this yourself using "jump to definition" in PyCharm or by searching on the web.
* **Uncover bugs, in our code or others' code**. All code has bugs, particularly code we just wrote that has not been tested exhaustively. As part of the coding process, we are constantly bouncing around, reading our existing code base to make sure everything fits together.

The purpose of this document is to explain how exactly a programmer reads code. Our first clue comes from the fact that we are not computers, hence, we should not read code like a computer, examining one symbol after the other. Instead, we're going to look for key elements and code patterns.

This is what we do when reading sentences in a foreign language. For example, my French is pretty bad so, when reading a French sentence, I have to consciously ask *who is doing what to whom*. In practice, that means identifying the subject, the verb, and the object. From these key elements, I try to imagine the thought patterns in the mind of the author.  I am essentially trying to reverse the process followed by the author.

In the programming world, the process goes like this: The code author might have thought "*convert prices to a new list by dividing by 2*", which they converted to "map" pseudocode and finally to a Python `for` loop.  When reading that loop code, our job is to reverse the process and imagine the original goal of the author.  

That's why you should emphasize clarity when writing code, so that reading the code more easily leads the reader to your intentions.  There is an excellent quote (by [John F. Woods](https://groups.google.com/forum/#!msg/comp.lang.c++/rYCO5yn4lXw/oITtSkZOtoUJ) I think) that summarizes things well:

> Always code as if the person who ends up maintaining your code will be a violent psychopath who knows where you live.

## Getting the gist of a program

When looking at a textbook for the first time, it makes sense to scan through the table of contents to get an overall view of the book content. The same is true when looking at a program for the first time. Look through all of the files and the names of the functions contained in those files. Also figure out where the main program is. Depending on your goal in reading the program, you might start stepping through the main program or immediately jump to a function of interest.

It's also useful to look at the input-output pairs of the program, because it helps you understand the program's functionality. In some sense, we are reverse-engineering the program work plan by examining and testing the program. Previously, we used the program work plan in the forward direction to design programs.

## Getting the gist of a function

Once we identify a main program or function to examine, it's time to reverse-engineer the function work plan. The function's name is perhaps the biggest clue as to what the function does, assuming the code author was a decent programmer. For example, there is no doubt what the following function's goal is:

```python
def average(...):
    ...
```

even without looking at the arguments or the function statements.

Often programmers will provide comments about the usage of a function, but be careful. Often programmers change the code without changing the comments and so the comments will be misleading. An acceptable comment might look like:

```python
def average(...):
    "Compute and return the average of a list of numbers"
    ...
```

If we're lucky, that comment corresponds to the function objective description in the work plan.

The next step is to identify the parameters and return value. Again, the names of the parameters often tell us a lot but, unfortunately, Python does support explicit parameter types so we have to figure that out ourselves. Knowing the types of value and variable is critical to understanding a program.  In a simple function like this, we can usually figure out the types of the parameters in the return values quickly. In other cases, we will have to dig through the statements of the function to figure this out (more on this later).  Let's zoom in to see more detail about our function:
 
```python
def average(data):
    ...
    return sum / n
```

At this point, we know that `data` is almost certainly a list of numbers and the function returns a single number. That means we can fill in the first part of the work plan for the function.

## What to look for in function code

Because we have prior knowledge of what the average is, we can fill in the work plan description of the function objective. In general, though, we have to scan the statements of the function to figure that out. (We might get lucky and find a reasonable function comment as well.) Let's look at the full function now:

```python
def average(data):
    n = len(data)
    sum = 0.0
    for x in data:
        sum = sum + x
    return sum / n
```

An inexperienced programmer must examine the statements of the function individually and literally, sort of emulating a computer to figure out the emergent behavior. In contrast, *an experienced programmer looks for patterns in the code that represent implementations* of high-level patterns like map, search, filter, etc... 

By analogy, consider memorizing the state of a chessboard in the middle of play. A beginner has to memorize where all of the pieces are individually whereas a chessmaster recognizes that the board is, say, merely a variation on the Budapest Gambit.

How do we know where to start and what to look at? Well, let's think back to the [generic analytics program template](programming.md):

1. Acquire data, which means finding a suitable file or collecting data from the web and storing in a file
2. Load data from disk and place into memory organized into data structures
2. Normalize, clean, or otherwise prepare data
3. Process the data, which can mean training a machine learning model, computing summary statistics, or optimizing a cost function
4. Emit results, which can be anything from simply printing an answer to saving data to the disk to generating a fancy visualization

The gist of that process is to load data into a handy data structure and process it. What do loading data, creating a data structure, and processing a data structure have in common? They all repeatedly execute a set of operations, which means that the gist of a program that processes data is looping. (There is even a famous book is entitled [Algorithms + Data Structures = Programs](https://www.amazon.com/Algorithms-Structures-Prentice-Hall-Automatic-Computation/dp/0130224189).)  A program that does not loop would likely be very boring as it could not traverse a data structure or process a data file.

From this, we can conclude that all of the action occurs in loops so we should look for loops in the code first. We saw lots of pseudocode loop templates in [Common lower-level programming patterns](combinations.md) and Python loop templates in [Programming Patterns in Python](python-patterns.ipynb). Reading code is a matter of finding such templates in the code of a function, which immediately tells us the kind of operation or pattern the author intended.

## Identifying programming patterns in code

Let's dig through some loop examples, trying to identify the high-level patterns or operations. The key elements to look for are the holes in the templates we studied. This usually means identifying the loop variable, the loop bounds, which data structure we're traversing, and the operation performed on the data elements.  The goal is to reverse engineer the intentions of the code author.

**Exercise**: To get started, what pattern does the `sum` function above follow?

```python
sum = 0.0
for x in data:
    sum = sum + x
```

That's an accumulator.

**Exercise**: Let's look at a loop where I have deliberately used crappy variable names.

```python
foo = []
for blah in blort:
    foo.append(blah * 2)
```

That's a map operation, which we can see from the initialization of an empty target list and the `foo.append(...)` call. The `blah * 2` is not relevant to finding the pattern other than the fact that the target list is a function of `blah`, which comes from the source list `blort`.

**Exercise**:  What kind of loop (for-each, indexed, nested, etc...) do you see in the following code? What kind of high level pattern is the code performing?

```python
blort = []
for boo in range(len(foo)):
    blort.append(foo[boo] * 2)
```

That's an indexed-loop that again does map operation. The clue that it is an indexed loop is that the bounds are `range(len(foo))` which is giving a range of indices. Because of the `blort.append` and reference to `foo[boo]`, we know it is a map operation. We know that `foo` is a list of some kind because of the `[boo]` index operator.

**Exercise**:  What is the high-level pattern followed by this code:

```python
foo = []
for i in range(len(X)):
    foo.append(X[i]+Y[i])
```

It is combining two columns (lists) into a target column. We know that X and Y are lists because of the `[i]` array indexing.

**Exercise**: What high-level math operation is this code performing?

```python
for i in range(n):
    for j in range(n):
        C[i][j] = A[i][j] + B[i][j]
```

Matrix addition. It's important here to recognize that a nested indexed-loop gives all combinations of the loop variables, `i` and `j`, in the range [0..n). One of the most common reasons to do this is to iterate through the elements of a matrix or an image. The answer here could also be image addition.

**Exercise**:  How many `'hi'`s get printed by this loop?

```python
for i in range(n):
    for j in range(n):
        print 'hi'
```

n * n. The inner loop goes around n times. The outer loop means we perform the entire inner loop n times.

**Exercise**:  What is this code doing? I.e., what is the value of `blort` in the abstract after the loop completes?

```python
blort = -99999
for x in X:
    if x > blort:
        blort = x
print blort
```

Max value in `X`. Anytime you see an `if` statement inside of a loop, think *filter* or *search*. It will usually be a variation on one of those. This assumes that the conditional expression is a function of the loop variable directly or indirectly.

**Exercise**: What does this variation print?

```python
blort = -99999
for i in range(len(X)):
    if X[i] > blort:
        blort = x
print blort
```

Exactly the same thing; `blort` is the max of `X`.  You see a conditional expression, that is a function of the loop variable, inside of a loop. This is just a reformulation of the previous.

**Exercise**: What is the goal of this code? I.e., what value it print for `foo` after the loop?

```python
foo = -1
bar = -99999
for i in range(len(X)):
    if X[i] > bar:
        bar = x
        foo = i
print foo
```

argmax of `X`.  We know the code associated with the conditional is figuring out the max from our previous examples, but it is also tracking the `i`, the index. 

Think of this as a standard pattern you've already figured out, but variation that does some extra stuff. Then ask what the difference between the two is. Here's an excellent case for trying to understand what the input-output pairs are (though we're talking about the guts of but not a full function here). With the max computation, the output is a value taken from `X`. In this case, the value printed out is an index in 0..len(X)-1.

**Exercise**: Describe what value `bar` has after this code completes.

```python
foo = []
bar = []
for blah in blort:
    foo.append(blah * 2)
for zoo in foo:
    if zoo>10:
        bar.append(zoo)
```

There's a lot going on here, but it is really nothing more than two patterns in a sequence. The first pattern is a map operation that doubles the values in `blort` to create the `foo` list, which is consumed by the second loop. The second loop is just a filter that extracts all values > 10 from `foo` into `bar.