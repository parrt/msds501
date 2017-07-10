# Functions (subprograms)

At this point, you should be getting pretty tired of repeating the sequence of operations in your program work plans that computes the average of some numbers:

* Use accumulator to sum the values<br>
* Use accumulator to count the values<br>
* If the count is 0, the average is 0 else compute the average as the sum divided by the count

The sequence is identical in all of the examples we've done so far; the only change is the list of numbers to which we apply the operations.  With some experience, we've learned to repeat that sequence every time we need to compute the average. It's exactly like learning to spit out the words for "*where is the subway?*" in a foreign language.

Now, let's bake that experience into a single entity, called a **function** or **procedure** or **method**, that formalizes the notion of reusing a sequence of operations.  For convenience, we're going to refer to this sequence by name, such as "*average*." Then, we can say things like invoke "*average of unit prices*" or "*average of rainfall*" to apply the sequence of operations to a specific list.  For example, the processing steps for [rainfall average](images/rainfall-average-plan.png) could be rewritten more simply as:

* Load the numbers into a list in memory
* Search for 999 in the list
* Slice out all numbers up to but not including 999’s position
* <s>Use accumulator to sum the values<br>
* Use accumulator to count the values<br>
* If the count is 0, the average is 0 else compute the average as the sum divided by the count</s>
* **Invoke the *average* computation on the rainfall subset**
* Print the average

Reusing someone else's proven sequence of operations is  something we do all the time in the real world.  For example, we reuse recipes from a cookbook when making dinner.  Each recipe has a name, a list of ingredients, a sequence of operations, and (returns) a final product.  Here's how I could describe my awesome recipe for making snow: 

**name**: `snow`<br>
**ingredients**: multiple ice cubes<br>
**result**: some snow<br>
**steps**:<br>
&nbsp;&nbsp;&nbsp;&nbsp;put ice in blender<br>
&nbsp;&nbsp;&nbsp;&nbsp;turn on blender for 10 seconds<br>
&nbsp;&nbsp;&nbsp;&nbsp;dump out the snow into a bowl

Functions are just like recipes except that the sequence of operations has to be more precise, since we will ultimately need to have an intolerant computer execute the sequence.

