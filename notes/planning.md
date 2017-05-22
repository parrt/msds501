# Program planning

*in progress*

A program is a sequence of operations that transforms data or performs computations that ultimately lead to the expected output. *Programming* is the act of designing programs: identifying the operations and their appropriate sequence.  In other words, programming is about coming up with a work plan intended for a computer, which we'll describe in semi-precise English called *pseudocode*. *Coding* is the act of mapping such high-level pseudocode to programming language syntax. We'll worry about the actual [coding](coding.md) part later, after we learn how to design programs.
 At this point, we have an excellent foundation to start building programs because we have an [overall problem-solving strategy](programming.md):

1. Clearly articulate the problem were trying to solve
2. Figure out what data we need
3. Manually write out a few input-output pairs
4. Identify a suitable sequence of operations
5. Code the problem
6. Verify that the program generates the correct output

and, for step #4, we have an overall analytics program outline:

1. Acquire data
2. Load data into a data structure
2. Normalize, clean, or otherwise prepare data
3. Process the data
4. Emit results

Because we're just learning to program, we're going to use this program outline and our set of [common patterns](programming.md) as a crutch. The outline gets us thinking about the kinds of operations we'll need and the set of patterns acts like a vocabulary of known words, helping to reduce the scope of the undertaking.

To design a program, we're going to break the problem down into operations and suboperations while following the general outline. But, how do we know which operations we need to plan out a program? The easiest way is to *start with the end result and work your way backwards*. The step or steps preceding step *i* compute the data or values needed by step *i*.

This approach is a well-known architectural and engineering trick. For example, imagine you want to erect a heavy statue 10 feet off the ground. A structural engineer might decide that the heavy statute needs a flat metal base directly underneath it. Then, to support all of that weight, four 10 foot steel beams should support the metal base. The beams should have deep concrete footings, and so on.

Taking the analogy further, construction proceeds in the opposite direction, from the concrete footings upwards. We'll also start coding the operations (translating to programming language syntax) starting with the first operation, thus, providing a strong foundation from which to code and test the rest of the program.

To see how the overall strategy and program outline come together, let's work through a series of programming problems.

## Getting started

As a first problem, let's plan out a program that computes the average of some numbers. To help us remember the problem-solving steps and program outline, let's use a [template for our program work plan](plans/program-planning.pdf).

Our first problem-solving step is to clearly identify the goal, although it's almost a simple restatement of the problem. Let's start with "*Compute and print the average of the numbers in a file*."  For step two, we can assume we have the necessary data by definition. The next step is to manually write out some sample input-output pairs. A single value, say, 1 should get us 1 as output. Two values like 1, 2 should give 1.5 etc.  Oh, what happens if there are no numbers? We should emit 0.  Let's revisit step one and change it to be more general: "*Compute and print the average of the numbers in a file. Print 0 if there are no numbers.*"

The meat of the task is to identify the sequence of operations needed to compute the result. The first two steps, acquiring data and loading it into a data structure, are so straightforward for our sample problems that we can identify those operations straightaway; i.e., without working backwards from the end result. In this case, acquiring and loading just means "*Load the numbers into a list in memory*."

We don't need to normalize or clean the data so we can proceed to the "process the data" operation. For the final "emit results" operation, we can simply say "*Print the average.*" For the average to exist, the previous step must divide the sum of the input numbers by the number of values in the list.  We also need to avoid dividing by zero, when there are no numbers in the list. For that, we can use a simple conditional pseudocode statement like: "*If the count is 0, the average is 0 else compute the average as the sum divided by the count*."

That computation implies that we need yet more previous operations, to compute the sum and count the elements in the list. Fortunately, we can use an accumulator pattern for both of those operations. Because summing and accounting only needs the list of numbers as input, there is no prior step we need to identify. (We already decided that the program needs to load the numbers into a list at the beginning.) Completely filled out, the program work plan looks like this:

<img src=images/average-plan.png width=500>

Now, let's make the problem a little more complicated

rainfall with Sentinel value

then Reduce a problem to one we already know how to solve.

add noise to rainfall problem.

combining patterns such as filter and sum and counting. talk about efficiency and the number of steps or clock ticks.


## sample problems:

rainfall

min / max

balanced parens

identity matrix

add matrices

what percent of data has x in field y

average cost per product category.

histogram

all possible combinations of first/last names.

power to weight ratio

**Acknowledgments**.  Some of the examples in this document and the notion of a program work plan were derived from [CS2102 at WPI](http://web.cs.wpi.edu/~cs2102/b16/Lectures/planning.html) and [Transferring Skills at Solving Word Problems from Computing to Algebra Through Bootstrap](https://cs.brown.edu/~sk/Publications/Papers/Published/sfkf-trans-word-prob-comp-alg-bs/paper.pdf).