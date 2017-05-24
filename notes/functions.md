# Functions (subprograms)

At this point, you should be getting pretty tired of repeating the sequence of operations in your program work plans that computes the average of some numbers:

* Use accumulator to sum the values<br>
* Use accumulator to count the values<br>
* If the count is 0, the average is 0 else compute the average as the sum divided by the count

The sequence is identical in all of the examples we've done so far; the only change is the list of numbers to which we apply the sequence.  

With some experience, we've learned to repeat that sequence every time we need to compute the average.  

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

**name**: snow<br>
**ingredients**: multiple ice cubes<br>
**result**: snow<br>
**steps**:
* put ice in blender
* turn on blender for 10 seconds.

 Functions are just like that except that the sequence of operations has to be more precise, since we will ultimately need to have an intolerant computer execute the sequence.

Let's come up with a few

sin(x)
double(x)

cow(grass) = milk

recipes

That reminds me of the old joke: *Never try to teach a pig to sing. It doesn't work and it annoys the pig.*

## Functions are subprograms

A sequence of operations grouped into a single, named entity is called a **function**. Functions are like mini programs or subprograms that we can plan out just like full programs. Instead of loading data from the disk, functions operate on data passed to it from the invoking program. This incoming data is in the form of one or more named *parameters* (also called *arguments*). Instead of printing a result or displaying a graph, functions *return* values.

When planning a function, the first thing we have to determine is:

1. a descriptive function name
2. the kind of value(s) it operates on (parameter types)
3. the kind of value it returns (return type)
4. what the function does

These function planning steps are essentially the first two steps from our program problem-solving strategy where we decide what kind of input we have and what the expected result is.
 
See the full [Function work plan](plans/function-planning.pdf).

To describe our "compute the average" functionality, we could say: function `average` takes a list of numbers as a parameter and returns a number that is the average of the numbers in the list.





print vs return. output of the overall program versus result of a function

left = right + right + right [Myth Busters' Turn Left Myth](https://www.youtube.com/watch?v=ppCz4f1L9iU)

[Power to weight ratio](average-power-to-weight-ratio.md)

**Acknowledgments**. Again I'm deriving the function work plan here from [The Recurring Rainfall Problem](https://pdfs.semanticscholar.org/f772/087a1ef8f524cc2414c3b64636dd0b9985eb.pdf).