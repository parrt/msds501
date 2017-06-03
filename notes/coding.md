# How to Code

*in progress*

Now that we've studied a problem-solving process and learned the common programming patterns using pseudocode, it's finally time to express ourselves using actual Python programming language syntax. Keep in mind that, to implement any program, we should follow the problem-solving process and write things out in pseudocode first. Then, coding is a simple matter of translating pseudocode to Python.

Let's review our computation model.  Our basic raw ingredient is data and that lives on our disk typically (or SSDs nowadays). Note: we might have to go get that data with code; see MSAN692. The disk is very large but cannot serve up data fast enough for the processor, which is orders of magnitude faster than the disk. Consequently, our first act in an analytics program is often to load the data from the disk into temporary memory. The memory is faster than the disk but smaller and disappears when the power goes off. The processor is still much faster than the memory but we have lots of tricks to increase the speed of communication between the processor and memory (e.g., caches).

The processor is where all of the action occurs because it is the entity that executes the statements in a program. The operations in a program boil down to one of these fundamental instructions within the processor:

* load small chunks of data from memory into the CPU
* perform arithmetic computations on data in the CPU
* store small chunks of data back to memory
* conditionally perform computations
* repeat operations

In [Model of Computation](computation.md), we studied pseudocode that maps to one or more of these fundamental instructions. We saw how some of the [higher-level programming patterns](patterns.md) map down to pseudocode chosen from these fundamental instructions. We finished up by looking at some of the [low-level programming patterns](combinations.md) that combine fundamental instructions to do useful things like filtering and image processing.

## Getting started

In order to write code in Python professionally, we have a lot of details to learn, just like we would when learning a new natural language. The act of translating a pseudocode operation into Python involves choosing the right Python construct, just like programming involves choosing the right pattern to solve a piece of a real-world problem. The detail comes in when we shoehorn our free-form pseudocode into the straitjacket of programming language syntax.

## Python program template

To simplify the process of learning to code in Python, we're going to restrict ourselves to a subset of the language and also follow a template suitable for all programs:

*import any libraries*<br>
*define any constants, simple data values*<br>
*define any functions*<br>
*main program body*

When we are building a library not a program, then we omit the main program:
 
*import any libraries*<br>
*define any constants, simple data values*<br>
*define any functions*<br>
