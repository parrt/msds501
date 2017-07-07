# How to Program

<p align="right">*Computer Science is no more about computers<br>than astronomy is about telescopes.*<br>
&nbsp;&nbsp;&nbsp;&nbsp;— Edsger Dijkstra

## What is programming?

When we think about programming, we immediately think about programming languages because we express ourselves using specific language syntax. But, that is like asking a physicist in which language they discuss physics. Programming is mostly about converting "word problems" (project descriptions) to an execution plan. The final act of entering code is required, of course, but learning to solve programming problems mentally is the most difficult process and is the most important.

The same is true for natural languages. Learning to prove mathematical theorems is harder than learning to write up proofs in some natural language. In fact, much of the mathematical syntax is the same across natural languages just as it is for programming languages.  Expressing your thoughts in Python or R, as you will do in the analytics program, is the simplest part of the programming process. That said, writing correct code is often the most frustrating and time-consuming part of the process even for experienced programmers.

Programming is more about *what* to say rather than *how* to say it. Solving a problem with a computer means identifying a sequence of operations, each of which solves a piece of the overall problem. Each operation might itself be a sequence of suboperations.  Expressing those operations in Python or R is not the hard part. Identifying which operations are necessary and their relative order is the hard part.

The good news is that all of the analytics and machine learning problems you'll likely run into can be solved using the same generic program outline, which we'll discuss shortly. Before that, we should come up with an overall strategy for attacking programming problems.

## Problem-solving strategy

Before trying to plan out an analytics program, we have to fully understand the problem at hand. That means we have to clearly articulate what we're trying to achieve and then make sure we have the necessary data. Next, it really helps to write out some sample input-output pairs by hand because that makes us think about the operations we'll need to automate with code. The following steps represent an overall problem-solving strategy for designing analytics programs.

**Step one** in any problem-solving situation is to clearly identify the goal. It might sound obvious, but any fuzziness in our understanding of the problem could send us off in the wrong direction. In an analytics setting, the goal is usually a question we're trying to answer, such as "*which sales regions show the fastest year-on-year growth?*" (summary statistics), "*which transactions are fraudulent?*" (classifier) or "*what will a stock price be at a future date?*" (predictor). We should be able to precisely articulate the goal and the expected output using English words. If we can't do that, then no amount of coding expertise in Python or R will solve the problem. We'll see some example shortly.

**Step two** is to figure out what data or input, our raw materials, that we need to achieve the goal. Without the right data, you can't solve the problem. For example, I once mentored a student practicum team whose goal was to identify which customers of a website would upgrade to a professional account. The students only had data on users that had upgraded and no data on users who declined to upgrade. Whoops! You can't build an apples versus oranges classifier if you only have data on apples. If you don't have all the data you need, it's important to identify this requirement as part of the problem-solving process.  Data acquisition often requires programming and we'll revisit the topic below as part of our generic program outline.

**Step three** of the problem-solving process is to write out some input-output pairs by hand. Doing so helps us understand what the program will need to do and how it might do it. As we will see, this technique works not only for the overall input and output, but also works great for designing functions (reusable bits of code). We can't automate operations with code if we can't identify the operations manually. Moreover, listing a bunch of cases usually highlights special cases, such as "when the input is negative, the output should be empty". In other words, the program should not crash with a negative number as input. Programmers call this *test-driven design*.

At this point, we've actually set the stage necessary to solve problems and we haven't thought about code at all. We started with the end result and then identified the data we need. The input-output pairs neatly bracket the computation we need to perform. At the beginning, we have the known data and, at the end, we have the expected output or work product. Ok, onto the programming steps.

**Step four** is to identify the sequence of operations that will compute the expected result.  Unlike the output-focused goal from step one, this step involves planning out the specific operations and suboperations that chew on the input data, gradually transforming it into the expected output. We'll learn how to make such plans below.

In **Step five**, we translate the operations in our plan to actual executable code. This step deserves an entire book but here's a summary of my advice. Start with the simplest  suboperations and make sure they work first. Then code the larger operations that use those suboperations. If there's a problem, you know that it is likely in the new code not the suboperations. In this phase, we'll normally find problems in our design from step four so we'll typically repeat four and five.  Testing functionality and fixing errors is called *debugging*.

Finally, **step six** is to check our overall results for correctness.  The most obvious check is to compare the output of our program with the known input-output pairs from step three. Then, most importantly, test the program with input that was not considered in steps three through five. This is an important test of the programs generality. If the program gives incorrect output, it's back to step four to see what's wrong.

And now for a dose of reality. The world is a big messy place and, since we know the least about a problem at the start, we typically need to repeat or bounce around through some or all of these steps. For example, let's say we're building an apples vs oranges classifier and the above process leads to a program that doesn't distinguish between the two fruit very well. Perhaps we only have data on size and shape. We might decide that the classifier needs data on color so it's back to step two (and possibly step three) then step six to check the results again.

