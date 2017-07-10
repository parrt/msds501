# Functions (subprograms)

At this point, you should be getting pretty tired of repeating the sequence of operations in your program work plans that computes the average of some numbers:

* Use accumulator to sum the values<br>
* Use accumulator to count the values<br>
* If the count is 0, the average is 0 else compute the average as the sum divided by the count

The sequence is identical in all of the examples we've done so far; the only change is the list of numbers to which we apply the operations.  With some experience, we've learned to repeat that pattern every time we need to compute the average. It's exactly like learning to spit out the words for "*where is the subway?*" in a foreign language.

Now, let's bake that experience into a single entity, called a **function** or **procedure** or **method**, that formalizes the notion of reusing a sequence of operations.  For convenience, we're going to refer to this sequence by name, such as "*average*." Then, we can say things like "*average of unit prices*" or "*average of rainfall*" to apply the sequence of operations to a specific list.  For example, the processing steps for [rainfall average](plans/rainfall-average-plan.png) could be rewritten more simply as:

* Load the numbers into a list in memory
* Search for 999 in the list
* Slice out all numbers up to but not including 999’s position
* <s>Use accumulator to sum the values<br>
* Use accumulator to count the values<br>
* If the count is 0, the average is 0 else compute the average as the sum divided by the count</s>
* **Invoke *average* on the rainfall subset**
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

Instead of loading data from the disk, functions operate on data given to them from the invoking program. This incoming data is analogous to a recipe's list of ingredients and is specified in the form of one or more named *parameters* (also called *arguments*). Instead of printing a result or displaying a graph, as a program would, functions *return* values. Functions are meant as helper routines that are generically useful.

We begin planning a function by identifying:
 
1. a descriptive function name
2. the kind of value(s) it operates on (parameter types)
3. the kind of value it returns (return type)
4. what the function does and the value it returns

If we can't specifying exactly what goes in and out of the function, there's no hope of determining the processing steps, let alone Python code, to implement that function.

As with the program work plan, we then manually write out some sample function invocations to show what data goes in and what data comes out. 

Once we fully understand our goal, we plan out the sequence of operations needed by the function to compute the desired result.  As when designing a whole program, we start with the return value and work our way backwards, identifying operations in reverse order. Note: The operations should be purely a function of the data passed to them as parameters---functions should be completely ignorant of any other data. (More on this when we actually translate function pseudocode to Python.) 

**Exercise**. Fill out a [Function work plan](plans/function-planning.pdf) for a function that computes *y = x + 2*. ([solution](plans/line-function-plan.pdf))

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

This plan only gives us two X/Y points on a line. We might want to compute the Y-coordinate for a whole list of X coordinates.

**Exercise**: See if you can figure out the program work plan for a variation that accepts a list of numbers, rather than a predefined set of just 2 X values.

Fleshing out the objective a bit, we could say, "*Collect and print the results of invoking the line function on each element of an X coordinate list*."

In this case, our sample input-output pairs for the program might look like:

2 → 4<br>
-3, 0, 2, 10 → -1, 2, 4, 12<br>
 → 

where the last line means that an empty list gets no output.

To identify the processing steps, we work backwards from the results step: "*print out the Y coordinates*." We get the Y coordinates using a map operation that applies the `line` function to each X coordinate in the list.  Before that, we need to load the X coordinates into a list in memory. It helps to look at the operation visually:

<img src=images/XY.png width=300>

The only difference between this map operation and what we've seen previously is that we are applying a function that *we* implemented, instead of a built-in operator like multiply.

The processing steps of the program work plan looks like this:

1. **Acquire data**
1. **Load data into a data structure**<br>
Load the X coordinates into a list in memory
1. **Normalize, clean, or otherwise prepare data**
1. **Process the data**<br>
Use map operation to apply `line` function to each element of the list, yielding a new list of Y coordinates
1. **Emit results**<br>
print out the Y coordinates

## Invoking Functions with list parameters

Now let's work on a function that takes a list instead of a number as a parameter.  Specifically, let's get our work plan for averaging numbers into a reusable function. That way, in the future, we can say things like "*average of weights*" or, more succinctly, "*average(weights)*".

**Exercise**. Fill out a [Function work plan](plans/function-planning.pdf) for a function that computes the average of some numbers. ([solution](plans/average-function-plan.pdf))

**Exercise**: Create a program work plan that takes in a list of numbers and prints out the average using the `average` function we just defined.

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

Reconsider the [previous exercise](planning.md#power) that computed the average power to weight ratio from a [sample car data set](../data/cars.xls). Let's say we want to write a program that identifies the maximum power to weight ratio for 8-cylinder cars, let's start by creating a function to help us out.

**Exercise**: Write a function work plan for function `max` that takes a list of numbers and returns the maximum value. Try to come up with two different plans for the processing steps. Hint: One of the plans uses a [max value accumulator](operations.md#accumulate) and the other does not.

**Exercise**: Write a program work plan to identify the max power-to-weight ratio (i.e., the most powerful car) among 8-cylinder cars using the `max` function you just defined.

## Return values versus printing

One of the big confusion points for students is the difference between return values and printing results. We'll look at this again when we translate plans to Python code, but it's important to understand this difference right away. 

Programs in the analytics world typically read data from a file and emit output or write data to another file. In other words, programs interact with the world outside of the program.  The world outside of the program is usually the network, the disk, or the screen.

In contrast, most functions that we write won't interact with the outside world.  Functions compute and return (give values back) to their caller. They don't print anything to the user unless explicitly asked to do so with a `print` statement.  (Later on, we will in fact build functions that process data files or emit complicated output.)

**Acknowledgments**. Again I'm deriving the function work plan here from [The Recurring Rainfall Problem](https://pdfs.semanticscholar.org/f772/087a1ef8f524cc2414c3b64636dd0b9985eb.pdf).
