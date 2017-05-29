# Model of Computation

*in progress*

In order to make it easier to learn the overall process of program and function planning, we've limited the set of possible operations to a set of common [programming patterns](patterns.md). As with natural language, however, the set of possible program operations is effectively infinite. We can mix and match simple operations to create more complex behavior or tweak common patterns to suit a specific problem.

Before dropping all the way down to the level of programming language syntax, let's explore the simplest, fine-grained operations that a computer can perform. Ultimately, it is these operations we will draw from to design programs. We're going to stick with pseudocode for now because the precise syntax isn't necessary to learn the computation model. The concepts apply across most programming leverages.

## Canonical processor operations

As we saw in [Representing data in memory](data-in-memory.md), a computer's memory holds data temporarily while the processor works on that data. We typically load data into memory from the disk and organize it into a structure that is suitable for the computation we'd like to perform. In the end, though, memory just holds data. All of the action happens in the computer processor (CPU), which has five principal operations:
 
* load small chunks of data from memory into the CPU
* perform arithmetic computations on data in the CPU
* conditionally perform computations
* repeat operations
* store small chunks of data back to memory

Processors execute low-level *machine instructions* that perform one or more of those principal operations. Each instruction does a tiny amount of work (like adding two numbers) but the processor can do them extremely fast, on the order of billions a second.   Writing a program in these low-level machine instructions would be extremely tedious, so we typically use programming languages such as Python to make our lives easier.

To give you an idea of just how low-level these machine operations are, consider the following simple pseudocode operation (which has a direct Python equivalent).
 
*let total be cost + tax*

Even something this simple requires the processor to execute multiple low-level instructions.  The processor must load `cost` and `tax` from memory, add the two values, then store the result back into memory at the address associated with `total`.

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

### Conditional execution

Some recipes give conditional instructions, such as

*if not sweet enough, add some sugar*

Similarly, processors can conditionally execute one or a group of operations. For example, if there is only sales tax on books, we might use a pseudocode statement like:

*if item is a book then let total be cost + tax*

or, equivalently,

*let total be cost + tax if item is a book*

Conditional statements execute only if the conditional expression is true. There is also a variant that executes operations in both cases. For example, we can express how to find the larger of two values, x and y, as:

*if x > y then let max be x*<br>
*else let max be y*

We can also execute a group of operations conditionally. For example, we might do something like this:

*if item is a book then:*<br>
&nbsp;&nbsp;&nbsp;&nbsp;*remove book from inventory list*<br>
&nbsp;&nbsp;&nbsp;&nbsp;*let total be cost + tax*

That is equivalent to this more awkward version:

*if item is a book then remove book from inventory list*<br>
*if item is a book then let total be cost + tax*

The key elements of a conditional statement are: the conditional expression and the operation(s) to perform if true. For the else-clause variant, we have the conditional expression, the operation to perform if true, and the operation to perform if the condition is false. When mapping a real-world problem to a conditional statement, your goal is to identify the conditional expression and the operations. A template for conditional execution looks like:

if *condition*:<br>
&nbsp;&nbsp;&nbsp;&nbsp;*operation 1*<br>
&nbsp;&nbsp;&nbsp;&nbsp;*operation 2*<br>
&nbsp;&nbsp;&nbsp;&nbsp;...

or

if *condition*:<br>
&nbsp;&nbsp;&nbsp;&nbsp;*operation 1*<br>
&nbsp;&nbsp;&nbsp;&nbsp;*operation 2*<br>
&nbsp;&nbsp;&nbsp;&nbsp;...<br>
else:<br>
&nbsp;&nbsp;&nbsp;&nbsp;*operation 1*<br>
&nbsp;&nbsp;&nbsp;&nbsp;*operation 2*<br>
&nbsp;&nbsp;&nbsp;&nbsp;...

### Repeated execution