So now we have an overall strategy for problem solving. It's time to think about actually programming a solution. Let's start by looking at a program outline that'll help us get started with the majority of analytics programs.

## Analytics program template

I remember being confronted with my first programming task (BASIC in 1980!) and drawing a complete blank. I didn't even know how to start solving the problem.  It turns out that experienced programmers draw from a collection of generic mental templates as starting points. There are templates for desktop GUI apps, machine learning classifiers, web servers, etc....  A template provides an overall structure for the program and the programmer just has to tailor it to a specific problem.

Relying on mental or even physical templates is very common, not just in programming. Lawyers have generic templates for contracts and screenwriters have generic scripts for the various movie genres. For example, most action movies go like this: Meet the bad guy. Meet the hero/heroine. Chase scene. Hero/heroine overcomes great difficulties to defeat the bad guy and his minions.  Programming is most similar to writing legal documents because of the required precision. A missing word or punctuation can crash a program or bankrupt a contract signatory. (e.g., see [The Typo that Destroyed a NASA Rocket](https://priceonomics.com/the-typo-that-destroyed-a-space-shuttle)).

Gaining experience as a programmer means recognizing patterns in your code and creating generic templates in your mind for future use.  While you're getting started, you can rely on the experience of other programmers by reusing existing libraries of code and by using relevant templates. This leads us to the following generic analytics program template that is suitable for most of the problems you're likely to run into:

1. Acquire data, which means finding a suitable file or collecting data from the web and storing in a file
2. Load data from disk and place into memory organized into data structures
2. Normalize, clean, or otherwise prepare data
3. Process the data, which can mean training a machine learning model, computing summary statistics, or optimizing a cost function
4. Emit results, which can be anything from simply printing an answer to saving data to the disk to generating a fancy visualization

Writing a program for a specific problem means figuring out what each of those steps are, though not all programs will use every step. Let's take a look at the template in action on a trivial problem, computing the average of some numbers:

1. Locate a file with some numbers
2. Load the data from the file into a list structure in memory
3. *no data prep needed*
4. Compute the average of the numbers in the list
5. Print the average

This problem is easy enough that most of us could outline a solution without explicitly and formally breaking it down in this manner. The point is that this template provides a framework to solve more difficult problems and you should get used to applying the template. At the very least, it's a way to get started on a project.

## Intro to planning out a program

The program template gives an overall outline for the coarsest-grained operations of the program but we'll need to break each of those operations down further and further into suboperations. We continue decomposing large operations into a sequence of smaller operations until we reach a level of granularity that can be directly expressed in our programming language.

Here's the key to converting an English description (a "word problem") into a sequence of operations: *start at the end result and work backwards asking what the prerequisites are for each step*. For example, we cannot print the average of some numbers before we compute that value. We can't compute that value until we load those numbers into memory etc...

This "working backwards" mechanism even helps us break down operations like "compute the average" into sequences of suboperations.  Computing the average requires that we compute the sum and count how many numbers there are (average is sum/length).  Computing the sum and counting the numbers can't happen until we load the numbers into memory from the disk. Depending on the libraries available to us in a particular programming language, we might need to break down "compute sum" and "count how many numbers" operations further.  For now, let's assume that those operations are either built-in or available as library functions. Altogether, then, the plan for our program looks like:

1. Locate a file with some numbers
2. Load the data from the file into a list structure in memory
3. Compute the sum of the numbers in the list
4. Count the numbers in the list (compute the list length)
5. Compute average as sum divided by length
6. Print the average

(Note that the step numbers no longer correspond directly to the standard program template since we have decomposed the steps into suboperations.)

The steps in this plan are fine-grained enough to be converted one-to-one to programming statements.  At that point, we have an executable program.  The hard part is coming up with a suitable plan, not converting it to code. 

This semi-precise English is what programmers call **pseudocode** and will be the way we plan out programs, whether out loud, on paper, or in a text file. 

Operation sequences occur even in simple arithmetic expressions that we often think of as one operation. For example, in the following algebraic expression, we have to do the multiplication first and then add in the shipping cost (according to the rules of arithmetic).

<i>shipping + unitprice * units</i>

When writing out the plan for a program, always keep in mind that the computer is executing one operation after the other so the setting up the right sequence is critical.

Next up:

* [Representing data in memory](data-in-memory.md)
* [Common programming patterns](patterns.md)

**Acknowledgements**. Conversations with [Kathi Fisler](http://cs.brown.edu/~kfisler/) provided a lot of inspiration for the disciplined, planned approach to programming summarized here. For more on design recipes, see [Transferring Skills at Solving Word Problems from Computing to Algebra Through Bootstrap](https://cs.brown.edu/~sk/Publications/Papers/Published/sfkf-trans-word-prob-comp-alg-bs/paper.pdf).