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

Because we're just learning to program, we're going to use this program outline and our set of [common patterns](programming.md) as a crutch. The outline gets us thinking about the kinds of operations we'll need and the set of patterns acts like a vocabulary of known words, helping to reduce the scope of the undertaking. Here's a summary of our programming patterns:

* [Map](patterns.md#map).  Apply an operator or function to every element of a sequence.
* [Accumulate](patterns.md#accumulate).  Accumulate a value or values while traversing a sequence.
* [Combine](patterns.md#combine).  Create a new sequence by combining values from multiple sequences.
* [Split](patterns.md#split). Split one sequence into multiple.
* [Sort](patterns.md#sort). Sort a list or sort a table by a column.
* [Slice](patterns.md#slice).  Extract a continuous subset of a list.
* [Remove duplicates](patterns.md#uniquify).  Convert a list to a set, with unique elements.
* [Filter](patterns.md#filter). Extract a subset of a sequence whose values satisfy a specific condition.
* [Search](patterns.md#search). Find the first or last index (position) of a specific value in a list.

To design a program, we're going to break the problem down into operations and suboperations while following the general outline. But, how do we know which operations we need to plan out a program? The easiest way is to follow this guideline:

*Start with the end result and work your way backwards, fulfilling prerequisites*.

In other words, the step or steps preceding step *i* compute the data or values needed by step *i*.

This approach is a well-known architectural and engineering trick. For example, imagine you want to erect a heavy statue 10 feet off the ground. A structural engineer might decide that the heavy statute needs a flat metal base directly underneath it. Then, to support all of that weight, four 10 foot steel beams should support the metal base. The beams should have deep concrete footings, and so on.

Taking the analogy further, construction proceeds in the opposite direction, from the concrete footings upwards. We'll also start coding the operations (translating to programming language syntax) starting with the first operation, thus, providing a strong foundation from which to code and test the rest of the program.

To see how the overall strategy and program outline come together, let's work through a series of programming problems.

## Getting started

As a first problem, let's plan out a program that computes the average of some numbers. To help us remember the problem-solving steps and program outline, let's use a [template for our program work plan](plans/program-planning.pdf).

Our first problem-solving step is to clearly identify the goal, although it's almost a simple restatement of the problem. Let's start with "*Compute and print the average of the numbers in a file*."  For step two, we can assume we have the necessary data by definition. The next step is to manually write out some sample input-output pairs. A single value, say, 1 should get us 1 as output. Two values like 1, 2 should give 1.5 etc.  Oh, what happens if there are no numbers? (Notice how laying out the possibilities helps us think about the definition of the problem.) We should emit 0.  Let's revisit step one and change it to be more general: "*Compute and print the average of the numbers in a file. Print 0 if there are no numbers.*"

The meat of the task is to identify the sequence of operations needed to compute the result. The first two steps, acquiring data and loading it into a data structure, are so straightforward for our sample problems that we can identify those operations straightaway; i.e., without working backwards from the end result. In this case, acquiring and loading just means "*Load the numbers into a list in memory*."

We don't need to normalize or clean the data so we can proceed to the "process the data" operation. For the final "emit results" operation, we can simply say "*Print the average.*" For the average to exist, the previous step must divide the sum of the input numbers by the number of values in the list.  We also need to avoid dividing by zero when there are no numbers in the list. For that, we can use a simple conditional pseudocode statement like: "*If the count is 0, the average is 0 else compute the average as the sum divided by the count*," which will map very easily to Python code.

That computation implies that we need yet more previous operations, to compute the sum and count the elements in the list. Fortunately, we can use an accumulator pattern for both of those operations. Because summing and counting only need the list of numbers as input, there is no prior step we need to identify. (We already decided that the program needs to load the numbers into a list at the beginning.) Completely filled out, the program work plan looks like this:

<img src=images/average-plan.png width=500>

Now, let's see what happens to the plan if we make the problem a little more complicated.

## Plan reuse

When discussing the slice programming pattern, we used 999 as a sentinel value to indicate the end of some rainfall data of interest. Let's solve the problem of computing the average rainfall coming from a sensor up to but not including value 999. To solve this, we're going to use the second  guideline for identifying program operations: 

*Reduce or simplify a new problem to a variation of an existing problem with a known solution.* 

This approach is well-known and used by just about every technical discipline (mathematics, physics, engineering, architecture, etc...).  For example, engineers building a new suspension bridge do not proceed as if such a thing has never been built before.  It's likely they will take an existing design and tweak it to suit the new situation.

As an aside, this guideline is often used to poke fun at other disciplines. For example, from [a collection of physicist jokes](https://www.astro.umd.edu/~avondale/extra/Humor/ScienceHumor/PhysicistJokes.html), here is a one variation:
> A Physicist and a mathematician are sitting in a faculty lounge. Suddenly, the coffee machine catches on fire. The physicist grabs a bucket and leap towards the sink, fills the bucket with water and puts out the fire. Second day, the same two sit in the same lounge. Again, the coffee machine catches on fire. This time, the mathematician stands up, gets a bucket, hands the bucket to the physicist, thus *reducing the problem to a previousely solved one*.

We also use this problem-reduction approach in the programming world.  For example, the only difference between this new data problem and the previous generic "average some numbers" problem is that we want to ignore data beyond a certain point in the list. It stands to reason that if we tweak our averaging program plan, we can solve this new problem quickly. If we take a subset of the original list using the slice pattern:

<img src=images/slice.png width=210>

then we get just a list of numbers and we're right back to the simple averaging problem from the last section.

In order to take the slice, however, we need to know where the 999 is in the list, which implies we need a "search for 999" operation preceding the slice.  We can't assume the computer will magically know where the 999 is and that it is significant. Like teaching a child, we must plan out all necessary steps.  We are making use of the "working backwards" approach to breakup a single complex operation into two suboperations: search for 999, slice out everything up to that position. This operation smacks of data cleanup, so let's make use of that position in the program outline. The rest of the plan is identical to the previous average plan:

<img src=images/rainfall-average-plan.png width=600>

**Exercise**: How can we handle the situation where the rainfall sensor is noisy and can spuriously generate some negative numbers? What should we change in our program work plan? Hint: it helps to write out the sample input-output pairs.

The goal is to reuse as much possible, so we should ask ourselves: "*How can we reduce this new problem to one that we have already solved?*"  The answer is to filter out any negative numbers before giving it to the rainfall average plan. So, all we have to do is add a single operation to the "clean data" step in the overall program outline. It helps to think about such data manipulation visually:

<img src=images/filter-slice.png width=320>

The complete plan now has negative numbers in the sample input-output pairs and a new (filter) operation in the data cleaning step:

<img src=images/noisy-rainfall-average-plan.png width=600>

## Computing average sales

Let's look at a different problem, computing the average unit price for items less than $10 in some [sample sales data](../data/sales-small.xls):

<img src=images/prices.png width=70>

**Exercise**: Using the program outline as a guide, complete a work plan for this task.

First, let's clarify our goal: "*Print the average of the unit prices less than 10. Print 0 if there are no unit prices*."  Manually writing out some sample input-output pairs makes our goal even more clear: 5, 10 gives 7.5 and 3, 11 gives 3 and an empty list gives 0.

Even though the application is completely different, unit price average versus rainfall average, the work plan is literally cut-and-paste from our previous plan. The only difference is that we are filtering out unit prices greater than or equal to 10 instead of filtering out negative rainfall data noise. The plan therefore looks like this:

<img src=images/unit-price-average-plan.png width=500>

**Summarizing**, we have two key guidelines to identify the sequence of operations when planning out a program:

1. Start with the end result and work your way backwards, fulfilling prerequisites.
1. Reduce or simplify a new problem to a variation of an existing problem with a known solution.

The more experience you have, the more you will recognize similar programming problems. The key is not to memorize that you learned to filter out noisy rainfall data. You want to abstract these similar plans as "*filter then average elements in a list*." In fact, we can formalize the concept of reuse by introducing the notion of a subprogram called a function. 

Next: [Functions (subprograms)](functions.md)

**Acknowledgments**.  Some of the examples in this document and the notion of a program work plan were derived from [CS2102 at WPI](http://web.cs.wpi.edu/~cs2102/b16/Lectures/planning.html).  For more on the rainfall problem and its various solutions, see [The Recurring Rainfall Problem](https://pdfs.semanticscholar.org/f772/087a1ef8f524cc2414c3b64636dd0b9985eb.pdf).