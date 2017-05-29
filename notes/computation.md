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

The key elements of a conditional statement are: the conditional expression and the operation(s) to perform if true. For the else-clause variant, we have the conditional expression, the operation to perform if true, and the operation to perform if the condition is false. A template for conditional execution looks like:

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

In the programming world, we call this a *loop*. The key elements of a loop are the condition expression and the operation(s) to perform while the condition is true. When trying to map a real-world problem to a loop, your goal is to identify the condition and the repeated steps. A template for a loop looks like:

while *condition*:<br>
&nbsp;&nbsp;&nbsp;&nbsp;*operation 1*<br>
&nbsp;&nbsp;&nbsp;&nbsp;*operation 2*<br>
&nbsp;&nbsp;&nbsp;&nbsp;...


We can also repeat repeated instructions, which we call a *nested loop*. For example, the recipe goes on to say:

> Continue adding broth 1/2 cup at a time, stirring continuously, until the liquid is absorbed and the rice is *al dente*, about 15 to 20 minutes.

We are supposed to add broth until we run out of it, 1/2 cup at a time.  For each 1/2 cup we add, we are to stir until it is absorbed. Making the recipe more precise, we might express it like this as a nested loop:

*while there is more broth:*<br>
&nbsp;&nbsp;&nbsp;&nbsp;*add 1/2 cup broth to pot*<br>
&nbsp;&nbsp;&nbsp;&nbsp;*repeat until broth is absorbed:*<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*stir rice in pot*<br>