As a more realistic example, consider the [formula for a line](https://www.mathsisfun.com/equation_of_line.html) from algebra: *y* = *mx* + *b* where *m* is the slope and *b* is the y-intercept. Here's a line at 45 degrees (slope 1) crossing the y-axis at 2: *y* = *x* + *2*. Another way to write that is *line(x)* = *x* + *2*, which we can describe as:

**name**: *line*<br>
**ingredients**: *x* coordinate<br>
**result**: *y* coordinate associated with *x*<br>
**steps**:<br>
&nbsp;&nbsp;&nbsp;&nbsp;compute *x* + *2*<br>
&nbsp;&nbsp;&nbsp;&nbsp;return that value

Now that we have the basic idea, let's take a more formal look at designing functions.
 
## Functions are subprograms

A sequence of operations grouped into a single, named entity is called a **function**. Functions are like mini programs or subprograms that we can plan out just like full programs.  

Python **programs** consist of zero or more functions and the so-called "main" program, consisting of a sequence of operations that gets the ball rolling.

Instead of loading data from the disk, functions operate on data given to them from the invoking program. This incoming data is analogous to a recipe's list of ingredients and is specified in the form of one or more named *parameters* (also called *arguments*). Instead of printing a result or displaying a graph, as a program would, functions *return* values.  

We begin planning a function by identifying:
 
1. a descriptive function name
2. the kind of value(s) it operates on (parameter types)
3. the kind of value it returns (return type)
4. what the function does

These function planning steps are essentially the first two steps from our program problem-solving strategy where we  identify what kind of input we have and what the expected result is.  If we can't specifying exactly what goes in and out of the function, there's no hope of processing steps, let alone Python code, to implement that function.

Then we manually write out some sample function invocations to show what data goes in and what data comes out. 

Next, we plan out the sequence of operations needed by the function to compute the desired result.  As when designing a whole program, we start with the return value and work our way backwards, identifying operations in reverse order. Note: The operations should be purely a function of the data passed to them as parameters---functions should be completely ignorant of any other data. (More on this when we actually translate function pseudocode to Python.) 

**Exercise**. Fill out a [Function work plan](plans/function-planning.pdf) for a function that computes *y = x + 2*. ([solution](images/line-function-plan.pdf))

## Invoking functions

Let's plan out an entire program that *invokes* or *calls* the `line` function a few times, which we might want to do when plotting a line. In other words, we want to give a bunch of X coordinates to the `line` function, one at a time, and get back a bunch of Y coordinates.  Starting out simply, let's plan out a program that "*computes two points on a line for X coordinates -3 and 3*" (our description of objective). The expected input-output is "*-3 and 3 give -1 and 5*".

The processing steps are pretty simple, but let's put them in the right positions:

1. **Acquire data**
1. **Load data into a data structure**
1. **Normalize, clean, or otherwise prepare data**
1. **Process the data**<br>
Invoke `line` with -3<br>
Invoke `line` with 3<br>
1. **Emit results**<br>
print first y value returned from `line`<br>
print second y value returned from `line`

For the data processing steps, we can also use the notation from the sample function parameter and result section of the `line` function:

1. **Process the data**<br>
`line(-3)`<br>
`line(3)`

But that only gives us two X/Y points on a line. We might want to compute the Y-coordinate for a whole list of X coordinates.

**Exercise**: See if you can figure out the program work plan for a variation that accepts a list of numbers, rather than a predefined set of just 2 X values.

In this case, our sample input-output pairs for the program look like:

-3, 0, 2, 10 → -1, 2, 4, 12<br>
 → 

where the second line means that an empty list gets no output.

The processing steps now need to load the numbers into memory as we did with the program that computed averages.  The programming operation we need to solve this problem is the *map*, which will apply the `line` function to each X coordinate in the list. It helps to look at the operation visually:

<img src=images/XY.png width=300>

The only difference between this map operation and what we've seen previously is that we are applying a function that *we* implemented, instead of a built-in operator like multiply.

To finish off the processing steps in the program work plan, we can print out the Y list computed during the map. The whole thing looks like this:

1. **Acquire data**
1. **Load data into a data structure**<br>
Load the X coordinates into a list in memory
1. **Normalize, clean, or otherwise prepare data**
1. **Process the data**<br>
Use map operation to apply `line` function to each element of the list, yielding a new list of Y coordinates
1. **Emit results**<br>
print out the Y coordinates

## List parameters

Now let's work on a function that takes a list instead of a number as a parameter.
 
**Exercise**. Fill out a [Function work plan](plans/function-planning.pdf) for a function that computes the average of some numbers. ([solution](images/average-function-plan.pdf))

This exercise has a bit of a wrinkle when describing the input parameter for the sample parameter-result pairs. When writing these out, we're going to get get a little closer to actual Python function invocation syntax because it is quite readable. Instead of saying, "*average of 3 returns 3*" in pure English, let's use something like this:

`average( 3 )` returns 3

where the parentheses group the sole argument.  Unfortunately, that syntax is not quite good enough.  For one thing, the average function takes a parameter whose data type is a list not just a number. Secondly, when there is more than one number in the list, we can't use a simple comma-separated list:

`average( 1, 2, 6 )` returns 4.5

That makes it look like the average function takes three parameters. Instead, let's group the numbers together using square brackets, which happens to be exactly how Python represents list, but also make sense in English:

`average( [1, 2, 6] )` returns 4.5

That definitely looks more like average takes a single, albeit complex, parameter. To specify an empty list then we can just use square brackets without any elements:

`average( [ ] )` returns 0

If we instead used `average( )`, it would look like the function doesn't take any arguments, which is incorrect.

**Exercise**: Create a program work plan that takes in a list of numbers and prints out the average using the `average` function we defined above.

The usual "accumulate sum of values" type processing steps get collapsed into just a single function invocation:

1. **Acquire data**
1. **Load data into a data structure**<br>
Load the numbers into a list in memory
1. **Normalize, clean, or otherwise prepare data**
1. **Process the data**<br>
Invoke `average` on the list of numbers
1. **Emit results**<br>
print the value returned from the `average` function

## Exercises

Reconsider the previous exercise that computed the average power to weight ratio from a [sample car data set](../data/cars.xls). If we want to write a program that identifies the maximum power to weight ratio for 8-cylinder cars, let's start by creating a function to help us out.

**Exercise**: Write a function work plan for function `max` that takes a list of numbers and returns the maximum value. Try to come up with two different plans for the processing steps. Hint: One of the plans uses an accumulator and the other does not.

**Exercise**: Write a program work plan to identify the max power-to-weight ratio (i.e., the most powerful car) among 8-cylinder cars using the `max` function you just defined.

## Return values versus printing

One of the big confusion points for students is the difference between return values and printing results. We'll look at this again when we translate plans to Python code, but it's important to understand this difference right away. 

Programs in the analytics world typically read data from a file and emit output or write data to another file. In other words, programs interact with the world outside of the program.  The world outside of the program is usually the network, the disk, or the screen.

In contrast, most functions that we write won't interact with the outside world.  Functions compute and return (give values back) to their caller. They don't print anything to the user unless explicitly asked to do so with a `print` statement.  (Later on, we will in fact build functions that process data files or emit complicated output.)

**Acknowledgments**. Again I'm deriving the function work plan here from [The Recurring Rainfall Problem](https://pdfs.semanticscholar.org/f772/087a1ef8f524cc2414c3b64636dd0b9985eb.pdf).
