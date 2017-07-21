# Model of Computation

In order to make it easier to learn the overall process of program and function planning, we've limited the set of possible operations to a set of common [programming operations](operations.md). As with natural language, however, the set of possible program operations is effectively infinite. We can mix and match simple operations to create more complex behavior or tweak common operations to suit a specific problem.

Before dropping all the way down to the level of programming language syntax, let's explore the simplest, fine-grained operations that a computer can perform. Ultimately, we will draw from those operations to design programs.  Programmers think in terms of high-level operations, such as *map* or *filter*, but our fingers type fine-grained code patterns associated with those high-level operations.

We're going to stick with pseudocode for now because the precise syntax isn't necessary to learn the computation model. The concepts apply across most programming languages.

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

Even something this simple requires the processor to execute multiple low-level instructions.  The processor must look at the values of *cost* and *tax* in memory, add the two values, then store the result back into memory at the address associated with *total*.

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

It's time to introduce a new data type: **boolean**, which holds either a true or false value. The result (value) of any equality or relational operator is boolean. For example, "3>2" evaluates to true and "3>4" evaluates to false.

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

**Exercise**: Chain multiple IF statements together to print A if a `grade` is 90-100, B if `grade` is 80-89, or C if `grade` is 70-79.

Conditional execution is kind of like executing an operation zero or one times, depending on the conditional expression.  We also need to execute operations multiple times in some cases.

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

*loop setup, usually init counter or value to update in loop*<br>
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

