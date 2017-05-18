# How to Program

*in progress*

## What is programming?

When we think about programming, we immediately think about programming languages because we express ourselves using specific language syntax. But programming is mostly about converting "word problems" (project descriptions) to an execution plan. The final act of entering code is required, of course, but learning to solve programming problems mentally is the most difficult process and is the most important.

The same is true for natural languages. Learning to prove mathematical theorems is harder than learning to write up proofs in a new natural language. In fact, much of the mathematical syntax is the same across natural languages just as it is for programming languages.  Expressing your thoughts in Python or R, as you will do in the analytics program, is the simplest part of the programming process. That said, writing correct code is often the most frustrating and time-consuming part of the process even for experienced programmers.

Programming is more about *what* to say rather than *how* to say it. Solving a problem with a computer means identifying a sequence of operations, each of which solves a piece of the overall problem. Each operation might itself be a sequence of suboperations.  Expressing those operations in Python or R is not the hard part. Identifying which operations are necessary and their order is the hard part.

The good news is that all of the analytics and machine learning problems you'll likely run into can be solved using the same generic program outline, which we'll discuss shortly. Before that, we should come up with an overall strategy for attacking problems.

## Problem-solving strategy

Before trying to plan out an analytics program, we have to fully understand the problem at hand. That means we have to clearly articulate what we're trying to achieve and then make sure we have the necessary data. Next, it really helps to write out some sample input-output pairs by hand because that makes us think about the operations we'll need to automate with code. The following steps represent an overall problem-solving strategy for designing analytics programs.

**Step one** in any problem-solving situation is to clearly identify the goal. It might sound obvious, but any fuzziness in our understanding of the problem could send us off in the wrong direction. In an analytics setting, the goal is usually a question we're trying to answer, such as "*which sales regions show the fastest year-on-year growth?*" (summary statistics), "*which transactions are fraudulent?*" (classifier) or "*what will a stock price be at a future date?*" (predictor). We should be able to precisely articulate the goal and the expected output using English words. If we can't do that, then no amount of coding expertise in Python or R will solve the problem. We'll see some example shortly.

**Step two** is to figure out what data or input, our raw materials, that we need to achieve the goal. Without the right data, you can't solve the problem. For example, I once mentored a student practicum team whose goal was to identify which customers of a website would upgrade to a professional account. The students only had data on users that had upgraded and no data on users who declined to upgrade. Whoops! You can't build an apples versus oranges classifier if you only have data on apples. If you don't have all the data you need, it's important to identify this requirement as part of the problem-solving process.  Data acquisition often requires programming and we'll revisit the topic below as part of our generic program outline.

At this point, we've actually set the stage necessary to solve problems and we haven't thought about code at all. We started with the end result and then identified the data we need. The input-output pairs neatly bracket the computation we need to perform. At the beginning, we have the known data and, at the end, we have the expected output or work product.

**Step three** of the problem-solving process is to write out some input-output pairs by hand. Doing so helps us understand what the program will need to do and how it might do it. As we will see, this technique works not only for the overall input and output, but also works great for designing functions (reusable bits of code). We can't automate operations with code if we can't identify the operations manually. Moreover, listing a bunch of cases usually highlights special cases, such as "when the input is negative, the output should be empty". In other words, the program should not crash with a negative number as input. Programmers call this *test-driven design*.

**Step four** is to identify the sequence operations that will compute the expected result.  Unlike the output-focused goal from step one, this step involves planning out the specific operations and suboperations that chew on the input data, gradually transforming it into the expected output. We'll learn how to make such plans below.

In **Step five**, we translate the operations in our plan to actual executable code. This step deserves an entire book but here's a summary of my advice. Start with the simplest  suboperations and make sure they work first. Then code the larger operations that use those suboperations. If there's a problem, you know that it is likely in the new code not the suboperations. In this phase, we'll normally find problems in our design from step four so we'll typically repeat four and five.  Testing functionality and fixing errors is called *debugging*.

Finally, **step six** is to check our overall results for correctness.  The most obvious check is to compare the output of our program with the known input-output pairs from step three. Then, most importantly, test the program with input that was not considered in steps three through five. This is an important test of the programs generality. If the program gives incorrect output, it's back to step four to see what's wrong.

