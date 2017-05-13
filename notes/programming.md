# How to Program

*in progress*

## What is programming?

When we think about programming, we immediately think about programming languages because we express ourselves using specific language syntax. But programming is mostly about converting "word problems" (project descriptions) to an execution plan. The final act of entering code is required, of course, but learning to solve programming problems mentally is the most difficult process and is the most important.

The same is true for natural languages. Learning to prove mathematical theorems is harder than learning to write up proofs in a new natural language. In fact, much of the mathematical syntax is the same across natural languages just as it is for programming languages.  Expressing your thoughts in Python or R, as you will do in the analytics program, is the simplest part of the programming process. That said, writing correct code is often the most frustrating and time-consuming part of the process even for experienced programmers.

Programming is more about *what* to say rather than *how* to say it. Solving a problem with a computer means identifying a sequence of operations, each of which solves a piece of the overall problem. Each operation might itself be a sequence of suboperations.  Expressing those operations in Python or R is not the hard part. Identifying which operations are necessary and their order is the hard part.

The good news is that all of the analytics and machine learning problems you'll likely run into can be solved using the same generic script, which we'll discuss shortly. Before that, we should come up with an overall strategy for attacking problems.

## Problem-solving strategy

Before trying to plan out an analytics program, we have to fully understand the problem at hand. To do that, we have to clearly articulate what we're trying to achieve and then make sure we have the necessary data. Next, it really helps to write out some sample input-output pairs by hand because that makes us think about the operations we'll need to automate with code. The following steps represent an overall problem-solving strategy for designing programs.

**Step one** in any problem-solving situation is to clearly identify the goal. In an analytics setting, the goal is usually a question you're trying to answer, such as "which sales regions show the fastest year-on-year growth", "which transactions are fraudulent" or "what will a stock price be at a future date". We should be able to precisely articulate the goal and expected output using English words. If we can't do that, then no amount of coding expertise in Python or R will solve the problem.

**Step two** is to figure out what data or input we need to satisfy that goal. Without the right data, you can't solve the problem. For example, I once mentored a student practicum team whose goal was to identify which customers of a website would upgrade to a professional account. The students only had data on users that had upgraded and no data on users who declined to upgrade. Whoops! You can't build an apples versus oranges classifier if you only have data on apples. If you don't have all the data you need, it's important to identify this requirement as part of the problem-solving process.  Data acquisition often requires programming and we'll revisit the topic below as part of our program outline.

At this point, we've actually set the stage necessary to solve problems and we haven't thought about code at all. We started with the end result and then identified the data we need, our raw material. The input-output pairs neatly bracket the computation we need to perform. At the beginning, we have the known data and, at the end, we have the expected output or work product.

**Step three** of the problem-solving process is to write out some input-output pairs by hand. Doing so helps us understand what the program will need to do and how it might do it. We can't automate operations with code if we can't identify the operations manually. Moreover, listing a bunch of cases usually highlights special cases, such as "when the input is negative, the output should be empty". In other words, the program should not crash with a negative number as input. Programmers call this *test-driven design*.

**Step four** is to identify the operations that will compute the right result. To do this, work backwards from the end product. Make a plan

**Step five** translate to code.

And, finally, **step six** is to check our results for correctness.  The most obvious check is to compare the operation of our program with the known input-output pairs from step three.

## Analytics program script

All of the problems you will likely run into during your masters program will follow the same generic overall script:

1. Acquire then load data into memory
2. Organize, normalize, or otherwise prepare data
3. Process the data, which can mean training a machine learning model, computing summary statistics, or optimizing a function
4. Emit results, which can be anything from simply printing an answer to saving data to the disk to generating a fancy visualization

These course-grain steps form the broad outline of a program in any language.  Writing a program for a specific problem means figuring out what each of those steps are.  Not all programs will use every step, but we'll need to break each of those steps further down into subtasks for all but the simplest problems.

For example, let's see how computing the average of some numbers fits into this outline. 

First, what are you given? what's unknown? Ok, now write down the comp u expect to perform. Now give some samples,
 
  Step one means getting a list of numbers, which we can assume is a given.

is this similar to something I've solved before?

 by starting at the last step in working our way backwards

 this highlights that you should start from the result, the last step, and work your way backwards

lowest level computer capabilities: 

* hold named chunks of data
* perform arithmetic computations
* conditionally perform computations.
* repeat steps

 At the other extreme there can be preprogrammed high-level operations that can, for example, display a bar chart given a list of numbers.
 
**Acknowledgements**. Conversations with [Kathi Fisler](http://cs.brown.edu/~kfisler/) provided a lot of inspiration for the disciplined, planned approach to programming summarized here. For more on design recipes, see [Transferring Skills at Solving Word Problems from Computing to Algebra Through Bootstrap](https://cs.brown.edu/~sk/Publications/Papers/Published/sfkf-trans-word-prob-comp-alg-bs/paper.pdf).