That counter loop is an example of an [accumulator](operations.md#accumulator).

**Exercise**: Write a pseudocode WHILE loop to sum the integers from 1 to 8, inclusively.

Another common analytics operation to add to our list (like map, search, etc...) is perhaps called "iterative computation". Basically we use a loop to iterate through a computation until we reach a desired result. The operation as an implied iterated value, just like the accumulator has an accumulated value. In fact, iterative computations often have both an iterative value and an accumulator, such as a counter.

For example, to compute the integer component of, say, *log<sub>2</sub>(n)* we can repeatedly divide *n* by 2 until we reach 1. The number of times we can divide a number by 2 is the log<sub>2</sub> by definition, though we are ignoring fractional part of the correct result. Here is the pseudocode:

*init a counter to 0*<br>
*while n>1*:<br>
&nbsp;&nbsp;&nbsp;&nbsp;*let n be n / 2*<br>
&nbsp;&nbsp;&nbsp;&nbsp;*add 1 to counter*<br>
*print "log is " counter*

Notice how if n is 1, the loop is never entered and we print a counter of zero, which is the right answer for *log<sub>2</sub>(1)*.

**Exercise**: Fill in a [Function work plan](plans/function-planning.pdf) to create a function that uses that pseudocode as the processing steps to compute the result. Hint: what needs to change to convert this from a program to a function?

**Exercise**: Fill in a [Function work plan](plans/function-planning.pdf) for with a functioning that performs integer division of 2 parameters, x and y, by counting how many times we can subtract y from x while the iterated value is greater or equal to the divisor y. You will need a counter and an interated value. The point to this exercise is for you to see a pattern after solving a similar problem to the log2 function.

<!--
```
def div(x,y):
	counter = 0
	n = x
	while n>=y:
		n = n - y
		counter += 1
	return counter
```
-->

### For-each loops

We also see a different kind of loop that *iterates* through a sequence of elements, such as a list. It is the implementation of choice for the map operation. For example, a recipe might say "*chop each of the ingredients*." In pseudocode, we could write:

*for each ingredient in ingredients list:*<br>
&nbsp;&nbsp;&nbsp;&nbsp;*chop ingredient*

Or, even closer to actual code, we might give a name to the iterated ingredient:

*for each ingredient x in ingredients list:*<br>
&nbsp;&nbsp;&nbsp;&nbsp;*chop x into small pieces*

With this code pattern, our goal is to find a good iterated variable named, identify the conditional, and then identify the operation(s) to repeat. The template for a for-each loop looks like:

for each *x* in *sequence*:<br>
&nbsp;&nbsp;&nbsp;&nbsp;*operate on x*

The value of *x* takes on each sequence/list value, one after the other.  Referring back to our discussion of traversing data structures, we iterated through a list of quantities:

<img src=images/int-list-item.png width=230>

A pseudocode loop implementing the implied movement in the visualization looks like:

*for each quantity in Quantity list*:<br>
&nbsp;&nbsp;&nbsp;&nbsp;*do something with quantity*

For example, to print out each quantity in the list, we could write:

*for each quantity in Quantity list*:<br>
&nbsp;&nbsp;&nbsp;&nbsp;*print quanity*



where *sequence* is typically a list or set. To use this pseudocode pattern, we have to identify a decent iterated variable name, the sequence, and the operations to repeat.

The [map](operations.md#map) operation used the following image to visualize the operations:

<img src=images/map-discount-op.png width=390>

We could implement that operation using:

*let Discounted be an empty list*<br>
*for each price in UnitPrice list*:<br>
&nbsp;&nbsp;&nbsp;&nbsp;<i>add price * 0.95 to Discounted list</i>

**Exercise**: Write a pseudocode loop for an [accumulator](operations.md#accumulator) that sums the numbers in a Quantity list.

**Exercise**: Write a pseudocode loop for the even-odd accumulator:

<img src=images/accumulator-even-odd.png width=320>

You can use "is even" and "is odd" to test values.

### Indexed loops

Using the for-each kind of loop, we can rephrase the 1 to 5 counter while-loop from above more simply as:

*for each value i in set 1..5*:<br>
&nbsp;&nbsp;&nbsp;&nbsp;*print "hi"*

There are 5 elements in the set 1..5 and so the for-each loop goes around 5 times. In this case, the loop operation doesn't use the iterated value, *i*, but *i*'s value would be available to any operation(s) that needed it.

The template for an indexed loop looks like:

for each value *i* in *integer_set or range*:<br>
&nbsp;&nbsp;&nbsp;&nbsp;*operation 1*<br>
&nbsp;&nbsp;&nbsp;&nbsp;*operation 2*<br>
&nbsp;&nbsp;&nbsp;&nbsp;...

Indexed loops are more general than the for-each loops. For example, this loop:

*for each quantity in Quantity list*:<br>
&nbsp;&nbsp;&nbsp;&nbsp;*print quanity*

is equivalent to:

*for each value i in set 0..n-1*:<br>
&nbsp;&nbsp;&nbsp;&nbsp;*print Quantity<sub>i</sub>*

where *Quantity<sub>i</sub>* is the *i<sup>th</sup>* value of Quantity and *n* is the length of the Quantity list.  The difference is that the indexed loop has access to the loop iterator variable *i* and the for-each loop does not.

**Exercise**: Given a `names` list, write a pseudocode indexed loop to print the elements of the list prefixed by their index starting at 0. Assume `len(names)` gives the length. For example:

```
0. bob
1. mary
2. xue
```

We tend to use indexed loops, that iterate through a range of integers, when traversing multiple lists at the same time. (To traverse a single list, we'd normally use a for-each loop.) For example, recall the visualization from the [combine programming operation](operations.md#combine):

<img src=images/map-mult.png width=490>

We can implement that operation using an indexed loop. At each time step, the loop operation needs to examine the same position in two lists. 

*let Cost be a list*<br>
*for each value i in set 0..n-1*:<br>
&nbsp;&nbsp;&nbsp;&nbsp;<i>let Cost<sub>i</sub> be Quantity<sub>i</sub> * UnitPrice<sub>i</sub></i>

Keep in mind that, when we get to Python code, ranges are inclusive on the left and exclusive on the right; `range(0,5)` is 0..4 inclusively.

**Exercise**: Using an indexed-loop, write pseudocode to [slice](operations.md#slice) elements in range [0 to 5), indexes (0,1,2,3,4), from a list `x` into a new list `y`. Hint: You'll need: "*add ... to y*".

### Translating formulas

Sigma notation from mathematics translates in a straightforward fashion to indexed loops. For example:

<img src=images/formula-translation.png width=490> 

We pick elements from the summations and insert them into the template for an indexed loop.

## Summary

Other than transferring data to and from memory, processors primarily perform arithmetic operations, such as "cost + tax".  Processors can also conditionally or repeatedly execute operations.

When mapping real-world problems to pseudocode, you'll follow the program or function work plan and eventually work backwards from the desired result to identify a suitable sequence of operations. These operations will either map to our high level [programming operations](operations.md) or to the lower level pseudocode patterns described here.

If you can't identify a higher level operation for a piece of the problem, try to map it to a conditional operation or a loop around one or more operations.

For conditionals, you have to identify the conditional Boolean expression and the operation or operations that should be executed conditionally:

if *condition*:<br>
&nbsp;&nbsp;&nbsp;&nbsp;*operation 1*<br>
&nbsp;&nbsp;&nbsp;&nbsp;*operation 2*<br>
&nbsp;&nbsp;&nbsp;&nbsp;...

If you need to execute code in case that condition fails, use this template:

if *condition*:<br>
&nbsp;&nbsp;&nbsp;&nbsp;*operation 1*<br>
&nbsp;&nbsp;&nbsp;&nbsp;*operation 2*<br>
&nbsp;&nbsp;&nbsp;&nbsp;...<br>
else:<br>
&nbsp;&nbsp;&nbsp;&nbsp;*operation 1*<br>
&nbsp;&nbsp;&nbsp;&nbsp;*operation 2*<br>
&nbsp;&nbsp;&nbsp;&nbsp;...

For repeated execution, we have a generic loop that executes one or more operations while a condition is met:

*loop setup, usually init counter or value to update in loop*<br>
while *condition*:<br>
&nbsp;&nbsp;&nbsp;&nbsp;*operation 1*<br>
&nbsp;&nbsp;&nbsp;&nbsp;*operation 2*<br>
&nbsp;&nbsp;&nbsp;&nbsp;...

A very common version of a loop traverses a sequence, such as a list, with a variable that takes on each value of the sequence one at a time:

for each *x* in *sequence*:<br>
&nbsp;&nbsp;&nbsp;&nbsp;*operate on x*

When iterating through multiple lists at the same time, we use an indexed list of the form:

for each value *i* in *some integer_set or range*:<br>
&nbsp;&nbsp;&nbsp;&nbsp;*operation 1*<br>
&nbsp;&nbsp;&nbsp;&nbsp;*operation 2*<br>
&nbsp;&nbsp;&nbsp;&nbsp;...

As we'll see next in [Common lower-level programming patterns](combinations.md), we often have to embed one of these patterns within another pattern to get the desired result.
