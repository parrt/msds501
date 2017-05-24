# Program Efficiency

How fast will the programs derived from these work plans execute?  We can't really answer that question because it depends on the speed of the processor (computer) running the code and how we translated the plan to code. On the other hand, we can say quite a bit about how efficient or complex a work plan is. Program *complexity* is so important that is worth spending a bit of time introducing the concept right from the beginning.

Consider manually accumulating a running sum from the values in a list. Clearly this will take us more time the longer the list. The same is true for computers. We can generally make the assumption that the same program processing larger data structures takes more time than smaller data structures.  Take another look at the image from our discussion of the accumulator pattern, but this time notice the time steps:

<img src=images/accumulator.png width=290>

It costs the computer a CPU "clock tick" every time it moves the "magnifying glass" to examine the next value.  Programmers say that the cost of traversing a list is *on the order of the length of the list*.

The order or *complexity* of the problem doesn't change if we compute more values at each time step, as long as it's a fixed number of operations. For example, the combine operation we discussed to compute sales cost has the same complexity as the accumulator:

<img src=images/map-mult.png width=490>

We can look at multiple values at each time step, but the cost of traversing two lists simultaneously instead of one is still dominated by the length of the lists.
