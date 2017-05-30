## Common lower-level programming patterns

*in progress*

As with natural language, we can combine any of the basic sentence structures to form more complex sentences. In the programming world, that means **nesting** one operation in another. In this section, we'll explore a few of the interesting combinations.

### Nested loops

We sometimes need to repeat repeated instructions, which we call a *nested loop*. For example, the risotto recipe goes on to say:

> Continue adding broth 1/2 cup at a time, stirring continuously, until the liquid is absorbed and the rice is *al dente*, about 15 to 20 minutes.

We are supposed to add broth until we run out of it, 1/2 cup at a time.  For each 1/2 cup we add, we are to stir until it is absorbed. Making the recipe more precise, we might express it like this as a nested loop:

*while there is more broth:*<br>
&nbsp;&nbsp;&nbsp;&nbsp;*add 1/2 cup broth to pot*<br>
&nbsp;&nbsp;&nbsp;&nbsp;*while broth not absorbed:*<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*stir rice in pot*

We are wrapping our previous loop in an outer loop. This code pops out from our loop template by identifying the two conditional expressions and the loop operations.

In the analytics world, nested loops are hugely important because we use them to process matrices, images, and tables of data.

Let's get started by summing the numbers in a 3x3 matrix:

<img src=images/matrixA.png width=100>

Recall that, while we can look at the entire matrix at once, a computer examines each element one-by-one. Because this is not a one-dimensional data structure, we can't use a simple "for each element in the matrix" loop. The most common template for iterating through all elements of an *n* x *m* matrix looks like this:

*for i in 0..n-1:*<br>
&nbsp;&nbsp;&nbsp;&nbsp;*for j in 0..m-1:*<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*do something with matrix<sub>i,j</sub>*

where *matrix<sub>i,j</sub>* accesses the element at row *i* and column *j*.  Such a nested loop gives all possible combinations of *i* and *j*, which is what we want when we operate on a matrix. Consider the following use of that template to print out all of the two-dimensional indices:

*for i in 0..n-1:*<br>
&nbsp;&nbsp;&nbsp;&nbsp;*for j in 0..m-1:*<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*print j without newline*<br>
&nbsp;&nbsp;&nbsp;&nbsp;print a newline

The output would be *n* rows of `0 1 2 ... m-1`:

```
0 1 2 ... m-1
0 1 2 ... m-1
...
```

To sum all of the elements of a 3x3 matrix, we let *n*=3 and *m*=3 and use an addition operation:

*init sum to 0*<br>
*for i in 0..2:*<br>
&nbsp;&nbsp;&nbsp;&nbsp;*for j in 0..2:*<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*add matrix<sub>i,j</sub> to sum*

You might recognize this as a 2D form of an accumulator pattern.

As a more realistic example, let's add two matrices A and B together to form C. The key operation is to add A<sub>i,j</sub> to B<sub>i,j</sub> to get C<sub>i,j</sub>. Visually, it looks like this:

<img src=images/ABC.png width=360>

**Exercise**: Write out the pseudocode nested indexed-loop to add matrices together.

<img src=images/obama-zoom.png width=400>

<img src=images/rows.png width=700>


### Conditional in a loop

One of the most common nested operations is a conditional inside of a loop. We use it to implement the [filter](patterns.md#filter) pattern, for example. The filter template looks like:

for each *x* in *a sequence*:<br>
&nbsp;&nbsp;&nbsp;&nbsp;if *condition*: add *x* to new list<br>

To convert a real-world filtering problem to pseudocode, your goal is to identify the sequence and the condition in that template. To filter out negative values (filter in nonnegative values) as we did in the rainfall problem, the *sequence* is the rainfall list and the *condition* is "*x >= 0*":

*for each x in rainfall*:<br>
&nbsp;&nbsp;&nbsp;&nbsp;*if x>=0: add x to new list*<br>
