# Common Programming Patterns

As we've discussed, programmers draw from a set of templates when choosing an overall program plan. The same is true of the individual operations themselves.  Programmers have a catalog of common operations that they rely on when choosing the steps of a plan.  We can call these common operations (and their mapping to code) *programming patterns*.

We've already seen a number of these patterns, such as:

* *sum the numbers in a list*
* *count the numbers in a list*.

But we can abstract those further into:

* *traverse a sequence and accumulate a value*
* *count the number of elements in a sequence*. 

The more abstract the pattern, the more widely applicable it is. For example, counting the number of elements is actually just a special case of (the more abstract) accumulating a value while traversing a sequence. Instead of adding the values at each position in a sequence, we would always just add one. 

The kinds of patterns we use depends partly on a programmer's style but is heavily influenced by the capabilities of the programming language and its libraries of pre-existing functionality. Let's identify some of the most useful patterns. Later we'll plan out programs using them.

<a name="map"></a>
## Map

Perhaps the most common pattern *maps* one sequence to another, applying an operator or function to each element. For example, using a spreadsheet to create a new column containing the unit price discounted by 5% starts like this:

<img src=images/map-discount.png width=120>

And then we drag the formula down the column so that it is applied to each element of the unit price column.  The  best way to think about the map pattern is "*transform one sequence into another by applying an operator or function.*"

What we're actually doing, though, is traversing the elements in one sequence, deriving new values, and injecting the computed value into a new sequence:

<img src=images/map-discount-op.png width=390>

As a special case of map, we get the **duplicate** pattern that duplicates a stream by applying the identity function, *f(x)* = *x*, to the elements of a stream to get a new stream.

<a name="accumulate"></a>
## Accumulate

Another extremely common pattern is an accumulator that traverses a sequence of elements and accumulates a value. For example, to sum the numbers in a sequence, we use the accumulator pattern with the `+` operator. As we traverse the sequence, we update a running sum that's initialized to 0:

<img src=images/accumulator.png width=290>

We can use any other arithmetic operator we want, such as `*`. In fact, we can use any function that takes two "input" numbers and returns a new value. For summing, the two "input" numbers of the function are the previous accumulated value and the next value in the sequence. The result of that function is the new accumulated value. `+` and `*` are the most common operators. 

