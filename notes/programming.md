# Introduction to programming

<p align="right"><i>Computer Science is no more about computers<br>than astronomy is about telescopes.</i><br>
&nbsp;&nbsp;&nbsp;&nbsp;— Edsger Dijkstra

I remember being confronted with my first programming task (BASIC in 1980!) and drawing a complete blank. I didn't even know how to start solving the problem. I was stumped, despite the fact that coding would quickly become very natural for me. The reason for my initial difficulty is now obvious: The instructor provided absolutely no technique or strategy for converting a problem into a running program.  I had to figure that out on my own.

The approach of focusing on the syntax of a programming language in introductory courses is understandable.  Problem-solving is not a precise, well-defined skill.  It's more of an overall ability that gets honed with practice. Teaching and grading it is therefore challenging. It's much easier to jump immediately into the syntax of some simple programming language statements. Such an approach is concrete, and in principle, easy to understand but totally skips the part about why and when we need those statements. Professors that could survive in that environment as students usually go on to perpetuate the sink-or-swim approach when teaching other programmers.
 
In this course, I'd like to rectify that by focusing on both solving problems and learning to write complex Python code.  To do that, we're going to follow an overall problem-solving strategy that involves designing a "work plan" or "algorithm," either on paper or in your head (when you get more experience). The plan helps us think about the problem long before we get to the coding phase. Part of the plan is to identify a suitable sequence of operation that solves our problem.  This is the tricky bit so we'll reduce the scope of the solution space by: (1) restricting ourselves to a common set of operations and data structures, (2) applying well-established methods we can call "working backwards" and "reducing to a known solution", and finally, (3) taking advantage of the topic-specific nature of this introductory course to adopt a program outline that'll work for most data science problems. When we do finally get to Python programming, we'll restrict ourselves to a useful subset of the language. The goal is to teach you to program, not teach you the complete Python language.

Allow me to begin by making a distinction between <b>programming</b> (problem solving) and <b>coding</b> (expressing our solution in a particular programming language).

## What is programming?

When we think about programming, we immediately think about programming languages because we express ourselves using specific language syntax. But, that is like asking a physicist in which language they discuss physics. **Programming** is mostly about converting "word problems" (project descriptions) to an execution plan. The final act of **coding** (entering code) is required, of course, but learning to solve programming problems mentally is the most difficult process and is the most important.

The same is true for natural languages. Learning to prove mathematical theorems is harder than learning to write up proofs in some natural language. In fact, much of the mathematical syntax is the same across natural languages just as it is for programming languages.  Expressing your thoughts in Python or R, as you will do in the  data science program, is the simplest part of the programming process. That said, writing correct code is often the most frustrating and time-consuming part of the process even for experienced programmers.

Programming is more about *what* to say rather than *how* to say it.  Solving a problem with a computer means identifying a sequence of operations, each of which solves a piece of the overall problem. Each operation might itself be a sequence of suboperations.  Expressing those operations in Python or R is not the hard part. Identifying which operations are necessary and their relative order is the hard part.

Let's start with an overall strategy for attacking programming problems.

## Problem-solving strategy

Regardless of the software we're trying to write, there is an overall problem-solving strategy that we can follow.

**Step one** in any problem-solving situation is to fully understand the problem and clearly identify the goal. It might sound obvious, but any fuzziness in our understanding of the problem could send us off in the wrong direction. In a data science setting, the goal is usually a question we're trying to answer, such as "*which sales regions show the fastest year-on-year growth?*" (summary statistics), "*which transactions are fraudulent?*" (classifier) or "*what will a stock price be at a future date?*" (predictor). We should be able to precisely articulate the goal and the expected output using English words. If we can't do that, then no amount of coding expertise in Python or R will solve the problem. We'll see some examples shortly.

**Step two** (or possibly part of step one) of the problem-solving process is to write out some input-output pairs by hand. Doing so helps us understand what the program will need to do and how it might do it. As we will see, this technique works not only for the overall input and output, but also works great for designing [functions](functions.ipynb) (reusable bits of code). **We can't automate operations with code if we can't identify and perform the operations manually.** Moreover, listing a bunch of cases usually highlights special cases, such as "when the input is negative, the output should be empty". In other words, the program should not crash with a negative number as input. Programmers call this *test-driven design*.

