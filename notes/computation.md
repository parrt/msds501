# Model of Computation

*in progress*

In order to make it easier to learn the overall process of program and function planning, we've limited the set of possible operations to a set of common [programming patterns](patterns.md). As with natural language, however, the set of possible program operations is effectively infinite. We can mix and match simple operations to create more complex behavior or tweak common patterns to suit a specific problem.

Before dropping all the way down to the level of programming language syntax, let's explore the simplest, fine-grained operations that a computer can perform. Ultimately, it is these operations we will draw from to design programs. We're going to stick with pseudocode for now because the precise syntax isn't necessary to learn the computation model. The concepts apply across most programming leverages.

## Canonical processor operations

As we saw in [Representing data in memory](data-in-memory.md), a computer's memory holds data temporarily while the processor works on that data. We typically load data into memory from the disk and organize it into a structure that is suitable for the computation we'd like to perform. In the end, though, memory just holds data. All of the action happens in the computer processor (CPU), which performs five principal operations:
 
* load small chunks of data from memory into the CPU
* perform arithmetic computations on data in the CPU
* store small chunks of data back to memory
* conditionally perform computations
* repeat operations

Processors execute low-level *machine instructions* that perform one or more of those principal operations. Each instruction does a tiny amount of work (like adding two numbers) but the processor can do them extremely fast, on the order of billions a second.   Writing a program in these low-level machine instructions would be extremely tedious, so we typically use programming languages such as Python to make our lives easier.

To give you an idea of just how low-level these machine operations are, consider the following simple pseudocode operation (which has a direct Python equivalent).
 
*let total be cost + tax*

Even something this simple requires the processor to execute multiple low-level instructions.  The processor must load *cost* and *tax* from memory, add the two values, then store the result back into memory at the address associated with *total*.

### Order of operations

Unless given instructions to the contrary, the processor keeps executing instructions one after the other. For example, given the following pseudocode sequence, a processor would execute the *let* statement and then execute the *print*.

*let total be cost + tax*<br>
*print total*

The notion of doing a sequence of operations in order is familiar to us from cooking with recipes. For example, a recipe might direct us to:

*put ingredients in bowl*<br>
*mix ingredients together*<br>
*pour into baking pan*<br>
*bake at 375 degrees for 40 minutes*

We naturally assume the steps are given in execution order.

## Conditional execution

Some recipes give conditional instructions, such as

*if not sweet enough, add some sugar*

Similarly, processors can conditionally execute one or a group of operations. For example, if sales tax is only computed on books, we might use a pseudocode statement like:

*if item is a book: let total be cost + tax*

Conditional operations execute only if the conditional expression is true. **To be clear, the processor does not execute all of the operations present in the program**. "*let total be cost + tax*," in this case, is present in the program but not always executed.

When mapping a real-world problem to a conditional statement, your goal is to identify these key elements:

1. the conditional expression
1. the operation(s) to perform if the condition is true

A template for conditional execution looks like:

if *condition*:<br>
&nbsp;&nbsp;&nbsp;&nbsp;*operation 1*<br>
&nbsp;&nbsp;&nbsp;&nbsp;*operation 2*<br>
&nbsp;&nbsp;&nbsp;&nbsp;...

The condition must be actionable by a computer. For example, the condition "*the cat is hungry*" is not actionable by computer because there's nothing in its memory a computer can test that is equivalent to the cat being hungry. Conditions almost always consist of equality or relational operators for arithmetic, such as "cost > 10", "cost + tax &lt; 100", or "quantity = 4".

It's time to introduce a new data type: **boolean**, which holds either a true or false value. The result (value) of any equality or relational operator is boolean. For example, "3>2" evaluates to true but "3>4" evaluates to false.

**Exercise**:  Design a conditional in pseudocode for the following situation. "Print a name if the length of the name is greater than zero." You can compute the length of some *x* with *len(x)*.

In some cases, we want to execute an operation in either case, one operation if the condition is true and a different operation if the condition is false.  The template looks like this:

if *condition*:<br>
&nbsp;&nbsp;&nbsp;&nbsp;*operation 1*<br>
&nbsp;&nbsp;&nbsp;&nbsp;*operation 2*<br>
&nbsp;&nbsp;&nbsp;&nbsp;...<br>
else:<br>
&nbsp;&nbsp;&nbsp;&nbsp;*operation 1*<br>
&nbsp;&nbsp;&nbsp;&nbsp;*operation 2*<br>
&nbsp;&nbsp;&nbsp;&nbsp;...

For example, we can express a conditional operation to find the larger of two values, *x* and *y*, as:

*if x > y: let max be x*<br>
*else: let max be y*

We can also execute a group of operations conditionally, such as:

*if item is a book:*<br>
&nbsp;&nbsp;&nbsp;&nbsp;*remove book from inventory list*<br>
&nbsp;&nbsp;&nbsp;&nbsp;*let total be cost + tax*

That is equivalent to this more awkward version:

*if item is a book: remove book from inventory list*<br>
*if item is a book: let total be cost + tax*