You will also see this pattern called *reduce*, as in *map*/*reduce* in the distributed computing world of Hadoop and Spark.

A **counter** is a special case of an accumulator that counts the number of elements in a sequence. It also uses the `+` operator but the two "input" numbers are the previous accumulated value and a fixed 1 value, not the next element in the sequence.

We can update multiple running accumulated values, not just one. For example, let's say we wanted to count the number of even and odd values in a sequence. We need two accumulator values, both starting at zero, but the pattern is the same:

<img src=images/accumulator-even-odd.png width=320>

The `+1` indicates an "add one to accumulated value" operation applied at each step.

<a name="combine"></a>
## Combine

As a variation on map, we can combine or merge values from multiple input sequences to form a new sequence. For example, to compute the cost of a sales transaction, we multiply the quantity times the unit price. In a spreadsheet, that looks like this:

<img src=images/map-formula.png width=250>

Dragging that formula down the Cost column, applies the formula to the following rows, thus, filling the new column.
 
Programmatically, what we're doing is multiplying the *ith* element from two different sequences and placing the result in the *ith* position of the output sequence:

<img src=images/map-mult.png width=490>

<a name="split"></a>
## Split

The opposite of combining is splitting where we split a stream into two or more new streams. For example, I often have to split the full names in a list into their first and last names. In a spreadsheet, we make a blank column:

<img src=images/split-names.png width=250>

and then split on the space character (In Excel, you use `Data` > `Text to Columns`) to get two new columns:

<img src=images/split-names-after.png width=160>

We could "undo" this split using a *combine* operation with the string concatenation operator, which would combine first and last names together into a new stream containing full names again.

Another common use of splitting is to take a string representing a string of numbers and split it into a list with those numbers. We'll see this again when we look at loading comma-separated value (CSV) files in [Loading files](https://github.com/parrt/msan501/blob/master/notes/files.md).

<a name="sort"></a>
## Sort

Programmers sort lists of strings and numbers all the time. I use the term list not sequence because typically we only sort data structures that are completely in memory, whereas a stream could be 3 terabytes on the disk.  One use case for sorting is to provide more organized output for human consumption. For example, we might want to sort a list of names:

<img src=images/sort-names.png width=210>

With data tables, we often sort entire rows by a specific column, keeping all data within a specific row together as a unit. Here's an example that sorts a table by GPA in *reverse order*:

<img src=images/sort-gpa.png width=280>

(Recall that rows typically represent data about a specific entity that should be kept together.)

Sorting can also be used as part of a computation. For example, to compute the median of some numbers we can sort the numbers and pick the middle value (if there is an odd number of elements).

A weaker version of sorting is **group by**, which also makes sure that all elements with the same value are grouped together. The difference is that the order of the groups is not necessarily sorted.

<a name="slice"></a>
## Slice

Most of the patterns we've examined so far yield lists or sequences that have the same size as the input sequence, but there are many patterns that yield subsets of the data. The first such pattern is *slice*, which extracts a subset of a list. (Again, here I explicitly use the term list to indicate that slicing generally occurs on a data structure that fits in memory.)

Programmers often use sentinel values to indicate the beginning or end of interesting list regions. For example, let's say that 999 indicates the end of interesting rainfall data coming from a rain sensor. Here's a visualization that takes a slice (subset) of the rainfall data up to but not including the sentinel value:

<img src=images/slice.png width=210>

The slice pattern is a function of two values, a start and end position within a list.  In this case, we slice from the first position to the 5th position, inclusively.  

*Warning*: Most languages and libraries assume the ending slice position is exclusive, which would mean slicing from the first position to the 6th position, in this case. To make matters more complicated, Python but not R, starts counting at 0 not 1. It's hard to switch back and forth between Python and R in this respect, so it's good to highlight here so you keep it in mind.

<a name="uniqify"></a>
## Remove duplicates

The slice pattern takes a contiguous subset but we often want to extract noncontiguous subsets.  The *remove duplicates* pattern yields a subset of a list that does not contain duplicate values. In other words, we are deriving a **set** from a list. For example, we might want a unique set of customers derived from a list of sales transactions:

<img src=images/unique.png width=290>

<a name="filter"></a>
## Filter

The most general pattern used to extract data from a list or  sequence is called *filter*. For example, using Excel's filter mechanism, we can filter a Shipping column for those values less than $10:

<img src=images/filter-shipping.png width=170>

The filter pattern is very similar to the map pattern. Map applies a function to each element of a sequence and creates a new sequence of the same size. Filter tests each element for a specific condition and, if true, adds that element to the new sequence.

<img src=images/filter-apply.png width=590>

We can also filter on one column but keep the data within each row together. Here is an example, using Excel, that filters Oscar winners from the list of nominees (the condition is *winner equals 1*):

<img src=images/filter-winners.png width=590>

<a name="search"></a>
## Search

The filter pattern finds all elements in a sequence that satisfy a specific condition, but often we'd like to know which element satisfies the condition first (or last). This brings us to the *search* pattern. At its most general, search returns the first (or last) position in the sequence rather than the value at that position. If we have the position, often called the *index*, we can always ask the sequence for the value at that position.

For example, searching for `999` in the rainfall sensor data from the slice pattern above, yields the 6th position.  Most programming languages (Python but not R) count from 0 not 1 so a search for `999` would yield index 5 not 6 in this case:

<img src=images/search-rainfall.png width=180>

The search pattern can even be used within a string (list of characters) to find the position of a character of interest. For example, to slice up a full name into first and last names, we can combine a search for the space character with two slice operations. Given full name `Xue Li`, a search for the space character returns the fourth position or index 3. To extract the first name, we slice from index 0 to index 3, exclusively. To get the last name, we slice from index 4 to 6, exclusively. 

<img src=images/split-string.png width=190>

To determine the index of the end of the string, programmers tend to use the length of the string. The length works out to be an index whose value is one past the end of the string, which is what we want for a slice using an exclusive right index.

## Summary

The two most commonly-used patterns are probably map and filter but here's a handy list:

* Map.  Apply an operator or function to every element of a sequence.
* Accumulate.  Accumulate a value or values while traversing a sequence.
* Combine.  Create a new sequence by combining values from multiple sequences.
* Split. Split one sequence into multiple.
* Sort. Sort a list or sort a table by a column.
* Slice.  Extract a continuous subset of a list.
* Remove duplicates.  Convert a list to a set, with unique elements.
* Filter. Extract a subset of a sequence whose values satisfy a specific condition.
* Search. Find the first or last index (position) of a specific value in a list.

Armed with these patterns and the overall program template, we are ready to start programming by planning out programs using pseudocode.