In a job interviewing setting, this step means immediately trying to draw a few instances of the problem. For example, if asked to process a list of numbers in some way, begin by putting three or four numbers up on the board or on a piece of paper.  This naturally brings up a number of important questions that the interviewer is expecting you to ask, such as where the data comes from and whether it can all fit in memory etc...

**Step three** is to figure out what data or input, our raw materials, that we need to achieve the goal. Without the right data, we can't solve the problem. For example, I once mentored a student practicum team whose goal was to identify which customers of a website would upgrade to a professional account. The students only had data on users that had upgraded and no data on users who declined to upgrade. Whoops! You can't build an apples versus oranges classifier if you only have data on apples. If you don't have all the data you need, it's important to identify this requirement as part of the problem-solving process.  Data acquisition often requires programming and we'll revisit the topic below as part of our generic program outline.  


At this point, we've actually set the stage necessary to solve problems and we haven't thought about code at all. We started with the end result and then identified the data we need. The input-output pairs neatly bracket the computation we need to perform. At the beginning, we have the known data and, at the end, we have the expected output or work product. Ok, onto the programming steps.

**Step four** is to identify the sequence of operations that will compute the expected result.  Sometimes this is called an *algorithm* and involves planning out the specific operations and suboperations that chew on the input data, gradually transforming it into the expected output. 