Conditional execution is kind of like executing an operation zero or one times, depending on the conditional expression.  We also want to execute operations multiple times.

## Repeated execution

In recipes, such as a [recipe for risotto](http://allrecipes.com/recipe/85389/gourmet-mushroom-risotto/), we'll typically find a repeated operation like:

> Add 1/2 cup broth to the rice, and stir until the broth is absorbed. 

In this case, the "stir" operation is repeated until the condition is met (or while the condition is not met). Bending the recipe more towards pseudocode, we might say:

*add 1/2 cup broth to rice in pot*<br>
*repeat until broth is absorbed:*<br>
&nbsp;&nbsp;&nbsp;&nbsp;*stir rice in pot*<br>

or, equivalently,

*add 1/2 cup broth to rice in pot*<br>
*while broth is not absorbed:*<br>
&nbsp;&nbsp;&nbsp;&nbsp;*stir rice in pot*<br>

(*repeat* and *while* are duals of each other and are equivalent when the conditions are inverted.)

In the programming world, we call this a **loop**.  

Just as with the conditional execution, mapping a real-world problem to a loop means identifying two key elements: a conditional (boolean) expression and the operation(s) to repeat.  A template for a loop looks like:

while *condition*:<br>
&nbsp;&nbsp;&nbsp;&nbsp;*operation 1*<br>
&nbsp;&nbsp;&nbsp;&nbsp;*operation 2*<br>
&nbsp;&nbsp;&nbsp;&nbsp;...

There is an important implicit understanding about the operations in a loop: **At least one operation in the loop alters the condition.** Otherwise, the loop would never terminate. For example, here is an *infinite loop* that prints "hi" forever.

*while true*:<br>
&nbsp;&nbsp;&nbsp;&nbsp;*print "hi"*<br>

Because the print statement does not alter the condition, *true*, the loop does not terminate.  As an example of a more proper loop, we might want to print "hi" 5 times. 

*init a counter to 1*<br>
*while counter <= 5*:<br>
&nbsp;&nbsp;&nbsp;&nbsp;*print "hi"*<br>
&nbsp;&nbsp;&nbsp;&nbsp;*add 1 to counter*<br>

In this case, the condition is altered by the "*add 1 to counter*" operation in the loop. When the counter gets to 6, the conditional expression will be false and the loop will terminate.

That counter loop is an example of an [accumulator](patterns.md#accumulator).

**Exercise**: Write a pseudocode loop to sum the integers from 1 to 8, inclusively.

### For-each loops

We also see a different kind of loop that *iterates* through a sequence of elements, such as a list. For example, a recipe might say "*chop each ingredient into small pieces*." In pseudocode, we could write:

*for each ingredient in ingredient list:*<br>
&nbsp;&nbsp;&nbsp;&nbsp;*chop ingredient into small pieces*

(Remember that our goal is to identify the conditional and the operation(s) to repeat.)

Or, even closer to actual code, we might give a name to the iterated ingredient:

*for each ingredient x in ingredient list:*<br>
&nbsp;&nbsp;&nbsp;&nbsp;*chop x into small pieces*

The value of *x* takes on each ingredient value, one after the other.  Referring back to our discussion of traversing data structures, we iterated through a list of quantities:

<img src=images/int-list-item.png width=230>

A pseudocode loop implementing the implied movement in the visualization looks like:

*for each quantity in Quantity list*:<br>
&nbsp;&nbsp;&nbsp;&nbsp;*do something*

For example, to print out each quantity in the list, we could write:

*for each quantity in Quantity list*:<br>
&nbsp;&nbsp;&nbsp;&nbsp;*print quanity*

The template for a for-each loop looks like:

for each *x* in *sequence*:<br>
&nbsp;&nbsp;&nbsp;&nbsp;*operate on x*

where *sequence* is typically a list or set.

The [map](patterns.md#map) pattern used the following image to visualize the operations:

<img src=images/map-discount-op.png width=390>

We could implement that pattern using:

*for each price in UnitPrice list*:<br>
&nbsp;&nbsp;&nbsp;&nbsp;<i>add price * 0.95 to Discounted list</i>

**Exercise**: Write a pseudocode loop for an [accumulator](patterns.md#accumulator) that sums the numbers in a Quantity list.

### Indexed loops

Using the for-each kind of loop, we can rephrase the 1 to 5 counter loop from above more simply as:

*for each value i in set 1..5*:<br>
&nbsp;&nbsp;&nbsp;&nbsp;*print "hi"*

There are 5 elements in the set 1..5 and so the for-each loop goes around 5 times. In this case, the loop operation doesn't use the iterated value, *i*, but *i*'s value would be available to any operation(s) that needed it.

**Exercise**: Write a pseudocode indexed-loop to print the numbers from 5 to 10, inclusively.

Indexed loops are more general than the for-each loops. For example, this loop:

*for each quantity in Quantity list*:<br>
&nbsp;&nbsp;&nbsp;&nbsp;*print quanity*

is equivalent to:

*for each value i in set 0..n-1*:<br>
&nbsp;&nbsp;&nbsp;&nbsp;*print Quantity<sub>i</sub>*

where *Quantity<sub>i</sub>* is the *i<sup>th</sup>* value of Quantity.

Because Python starts list indexing at 0, let's stick with that convention and that loop iterates from index 0 to *n*-1 for *n* elements in the lists. The length of Quantity is expressed as *len(Quantity)*.

We tend to use indexed loops, that iterate through a range of integers, when traversing multiple lists at the same time. (To traverse a single list, we'd normally use a for-each loop.) For example, recall the visualization from the [combine programming pattern](patterns.md#combine):

<img src=images/map-mult.png width=490>

We can implement that pattern using an indexed loop. At each time step, the loop operation needs to examine the same position in two lists. 

*for each value i in set 0..n-1*:<br>
&nbsp;&nbsp;&nbsp;&nbsp;<i>let Cost<sub>i</sub> be Quantity<sub>i</sub> * UnitPrice<sub>i</sub></i>

**Exercise**: Using an indexed-loop, write pseudocode to [slice](patterns.md#slice) elements in range [0 to 5), indexes (0,1,2,3,4), from a rainfall list into a new list somerainfall.

## Combining operations

As with natural language, we can combine any of the basic sentence structures to form more complex sentences. In the programming world, that means **nesting** one operation in another. In this section, we'll explore a few of the interesting combinations.

### Nested loops

We sometimes need to repeat repeated instructions, which we call a *nested loop*. For example, the risotto recipe goes on to say:

> Continue adding broth 1/2 cup at a time, stirring continuously, until the liquid is absorbed and the rice is *al dente*, about 15 to 20 minutes.

We are supposed to add broth until we run out of it, 1/2 cup at a time.  For each 1/2 cup we add, we are to stir until it is absorbed. Making the recipe more precise, we might express it like this as a nested loop:

*while there is more broth:*<br>
&nbsp;&nbsp;&nbsp;&nbsp;*add 1/2 cup broth to pot*<br>
&nbsp;&nbsp;&nbsp;&nbsp;*while broth not absorbed:*<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*stir rice in pot*

We are wrapping our previous loop in an outer loop. This code pops out from our loop template by identifying the two conditional expressions and the loop operations.

In the analytics world, nested loops are hugely important because we use them to process matrices, images, and tables of data.

Let's get started by summing the numbers in a 3x3 matrix:

<img src=images/matrixA.png width=100>

Recall that, while we can look at the entire matrix at once, a computer examines each element one-by-one. Because this is not a one-dimensional data structure, we can't use a simple "for each element in the matrix" loop. The most common template for iterating through all elements of an *n* x *m* matrix looks like this:

*for i in 0..n-1:*<br>
&nbsp;&nbsp;&nbsp;&nbsp;*for j in 0..m-1:*<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*do something with matrix<sub>i,j</sub>*

where *matrix<sub>i,j</sub>* accesses the element at row *i* and column *j*.  Such a nested loop gives all possible combinations of *i* and *j*, which is what we want when we operate on a matrix. Consider the following use of that template to print out all of the two-dimensional indices:

*for i in 0..n-1:*<br>
&nbsp;&nbsp;&nbsp;&nbsp;*for j in 0..m-1:*<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*print j without newline*<br>
&nbsp;&nbsp;&nbsp;&nbsp;print a newline

The output would be *n* rows of `0 1 2 ... m-1`:

```
0 1 2 ... m-1
0 1 2 ... m-1
...
```

To sum all of the elements of a 3x3 matrix, we let *n*=3 and *m*=3 and use an addition operation:

*init sum to 0*<br>
*for i in 0..2:*<br>
&nbsp;&nbsp;&nbsp;&nbsp;*for j in 0..2:*<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*add matrix<sub>i,j</sub> to sum*

You might recognize this as a 2D form of an accumulator pattern.

As a more realistic example, let's add two matrices A and B together to form C. The key operation is to add A<sub>i,j</sub> to B<sub>i,j</sub> to get C<sub>i,j</sub>. Visually, it looks like this:

<img src=images/ABC.png width=360>

**Exercise**: Write out the pseudocode nested indexed-loop to add matrices together.

<img src=images/obama-zoom.png width=400>

<img src=images/rows.png width=700>


### Conditional in a loop

One of the most common nested operations is a conditional inside of a loop. We use it to implement the [filter](patterns.md#filter) pattern, for example. The filter template looks like:

for each *x* in *a sequence*:<br>
&nbsp;&nbsp;&nbsp;&nbsp;if *condition*: add *x* to new list<br>

To convert a real-world filtering problem to pseudocode, your goal is to identify the sequence and the condition in that template. To filter out negative values (filter in nonnegative values) as we did in the rainfall problem, the *sequence* is the rainfall list and the *condition* is "*x >= 0*":

*for each x in rainfall*:<br>
&nbsp;&nbsp;&nbsp;&nbsp;*if x>=0: add x to new list*<br>

## Summary

In the end, any program will consist of these canonical operations. 