Conditional execution is kind of like executing an operation zero or one times. We also want to execute operations multiple times, just like we do in a recipe.  For example, in a 
[recipe for risotto](http://allrecipes.com/recipe/85389/gourmet-mushroom-risotto/), we'll typically find a repeated operation like:

> Add 1/2 cup broth to the rice, and stir until the broth is absorbed. 

Bending this more towards pseudocode, we might say:

*add 1/2 cup broth to rice in pot*<br>
*repeat until broth is absorbed:*<br>
&nbsp;&nbsp;&nbsp;&nbsp;*stir rice in pot*<br>

or, equivalently,

*add 1/2 cup broth to rice in pot*<br>
*while broth not absorbed:*<br>
&nbsp;&nbsp;&nbsp;&nbsp;*stir rice in pot*<br>

In the programming world, we call this a *loop*. The key elements of a loop are the condition expression and the operation(s) to perform while the condition is true. When trying to map a real-world problem to a loop, your goal is to identify the condition and the repeated steps. A template for a loop looks like:

while *condition*:<br>
&nbsp;&nbsp;&nbsp;&nbsp;*operation 1*<br>
&nbsp;&nbsp;&nbsp;&nbsp;*operation 2*<br>
&nbsp;&nbsp;&nbsp;&nbsp;...

There is an important implicit understanding about the operations in a loop: The operations in the loop alter the condition. Otherwise, the loop would never terminate. For example, here is an *infinite loop* that prints "hi" forever.

*while true*:<br>
&nbsp;&nbsp;&nbsp;&nbsp;*print "hi"*<br>

Because the print statement does not alter the condition, *true*, the loop does not terminate.  As an example of a more proper loop, we might want to print "hi" 5 times. 

*init a counter to 1*<br>
*while counter <= 5*:<br>
&nbsp;&nbsp;&nbsp;&nbsp;*print "hi"*<br>
&nbsp;&nbsp;&nbsp;&nbsp;*add 1 to counter*<br>

In this case, the condition is altered by the "*add 1 to counter*" operation in the loop. When the counter gets to 6, the conditional expression will be false in the loop will terminate.

### Nested loops

We can also repeat repeated instructions, which we call a *nested loop*. For example, the risotto recipe goes on to say:

> Continue adding broth 1/2 cup at a time, stirring continuously, until the liquid is absorbed and the rice is *al dente*, about 15 to 20 minutes.

We are supposed to add broth until we run out of it, 1/2 cup at a time.  For each 1/2 cup we add, we are to stir until it is absorbed. Making the recipe more precise, we might express it like this as a nested loop:

*while there is more broth:*<br>
&nbsp;&nbsp;&nbsp;&nbsp;*add 1/2 cup broth to pot*<br>
&nbsp;&nbsp;&nbsp;&nbsp;*while broth not absorbed:*<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*stir rice in pot*

This pops out from our loop template by identifying the two conditional expressions and the loop operations.

### For-each loops

We also see a different kind of loop that *iterates* through a sequence of elements, such as a list. For example, a recipe might say "*chop each ingredient into small pieces*." In pseudocode, we would write:

*for each ingredient in ingredient list:*<br>
&nbsp;&nbsp;&nbsp;&nbsp;*chop ingredient into small pieces*

(Remember that our goal is to identify the conditional and the operation(s) to repeat.)

Or, even closer to actual code, we might give a name to the iterated ingredient:

*for each ingredient x in ingredient list:*<br>
&nbsp;&nbsp;&nbsp;&nbsp;*chop x into small pieces*

The value of *x* takes on each ingredient value, one after the other.  Referring back to our discussion of traversing data structures, we iterated through a list of quantities:

<img src=images/int-list-item.png width=230>

A pseudocode loop implements the implied movement in the visualization:

*for each quantity in Quantity list*:<br>
&nbsp;&nbsp;&nbsp;&nbsp;*do something*

For example, to print out each quantity in the list, we could write:

*for each quantity in Quantity list*:<br>
&nbsp;&nbsp;&nbsp;&nbsp;*print quanity*

### Indexed loops

Using the for-each kind of loop, we can rephrase the counter loop from above more simply:

*for each value i in set 1..5*:<br>
&nbsp;&nbsp;&nbsp;&nbsp;*print "hi"*

There are 5 elements in the set 1..5 and so the for-each loop goes around 5 times. In this case, the loop operation doesn't use the iterated value, *i*, but *i*'s value would be available to any operation(s) that needed it.

We tend to use such loops that iterate through a range of integers when traversing multiple lists at the same time. (To traverse a single list, we'd use the for-each loop.) For example, recall the visualization from the [combine programming pattern](patterns.md#combine):

<img src=images/map-mult.png width=490>

We can implement that pattern using a loop. At each time step, the loop operation needs to examine the same position in two lists. Because Python starts list indexing and 0, let's stick with that convention and iterate from index 0 to *n*-1 for *n* elements in the lists.

*for each value i in set 0..n-1*:<br>
&nbsp;&nbsp;&nbsp;&nbsp;*let ith Cost be ith Quantity times ith Unit Price*

## Rephrasing programming patterns

The common programming patterns we saw from before, map down to these simpler operations.

## Summary

In the end, any program will consist of these canonical operations. 