These first four steps are a key part of the so-called [Feynman technique](https://www.google.com/search?q=feynman+technique), which includes writing down a complete explanation of an assigned task or problem as you would explain it to a nonexpert. Until you can write it down simply, without confusing language or terms, you yourself don't understand the problem. There is no point in continuing until you get past this phase. (Faculty often joke that the best way to learn a new topic is to teach a class on that topic!)

In **Step five**, we translate the operations in our plan to actual executable code. This step deserves an entire book but here's a summary of my advice. Start with the simplest  suboperations and make sure they work first. Then code the larger operations that use those suboperations. If there's a problem, you know that it is likely in the new code not the already-tested suboperations. In this phase, we'll normally find problems in our design from step four so we'll typically repeat four and five.  Testing functionality and fixing errors is called *debugging*.

Finally, **step six** is to check our overall results for correctness.  The most obvious check is to compare the output of our program with the known input-output pairs from step three. Then, most importantly, test the program with input that was not considered in steps three through five. This is an important test of the programs generality. If the program gives incorrect output, it's back to step four to see what's wrong.

And now for a dose of reality. The world is a big messy place and, since we know the least about a problem at the start, we typically need to repeat or bounce around through some or all of these steps. For example, let's say we're building an apples vs oranges classifier and the above process leads to a program that doesn't distinguish between the two fruit very well. Perhaps we only have data on size and shape. We might decide that the classifier needs data on color so it's back to step two (and possibly step three) then step six to check the results again.

### Conjuring up plans and programs

A program is a sequence of operations that transforms data or performs computations that ultimately lead to the expected output. *Programming* is the act of designing programs: identifying the operations and their appropriate sequence.  In other words, programming is about coming up with a work plan intended for a computer, which we often describe in semi-precise English called *pseudocode*. This is **step four** from the previous section.  

*Coding*, on the other hand, is the act of translating such high-level pseudocode to programming language syntax. As you gain more experience, it'll become easier and easier to go from a work plan in your head straight to code, without the pseudocode step.

When first learning to program, it helps to use established patterns, templates, strategies, and common data transformation operations as a crutch. For example, in the next section will look at a template for a data science program that will work in most cases throughout this program! In [programming patterns in Python](https://github.com/parrt/msan501/blob/master/notes/python-patterns.ipynb), we'll see lots of patterns you can piece together to create programs.

As mentioned above, there are also two strategies or general guidelines you can use to approach the program design process:

* *Start with the end result and work your way backwards, asking what the prerequisites are for each step*. In other words, the processing step or steps preceding step *i* compute the data or values needed by step *i*. For example, we cannot print the average of some numbers before we compute that average. We can't compute the average until we sum those numbers. We can't sum until we load those numbers into memory etc...
* *Reduce or simplify a new problem to a variation of an existing problem with a known solution.* To apply this new approach, ask what the difference is between the problem you're trying to solve and other problems for which you have a solution.

Both techniques are well known in architecture, engineering, and mathematics.  For example, imagine you want to erect a heavy statue 10 feet off the ground. A structural engineer might decide that the heavy statute needs a flat metal base directly underneath it. Then, to support all of that weight, four 10 foot steel beams should support the metal base. The beams should have deep concrete footings in the ground, and so on. That's working backwards from the end result.

As an example of reuse, engineers building a new suspension bridge do not proceed as if such a thing has never been built before.  It's likely they will take an existing design and tweak it to suit the new situation.

As an aside, plan reuse is often used to poke fun at other disciplines. For example, from [a collection of physicist jokes](https://www.astro.umd.edu/~avondale/extra/Humor/ScienceHumor/PhysicistJokes.html), here is a one variation:
> A Physicist and a mathematician are sitting in a faculty lounge. Suddenly, the coffee machine catches on fire. The physicist grabs a bucket and leap towards the sink, fills the bucket with water and puts out the fire. Second day, the same two sit in the same lounge. Again, the coffee machine catches on fire. This time, the mathematician stands up, gets a bucket, hands the bucket to the physicist, thus *reducing the problem to a previously solved one*.

**Exercise**: Given a string containing the digits of a number, such as `s = "501"`, print out the sum of the individual digits. In this case, the output should be `6 = 5 + 0 + 1`. Hint: `int('9')` yields value 9. Work backwards from the desired result, the sum, to figure out what you need. For example, the result is the sum of the digits. That means we need the digits. To get the digits, we can either iterate through the characters of a string or we can convert the string to a list of characters and iterate that. As we iterate, we can just sum up the digit values. To sum things up, we need to initialize a temporary result variable, perhaps called `n`.

**Exercise**: Given a list of numbers in `A`, reverse the numbers *inline* (meaning w/o a separate copy of `A` and w/o creating a new list to return). Start by writing an example on the board. This exercise is useful for flipping images in your [images project](../projects/images.md).

If you get stuck, or just to check your answers, you can check [my solutions](https://github.com/parrt/msan501/blob/master/notes/code/problem_solving.py).

Now that we have an overall strategy for problem solving, let's look at a program outline that'll help us get started with just about any data science program you need to build.

## Data science program template

Experienced programmers draw from a collection of generic mental templates as starting points. There are templates for desktop GUI apps, machine learning classifiers, web servers, etc....  A template provides an overall structure for the program and the programmer just has to tailor it to a specific problem.

Relying on mental or even physical templates is very common, not just in programming. Lawyers have generic templates for contracts and screenwriters have generic scripts for the various movie genres. For example, most action movies go like this: Meet the bad guy. Meet the hero/heroine. Chase scene. Hero/heroine overcomes great difficulties to defeat the bad guy and his minions.  Programming is most similar to writing legal documents because of the required precision. A missing word or punctuation can crash a program or bankrupt a contract signatory. (e.g., see [The Typo that Destroyed a NASA Rocket](https://priceonomics.com/the-typo-that-destroyed-a-space-shuttle)).

Gaining experience as a programmer means recognizing patterns in your code and creating generic templates in your mind for future use.  While you're getting started, you can rely on the experience of other programmers by reusing existing libraries of code and by using relevant templates. This leads us to the following generic data science program template that is suitable for most of the problems you're likely to run into:

1. Acquire data, which means finding a suitable file or collecting data from the web and storing in a file or database
2. Load data from disk or database and place into memory, organized into data structures
2. Normalize, filter, clean, or otherwise prepare data
3. Process the data, which can mean training a machine learning model, transforming the data, computing summary statistics, or optimizing a cost function
4. Emit results, which can be anything from simply printing an answer to saving data to the disk to generating a fancy visualization

Writing a program for a specific problem means figuring out what each of those steps are, though not all programs will use every step. 

**Acknowledgements**. Conversations with [Kathi Fisler](http://cs.brown.edu/~kfisler/) provided a lot of inspiration for the disciplined, planned approach to programming summarized here. For more on design recipes, see [Transferring Skills at Solving Word Problems from Computing to Algebra Through Bootstrap](https://cs.brown.edu/~sk/Publications/Papers/Published/sfkf-trans-word-prob-comp-alg-bs/paper.pdf).
