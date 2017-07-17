# Program planning

A program is a sequence of operations that transforms data or performs computations that ultimately lead to the expected output. *Programming* is the act of designing programs: identifying the operations and their appropriate sequence.  In other words, programming is about coming up with a work plan intended for a computer, which we'll describe in semi-precise English called *pseudocode*. *Coding* is the act of translating such high-level pseudocode to programming language syntax. We'll worry about the actual [coding](coding.md) part later, after we learn how to design programs.
 At this point, we have an excellent foundation to start building programs because we have an [overall problem-solving strategy](programming.md):

1. Clearly articulate the problem were trying to solve
2. Figure out what data we need
3. Manually write out a few input-output pairs
4. Identify a suitable sequence of operations
5. Code the problem
6. Verify that the program generates the correct output

To help us follow this strategy, we'll use a [program work plan](plans/program-planning.pdf) as a guide.  For step #4 of the strategy, we also have an overall analytics program outline:

1. Acquire data
2. Load data into a data structure
2. Normalize, clean, or otherwise prepare data
3. Process the data
4. Emit results

Because we're just learning to program, we're going to use this program outline and our set of [common operations](programming.md) as a crutch. The outline gets us thinking about the kinds of operations we'll need and the finite set of common operations acts like a vocabulary of known words, helping to reduce the scope of our undertaking. Here's a summary of our programming operations:

* [Map](operations.md#map).  Apply an operator or function to every element of a sequence.
* [Accumulate](operations.md#accumulate).  Accumulate a value or values while traversing a sequence.
* [Combine](operations.md#combine).  Create a new sequence by combining values from multiple sequences.
* [Split](operations.md#split). Split one sequence into multiple.
* [Sort](operations.md#sort). Sort a list or sort a table by a column.
* [Slice](operations.md#slice). Extract a continuous subset of a list.
* [Remove duplicates](operations.md#uniquify).  Convert a list to a set, with unique elements.
* [Filter](operations.md#filter). Extract a subset of a sequence whose values satisfy a specific condition.
* [Search](operations.md#search). Find the first or last index (position) of a specific value in a list.

## Sample problem: Rainfall data

Let's think about solving a problem that has a lot of moving parts:

> Design a program called *rainfall* that processes a list of numbers representing daily rainfall amounts. The list contains the number 999 indicating the end of the data of interest. The program must produce the average of the non-negative values in the list up to but not including the 999. You cannot use built-in functions like `mean()`, `len()`, `sum()`.

This problem stumps a shockingly-high percentage of computer science students completing first semester programming classes. We're going to solve this easily in this lecture by breaking the problem down into manageable chunks.
 
## The program design process

To see how the overall strategy and program outline come together, let's plan do the easy, well-understood part of the rainfall problem: computing the average of some numbers. To help us remember the problem-solving steps and program outline, we'll use a [template for our program work plan](plans/program-planning.pdf).

Our first problem-solving/work-plan step is to clearly identify the goal, although it's almost a simple restatement of the problem. Let's start with "*Compute and print the average of the numbers in a file*."  The next step is to manually write out some sample input-output pairs. A single value, say, 1 should get us 1 as output. Two values like 1, 2 should give 1.5 etc.  Oh, what happens if there are no numbers? (Notice how laying out the possibilities helps us think about the definition of the problem.) We should emit 0.  Let's revisit step one and change it to be more general: "*Compute and print the average of the numbers in a file. Print 0 if there are no numbers.*"

The next step in the work plan is to design the program, which means identifying the processing steps our program needs to take to compute the result.  We start by breaking the overall problem down into a sequence of operations using the overall program outline as a guide. We continue decomposing complex operations into sequences of smaller suboperations until we reach a level of granularity that can be directly expressed in our programming language. Until we learn to code, we can simply draw from the [common set of operations](operations.md).

But, how do we know which operations we need to plan out a program? Here's the key to converting an English description (a "word problem") into a sequence of operations:

<img src="images/redbang.png" width=30 align="left">*Start with the end result and work your way backwards, asking what the prerequisites are for each step*.

In other words, the processing step or steps preceding step *i* compute the data or values needed by step *i*. For example, we cannot print the average of some numbers before we compute that average. We can't compute the average until we load those numbers into memory etc...

This approach is a well-known architectural and engineering trick. For example, imagine you want to erect a heavy statue 10 feet off the ground. A structural engineer might decide that the heavy statute needs a flat metal base directly underneath it. Then, to support all of that weight, four 10 foot steel beams should support the metal base. The beams should have deep concrete footings in the ground, and so on.

The method of working backwards means starting at the last processing step, emitting results. For that final step, we can simply say "*Print the average.*"  

Now we move backwards a step (into the "Process the data" section of the program outline). For the average to exist for printing, the previous step must divide the sum of the input numbers by the number of values in the list.  We also need to avoid dividing by zero when there are no numbers in the list. For that, we can use a simple conditional pseudocode statement like: "*If the count is 0, the average is 0 else the average is the sum divided by the count*," which will map very easily to Python code later.

That division implies that we need yet more previous operations, to compute the sum and count the elements in the list. Fortunately, we can use an accumulate operation for both of those computations. We could say something like "*Use accumulator to some the values*". That's it for the data processing step of the program outline.

Those data processing operations need only the list of numbers as prerequisites. We can use pseudocode like "*load the numbers into a list in memory*" to make that list available. Because that fits into the "load data" step in the outline, there's nothing to fill in for the "normalize, clean the data" step. The "acquire data" step is also empty because we can assume that the file is sitting on the desk somewhere for us to load. That's the end of the program design.

Completely filled out, the program work plan looks like this:

<img src=plans/average-plan.png width=500>

Now, let's see what happens to the plan if we make the problem a little more complicated.

## Plan reuse

Now, let's add back the complexity of stopping at 999 to the problem we're trying to solve. We want to compute the average rainfall coming from a sensor up to but not including value 999. To solve this, we're going to use the second method for identifying program operations: 

<img src="images/redbang.png" width=30 align="left">*Reduce or simplify a new problem to a variation of an existing problem with a known solution.* 

This approach is well-known and used by just about every technical discipline (mathematics, physics, engineering, architecture, etc...).  For example, engineers building a new suspension bridge do not proceed as if such a thing has never been built before.  It's likely they will take an existing design and tweak it to suit the new situation.

As an aside, this guideline is often used to poke fun at other disciplines. For example, from [a collection of physicist jokes](https://www.astro.umd.edu/~avondale/extra/Humor/ScienceHumor/PhysicistJokes.html), here is a one variation:
> A Physicist and a mathematician are sitting in a faculty lounge. Suddenly, the coffee machine catches on fire. The physicist grabs a bucket and leap towards the sink, fills the bucket with water and puts out the fire. Second day, the same two sit in the same lounge. Again, the coffee machine catches on fire. This time, the mathematician stands up, gets a bucket, hands the bucket to the physicist, thus *reducing the problem to a previously solved one*.

We also use this problem-reduction approach in the programming world.  For example, the only difference between this new data problem and the previous generic "average some numbers" problem is that we want to ignore data beyond a certain point in the list. It stands to reason that if we tweak our averaging program plan, we can solve this new problem quickly. 

As before, we start designing a program by clearly describing our objective.  In this case, we just have to tweak the objective so that it indicates we'd like to average the numbers in a file up to but not including the 999 sentinel. Next, we augment the sample input-output pairs to have 999, such as "1, 2, 999, 5, 4 → 1.5."

Ok, now we can focus on reuse to solve this new problem. If we take a subset of the original list using the slice operation:

<img src=images/slice.png width=210>

then we get just a list of numbers and we're right back to the simple averaging problem from the last section.

Next up in the work plan, we design the program. The method of reuse tells us that somewhere in the program sequence we'll see a slice operation and the average computing operations we had from before. Using the method of "working backwards", we know that the slice must precede the averaging operations. The averaging operation consumes the result of slicing.

Working backwards also tells us that we must search for the 999 sentinel in the list before the slice so the slice operation knows the bounds (range of desired elements).  We can't assume the computer will magically know where the 999 is and that 999 is significant. Like teaching a child, we must plan out all necessary steps.  The search and slice operations smack of data cleanup, so let's put them in that position in the program outline. The rest of the plan is identical to the previous average work plan:

<img src=plans/rainfall-average-plan.png width=600>

## Noisy rainfall sensor data

We can add the final complexity to the rainfall problem: The rainfall sensor is noisy and can spuriously generate some negative numbers. What should we change in our program work plan? Well, it helps to write out the sample input-output pairs.

The goal is to reuse as much possible, so we should ask ourselves: "*How can we reduce this new problem to one that we have already solved?*"  The answer is to filter out any negative numbers before giving it to the rainfall average plan. So, all we have to do is add a single operation to the "clean data" step in the overall program outline. It helps to think about such data manipulation visually:

<img src=images/filter-slice.png width=320>

The complete plan now has negative numbers in the sample input-output pairs and a new (filter) operation in the data cleaning step. 

Try to do this without looking at the [solution](plans/noisy-rainfall-average-plan.png)

## Computing average sales

Let's look at a different problem, computing the average unit price for items less than $10 in some [sample sales data](../data/sales-small.xls):

<img src=images/prices.png width=70>

**Exercise**: Using the program outline as a guide, complete a work plan for this task.

First, clarify the goal: "*Print the average of the unit prices less than 10. Print 0 if there are no unit prices*."  Manually writing out some sample input-output pairs makes our goal even more clear: 5, 10 gives 7.5 and 3, 11 gives 3 and an empty list gives 0.

Even though the application is completely different, unit price average versus rainfall average, the work plan is literally cut-and-paste from our previous plan. The only difference is that we are filtering out unit prices greater than or equal to 10 instead of filtering out negative rainfall data noise. The plan therefore looks like this:

Try to do this without looking at the [solution](plans/unit-price-average-plan.png)

<a name="power"></a>
### Power-to-weight ratio

**Exercise**: Compute the average power-to-weight ratio of just the 8-cylinder engines from a [sample car data set](../data/cars.xls). The first few rows look like:

<img src=images/cars.png width=240>

ENG is the power column.

Follow the process in our [program work plan](plans/program-planning.pdf). Hints: For the sample input-output pairs step of the design process, I actually manually do some interactive work in a spreadsheet. Here is one experiment in process:

<img src=images/power-to-weight-op.png width=300>

For the loading data section, you can say something like "*load car table into memory*". Assuming we can access a column within a table by name, such as ENG and WGT.

Try to do this without looking at the [solution](plans/power-to-weight-plan.pdf).

## Summary

We have two key methods for identifying the sequence of operations when planning out a program:

1. Start with the end result and work your way backwards, fulfilling prerequisites.
1. Reduce or simplify a new problem to a variation of an existing problem with a known solution.

The more experience you have, the more you will recognize similar programming problems. The key is not to memorize that you learned to filter out noisy rainfall data. You want to abstract these similar plans as "*filter then average elements in a list*." In fact, we can formalize the concept of reuse by introducing the notion of a subprogram called a [function](functions.md), which is what we'll do next.

**Acknowledgments**.  Some of the examples in this document and the notion of a program work plan were derived from [CS2102 at WPI](http://web.cs.wpi.edu/~cs2102/b16/Lectures/planning.html).  For more on the rainfall problem and its various solutions, see [The Recurring Rainfall Problem](https://pdfs.semanticscholar.org/f772/087a1ef8f524cc2414c3b64636dd0b9985eb.pdf).