And now for a dose of reality. The world is a big messy place and, since we know the least about a problem at the start, we typically need to repeat or bounce around through some or all of these steps. For example, let's say we're building an apples vs oranges classifier and the above process leads to a program that doesn't distinguish between the two fruit very well. Perhaps we only have data on size and shape. We might decide that the classifier needs data on color so it's back to step two (and possibly step three) then step six to check the results again.

## Analytics program template

I remember being confronted with my first programming task (BASIC in 1980!) and drawing a complete blank. I didn't even know how to start solving the problem.  It turns out that experienced programmers draw from a collection of generic mental templates as starting points. There are templates for desktop GUI apps, machine learning classifiers, web servers, etc....  A template provides an overall structure for the program and the programmer just has to tailor it to a specific problem.

Relying on mental or even physical templates is very common, not just in programming. Lawyers have generic templates for contracts and screenwriters have generic scripts for the various movie genres. For example, most action movies go like this: Meet the bad guy. Meet the hero/heroine. Chase scene. Hero/heroine overcomes great difficulties to defeat the bad guy and his minions.  Programming is most similar to writing legal documents because of the required precision. A missing word or punctuation can crash a program or bankrupt a contract signatory. (e.g., see [The Typo that Destroyed a NASA Rocket](https://priceonomics.com/the-typo-that-destroyed-a-space-shuttle)).

Gaining experience as a programmer means recognizing patterns in your code and creating generic templates in your mind for future use.  While you're getting started, you can rely on the experience of other programmers by reusing existing libraries of code and by using relevant templates. This leads us to the following generic analytics program template that is suitable for most of the problems you're likely to run into:

1. Acquire data
2. Load data into memory and organize into data structures
2. Normalize or otherwise prepare data
3. Process the data, which can mean training a machine learning model, computing summary statistics, or optimizing a cost function
4. Emit results, which can be anything from simply printing an answer to saving data to the disk to generating a fancy visualization

Writing a program for a specific problem means figuring out what each of those steps are, though not all programs will use every step. Let's take a look at the template in action on a trivial problem, computing the average of some numbers:

1. Locate a file with some numbers
2. Load the data from the file into a list structure in memory
3. *no data prep needed*
4. Compute the average of the numbers in the list
5. Print the average

This problem is easy enough that most of us could outline a solution without explicitly and formally breaking it down in this manner. The point is that this template provides a framework to solve more difficult problems and you should get used to applying the template. At the very least, it's a way to get started on a project.

## Planning out a program

The program template gives an overall outline for the coarsest-grained operations of the program but we'll need to break each of those operations down further and further into suboperations. We continue decomposing large operations into a sequence of smaller operations until we reach a level of granularity that can be directly expressed in our programming language. 

Here's the key to converting an English description (a "word problem") into a sequence of operations: *start at the end result and work backwards asking what the prerequisites are for each step*. For example, we cannot print the average of some numbers before we compute that value. We can't compute that value until we load those numbers into memory etc...

This "working backwards" mechanism even helps us break down operations like "compute the average" into sequences of suboperations.  Computing the average requires that we compute the sum and count how many numbers there are (average is sum/length).  Computing the sum and counting the numbers can't happen until we load the numbers into memory from the disk. Depending on the libraries available to us in a particular programming language, we might need to break down "compute sum" and "count how many numbers" operations further.  For now, let's assume that those operations are either built-in or available as library functions. Altogether, then, the plan for our program looks like:

1. Locate a file with some numbers
2. Load the data from the file into a list structure in memory
3. Compute the sum of the numbers in the list
4. Count the numbers in the list (compute the list length)
5. Compute average as sum divided by length
6. Print the average

The steps in this plan are fine-grained enough to be converted one-to-one to programming statements.  At that point, we have an executable program.  The hard part is coming up with a suitable plan, not converting it to code.

Sequences occur even in simple arithmetic expressions that we often think of as one operation. For example, in the following expression, we have to do the multiplication first and then add in the shipping cost.

```
shipping + unitprice * units
```

When writing out the plan for a program, always keep in mind that the computer is executing one operation after the other so the setting up the right sequence is critical.

## Representing data in memory

So far, we've glossed over the details of loading data into memory from disk (step 2 in our plan above) but the way we represent data in memory is critical to building programs. This is particularly true with analytics programs because processing data is our focus.  Let's take a bit of a detour into computer architecture to get a handle on what it means to load something into memory.

A computer consists of three primary components: a disk to hold data, a memory (that is wiped upon power off), and a processor (CPU) to process that data. Here is a picture of an actual CPU and some memory chips:

<img src=images/cpu-memory.png width=400>

The memory is broken up into discrete chunks of a fixed size (8 *bits* called one *byte*) and each chunk is identified by an integer address, just like the house numbers on street addresses like 101 Howard Street. Processors can ask for the data at a particular address and can store a piece of data at a specific memory location as well as well. For example, here is an abstract representation of byte-addressable computer memory:

<img src=images/addresses.png width=100> 

In this case, the memory has value 100 at address 0. At address 1, the memory has value 0. Address 4 has the maximum value we can store in a single byte: 255. Everything from actual numbers to music to videos is stored using one or more of these atomic storage units called bytes.

Computer memory is much faster but usually much smaller than the disk and all memory is lost when the computer powers off. Think of memory as your working or scratch space and the disk as your permanent storage. Memory chips are kind of like human short-term memory that is prone to disappearing versus a piece of paper which is slower to read and write but *persistent*.

Programming languages present us with a higher level view of the memory in two ways: we can use names to refer to locations in memory and each memory cell can hold integer and real number values of arbitrary size (they do you have a limit, but let's keep things simple for now). For example, here are two named values stored in memory:

<img src=images/named-memory.png width=110>

When referring to the kind of thing a value represents, we use the word **type**. The type of the "units" cell is integer and the type of "price" is real number (or floating-point number).
 
Another very common value type is string, which is really a sequence of characters. We use strings to hold place names, book titles, and any other text-based value.  We can think of strings as being a single value because the programming language hides the details.  Strings can be arbitrarily long and the programming language stores the characters as a sequence of bytes in memory. In other words, we think of it as

<img src=images/strings.png width=110>

but it is really more like this:

<img src=images/strings2.png width=110>

These basic data types are our building blocks. If we arrange many of these blocks together, we can create more complex structures.

## Data structures

One of the most common *data structures* is the **list**, which is just a sequence of memory cells.  Because we're all familiar with spreadsheets, let's visualize these data structures using a spreadsheet.  Columns in a spreadsheet are really lists, such as the following lists/columns of integers, floating-point numbers, and strings:

<img src=images/int-list.png width=60>&nbsp;&nbsp;<img src=images/float-list.png width=80>&nbsp;&nbsp;<img src=images/names-list.png width=139>

We can think of the rows of a spreadsheet as lists also. For example, the header row of a spreadsheet is really a list of strings:

<img src=images/header-row.png width=720>

All of these lists have one thing in common: the type of element is the same. But, we can also have lists with *heterogeneous* elements, which is typically what we see in spreadsheet rows:

<img src=images/sample-row.png width=750>

Spreadsheets arrange rows one after the other, which programmers interpret as a "list of lists." In the analytics or database world, we call this a **table**:

<img src=images/rows.png width=680>

If the table elements are all numbers, we call this a **matrix**. Here's a matrix with 5 rows and 2 columns:

<img src=images/matrix.png width=110>

If we arrange two lists side-by-side and kind of glue them together, we get a **dictionary**. Dictionaries map one value to another, just like a dictionary in the real world that maps a word to a definition.  Here is a sample dictionary that maps movie title to the year it won an Oscar:

<img src=images/dict.png width=220>

The spreadsheet model is a good one for understanding data structures but it's important to keep in mind that computers process one element (number or string) at a time.
As humans, we can look at the spreadsheet or data structure from above in its entirety, but programs must **walk** or **traverse** the elements of a data structure one after the other. It's kind of like sliding a magnifying glass over the elements of a list:

<img src=images/int-list-item.png width=230>

This notion of traversal abstracts to any **sequence** of elements, not just lists. For example, we will eventually traverse the lines of a text file or a sequence of filenames obtained from the operating system. Sequences are extremely powerful because it allows us to process data that is much bigger than the memory of our computer. We can process the data piecemeal whereas a list requires all elements to be in memory at once.


At this point, we have a rough idea how to plan out a program by working backwards from the result and we have an idea how to represent data in memory. To further clarify how to plan out a program, we need to consider the set of possible operations.

## Programming patterns

As we discussed above, programmers draw from a set of  templates when choosing an overall program plan. The same is true of the individual operations themselves.  Programmers have a catalog of common operations that we  rely on when choosing the steps of a plan.  We can call these common operations (and their mapping to code) *programming patterns*. 

We've already seen a number of these patterns, such as:

* *sum the numbers in a list*
* *count the numbers in a list*.

But we can abstract those further into:

* *traverse a sequence and accumulate a value*
* *count the number of elements in a sequence*. 

The more abstract the pattern, the more widely applicable it is. For example, counting the number of elements is actually just a special case of (the more abstract) accumulating a value while traversing a sequence. Instead of adding the values at each position in a sequence, for example, we would always just add one. 

The kinds of patterns we use depends partly on a programmer's style but is heavily influenced by the capabilities of the programming language and its libraries of pre-existing functionality. Let's identify some of the most useful patterns and then try to plan out some programs using them.

### Map

One of the most common patterns maps one sequence to another, applying an operator or function to each element. For example, using a spreadsheet to create a new column containing the unit price discounted by 5% starts like this:

<img src=images/map-discount.png width=120>

And then we drag the formula down the column so that it is applied to each element of the unit price column.  The  best way to think about the map pattern is "*transform one sequence into another by applying an operator or function.*"

What we're actually doing, though, is traversing the sequence of elements in one list, computing a new value, and injecting the new value into a new list:

<img src=images/map-discount-op.png width=390>

### Combine

As a variation on map, we can combine values from multiple input sequences to form a new sequence. For example, to compute the cost of a sales transaction, we multiply the quantity times the unit price. In a spreadsheet, that looks like this:

<img src=images/map-formula.png width=250>

Programmatically, what we're doing is multiplying the *ith* element from two different sequences and placing the result in the *ith* position of an output sequence:

<img src=images/map-mult.png width=490>

variations for duplicate. just multiply by one or at zero. or f(x) = x function. identity function.
 
### Filter

### Remove duplicates

### Sort

### Accumulate

An accumulator traverses a sequence of elements and accumulates a value. For example, to sum the numbers in a sequence, we use the accumulator pattern with the `+` operator:

<img src=images/accumulator.png width=290>

We can use any other arithmetic operator we want, such as `*`. In fact, we can use any function that takes two "input" numbers and returns a new value. For summing, the two "input" numbers of the function are the previous accumulated value and the next value in the sequence. The result of that function is the new accumulated value. `+` and `*` are the most common operators. 

You will also see this pattern called *reduce*, made famous by the *map*/*reduce* term from Hadoop.

Counting the number of elements uses the `+` operator with the previous accumulated value and a fixed 1 value instead of the next element in the sequence.

## Computation model

Memory just holds data; all of the action happens in the processor, which has five principal operations:
 
* load chunks of data from memory into the processor
* perform arithmetic computations
* conditionally perform computations
* repeat steps
* store chunks of data back to memory

Processors execute low-level *machine instructions* that perform one or more of those principal operations. Each instruction does a tiny amount of work but the processor can do them extremely fast, on the order of billions a second.  A program then is just a sequence of these low-level instructions. Writing a program in these low-level machine instructions would be extremely tedious, so we typically use programming languages such as Python to make our lives easier. Each high-level instruction such as the following actually force the processor to execute multiple low-level instructions.

```
total = cost + tax
```

The processor must load `cost` and `tax` from memory, add the two values, then store the result in memory at the address associated with `total`.

Unless given instructions to the contrary, the processor keeps executing instructions one after the other.
 
## operations

First, what are you given? what's unknown? Ok, now write down the comp u expect to perform. Now give some samples,
 
Step one means getting a list of numbers, which we can assume is a given.

is this similar to something I've solved before?

 by starting at the last step in working our way backwards

 this highlights that you should start from the result, the last step, and work your way backwards

analogy with a food truck that picks up raw materials at one spot drives down the road chooses a fork in the road, prepares food en route, then delivers prepared food at a different location. This might circle back to get more  raw materials.
 
 At the other extreme there can be preprogrammed high-level operations that can, for example, display a bar chart given a list of numbers.
 
**Acknowledgements**. Conversations with [Kathi Fisler](http://cs.brown.edu/~kfisler/) provided a lot of inspiration for the disciplined, planned approach to programming summarized here. For more on design recipes, see [Transferring Skills at Solving Word Problems from Computing to Algebra Through Bootstrap](https://cs.brown.edu/~sk/Publications/Papers/Published/sfkf-trans-word-prob-comp-alg-bs/paper.pdf).