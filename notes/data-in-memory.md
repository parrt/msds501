# Representing data in memory

So far, we've glossed over the details of loading data into memory from disk (step 2 in our plan above) but the way we represent data in memory is critical to building programs. This is particularly true with analytics programs because processing data is our focus.  Let's take a bit of a detour into computer architecture to get a handle on what it means to load something into memory.

A computer consists of three primary components: a disk to hold data, a memory (that is wiped upon power off), and a processor (CPU) to process that data. Here is a picture of an actual CPU and some memory chips:

<img src=images/cpu-memory.png width=400>

The memory is broken up into discrete cells of a fixed size. The size of a cell is one *byte*, which consists of 8 *bits*, binary on/off digits. It is sufficient to hold a number between 0 and 255. Each cell is identified by an integer address, just like the numbers on mailboxes (see image below and to the right). Processors can ask for the data at a particular address and can store a piece of data at a specific memory location as well. For example, here is an abstract representation of byte-addressable computer memory:

<img src=images/addresses.png width=80>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="images/mailboxes.png"  width=70>

In this case, the memory has value 100 at address 0. At address 1, the memory has value 0. Address 4 has the maximum value we can store in a single byte: 255. Everything from actual numbers to music to videos is stored using one or more of these atomic storage units called bytes.

Computer memory is much faster but usually much smaller than the disk and all memory is lost when the computer powers off. Think of memory as your working or scratch space and the disk as your permanent storage. Memory chips are kind of like human short-term memory that is prone to disappearing versus a piece of paper which is slower to read and write but *persistent*.

Programming languages present us with a higher level view of the memory in two ways: we can use names to refer to locations in memory and each memory cell can hold integer and real number values of arbitrary size (they do have a limit, but let's keep things simple for now). For example, here are two named values stored in memory:

<img src=images/named-memory.png width=90>

<img src="images/redbang.png" width=30 align="left">When referring to the kind of thing a value represents, we use the word **type**. The type of the "units" cell is integer and the type of "price" is real number (or floating-point number).

Another very common value type is *string*, which is really a list of characters. We use strings to hold place names, book titles, and any other text-based values.  We can think of strings as being a single value because the programming language hides the details.  Strings can be arbitrarily long and the programming language stores the characters as a sequence of bytes in memory. In other words, we think of it as

<img src=images/strings.png width=110>

but it is really more like this:

<img src=images/strings2.png width=110>

These basic data types (integers, floating-point numbers, and strings) are our building blocks. If we arrange some of these blocks together, we can create more complex structures.

## Data structures

### List

One of the most common *data structures* is the **list**, which is just a sequence of memory cells.  Because we're all familiar with spreadsheets, let's visualize these data structures using a spreadsheet.  Columns in a spreadsheet are really lists, such as the following lists/columns of integers, floating-point numbers, and strings:

<img src=images/int-list.png width=60>&nbsp;&nbsp;<img src=images/float-list.png width=80>&nbsp;&nbsp;<img src=images/names-list.png width=139>

We can think of the rows of a spreadsheet as lists also. For example, the header row of a spreadsheet is really a list of strings:

<img src=images/header-row.png width=750>

All of these lists have one thing in common: the type of element is the same. They are *homogeneous*. But, we can also have lists with *heterogeneous* elements, which is typically what we see in spreadsheet rows:

<img src=images/sample-row.png width=800>

Heterogeneous lists are typically used to group bits of information about a particular entity. In machine learning, we call this a **feature vector**, an **instance**, or an **observation**.  For example, an apples versus oranges classifier might have feature vectors containing weight (number), volume (number), and color (string).  The important point here is that a list can also be used to as a way to aggregate features about a particular entity. The sequence of the elements is less important than the fact that they are contained (aggregated) within the same list. We will see this notion again when we talk about *tuples* in [Extracting information from text](text.ipynb).

### Set

If we enforce a rule that all elements within a list are unique, then we get a **set**. In that case, we also tend not to care about the order.

### Tables (list of lists)

Spreadsheets arrange rows one after the other, which programmers interpret as a *list of lists.* In the analytics or database world, we call this a **table**:

<img src=images/rows.png width=700>

In this example, each row represents a sales transaction.

The input to machine learning algorithms is often a table where each row aggregates the data associated with a specific instance or observation. 

### Matrix

If the table elements are all numbers, we call it a **matrix**. Here's a matrix with 5 rows and 2 columns:

<img src=images/matrix.png width=110>

### Dictionary

If we arrange two lists side-by-side and kind of glue them together, we get a **dictionary**. Dictionaries map one value to another, just like a dictionary in the real world maps a word to a definition.  Here is a sample dictionary that maps a movie title to the year it was nominated for an Oscar award:

<img src=images/dict.png width=220>

## Traversing data structures

The spreadsheet model is a good one for understanding data structures but it's important to keep in mind that computers process one element (number or string) at a time.
As humans, we can look at the spreadsheet or data structure from above in its entirety, but programs must **walk** or **traverse** the elements of a data structure one after the other. It's kind of like sliding a magnifying glass over the elements of a list:

<img src=images/int-list-item.png width=230>

This notion of traversal abstracts to any **sequence** (or **stream**) of elements, not just lists. For example, we will eventually traverse the lines of a text file or a sequence of filenames obtained from the operating system. Sequences are extremely powerful because it allows us to process data that is much bigger than the memory of our computer. We can process the data piecemeal whereas a list requires all elements to be in memory at once.

For lists and other structures that fit completely in memory, we often find a **reverse traversal** useful, that examines elements from last to first.

At this point, we have a rough idea how to plan out a program by working backwards from the result and we have an idea how to represent data in memory. To further clarify how to plan out a program, we need to consider the set of possible operations.

## Summary

Here are the commonly-used data types:

* integer numbers like -2, 0, 99
* real numbers (floating-point numbers) like -2.3, 99.1932
* strings like "Mary", "President Obama"

And here are the commonly-used data structures:

* ordered list
* set (just an unordered, unique list)
* list of lists such as tables or matrices with rows and columns 
* dictionary such as mapping a student name to their student ID; we can think of this as a table where each row in the table associates the key with a value.Is