# Loading files

The goal of this lecture-lab is to learn how to extract data from files on your laptop's disk. We'll load words from a text file and numbers from data files.  Along the way, will learn more about filenames and paths to files. To make loading data meaningful, we'll also learn how to generate histograms from data files using [matplotlib](https://matplotlib.org/).

## What are files?

As we've discussed before, both the disk and RAM are forms of memory. RAM is much faster (but smaller) than the disk but RAM all disappears when the power goes out. Disks, on the other hand, are persistent. A file is simply a chunk of data on the disk identified by a filename. You use files all the time. For example, we can double-click on a text file or Excel file, which opens an application to display those files. 

We need to be able to write Python programs that read data from files just like, say, Excel does.  Accessing data in RAM is very easy in a Python program, we simply refer to the various elements in a list using an index, such as `names[i]`.  File data is less convenient to access  because we have to explicitly load the file into working memory first.  For example, we might want to load a list of names from a file into a `names` list. 

If a file is too big to fit into memory all at once, we have to process the data in chunks.  For now, let's assume all files fit in memory. 

Even so, accessing files is a bit of a hassle because we must explicitly tell Python to open a file and then close it when we're done. We also must distinguish between reading and writing from/to a file, which dictates the mood in which we open the file.  We can open the file in read, write, or append mode. For this lab, we will only concern ourselves with the default case of "opening a file for reading." Here is how to open a file called `/tmp/foo.txt` in read mode (the default) then immediately close that file:

```
f = open('/tmp/foo.txt')  # open for read mode
f.close()                 # ok, we're done
```

Hmm...what kind of object is returned from `open()` and stored in `f`? Why do we have to close files?

**File descriptors**

When we open a file, Python gives us a "file object" that is really just a handle or cookie that the operating system gives us. It's a unique identifier and how the operating system likes to identify a file that we work with. The file object is not the filename and is also not the file itself on the disk. It's really just a descriptor and a reference to the file.

We will use a filename to get a file object using `open()` and use the file object to get the file contents.

The close operation informs the operating system that you no longer need that resource. The operating system can only open so many files at once so you should close files when you're done using them. 

Later, when you are learning to write data to files, the close operation is also important. Closing a file flushes any data in memory buffers that needs to be written. From the Python documentation:

> "It is a common bug to write a program where you have the code to add all the data you want to a file, but the program does not end up creating a file. Usually this means you forgot to close the file."

<img src="images/redbang.png" width=30 align="left"> To help avoid confusion, keep this analogy in mind. Your house (file) contents is different than your address (file name) and different than a piece of paper with the address written on it (file descriptor). More specifically:

1. The filename is a string that identifies a file on the disk. It can be fully qualified or relative to the current working directory.

2. The file object is not the filename and is also not the file itself on the disk. It's really just a descriptor and a reference to the file.

3. The contents of the file is different than the filename and the file (descriptor) object that Python gives us.

**File names and paths**

You know what a file name is because you've created lots of files before. (BTW, another reminder not to use spaces in your file or directory names.) *Paths* are what we call fully qualified filenames because they give a description of the directories from the root of the file system. The root of the file system is identified with `/` forward slashat the start of a pathname. You are probably used to seeing it as "Macintosh HD" but from a programming point of view, it's just `/`. Here's a useful diagram showing the components of a fully qualified pathname to a file called `view.py`:

<img src=images/path-names.png width=750>

As a shorthand, you can start a path with `~`, which means "my home directory". On a Mac that's `/Users/parrt` or whatever your user ID is. On Linux, it's probably `/home/parrt`.

The last element in a path is either a filename or a directory. For example to refer to the directory holding `view.py` in the above diagram, use path `/Users/parrt/classes/msan501/images-parrt`. Or, using the shortcut, the fully qualified path is `~/classes/msan501/images-parrt`. Here's an example bash session that uses some fully qualified paths:

```bash
$ ls /Users/parrt/classes/msan501/images-parrt/view.py
/Users/parrt/classes/msan501/images-parrt/view.py
$ cd /Users/parrt/classes/msan501/images-parrt $ pwd
/Users/parrt/classes/msan501/images-parrt
$ cd ~/classes/msan501/images-parrt
$ pwd
/Users/parrt/classes/msan501/images-parrt
```

**Current working directory**

All programs run with the notion of a *current working directory*. So, if a program is running inside the directory `~/classes/msan501/images-parrt`, then the program could refer to any data files sitting in that directory with just a file name--no path is required.  For example, let's use the `ls` program to demonstrate the different kinds of paths.

```bash
$ cd ~/classes/msan501/images-parrt
$ ls
view.py
$ ls /Users/parrt/classes/msan501
images-parrt/
$ ls /Users/parrt/classes
msan501/
```

Any path that does not start with `~` or `/` is called a *relative pathname*. For completeness, note that `..` means the directory above the current working directory:

```bash
$ cd ~/classes/msan501/images-parrt
$ ls ..
images-parrt/
$ ls ../..
msan501/
```

Oh, you will often see me use `/tmp`, which is a temporary directory or dumping ground.  All files in that directory are usually erased when you reboot.

## Loading text files

As we discussed early in the semester, files are just bits. It's how we interpret the bits that is meaningful. The bits could represent an image, a movie, an article, data, Python program text, whatever. Let's call any file containing characters a *text file* and anything else a *binary file*.

Text files are usually 1 byte per character (8 bits) and have the notion of a line. A line is just a sequence of characters terminated with either `\r\n` (Windows) or `\n` (UNIX, Mac). A text file is usually then a sequence of lines. Download this sample text file, [IntroIstanbul.txt](https://raw.githubusercontent.com/parrt/msan501/master/data/berlitz1/IntroIstanbul.txt) so we have something to work with. You can save it in `/tmp` or whatever directory you are using for in class work. For the purposes of this discussion, I will put it in the temporary directory.

Now, let's examine the contents of the file in a raw fashion rather than with a text editor. The `od` command (octal dump) is useful for looking at the bytes of the file. Use option `-c` to see the contents as 1-byte characters:

```bash
$ od -c /tmp/IntroIstanbul.txt
0000000   \n          \n          \n                  \n                
0000020           \n                                   T   h   e       C
0000040    i   t   y       a   n   d       I   T   S       P   e   o   p
0000060    l   e  \n                                   I   s   t   a   n
0000100    b   u   l       i   s       o   n   e       o   f       t   h
...
```

Wow. That's a lot of output so let's extend the command to pipe the output to the `more` program that paginate's long input.

```bash
$ od -c /tmp/IntroIstanbul.txt | more
...
```

The `\n` character you see represents the single character we know as the carriage return. The numbers on the left are the character offsets into the file (it looks like they are octal not decimal, btw; use `-A d` to get decimal addresses).

Let's look at some common programming patterns dealing with text files.

**Pattern**: Load all file contents into a string.

```python
f = open('/tmp/IntroIstanbul.txt')
contents = f.read() # read all content of the file
f.close()
print contents
```

**Exercise**: *Without cutting and pasting*, type in that sequence and make sure you can print the contents of the file from Python. Instead of `/tmp`, use whatever directory you saved that IntroIstanbul.txt in.

**Pattern**: Load all words of file into a list.

This pattern is just an extension of the previous where we `split()` on the space character to get a list:

```python
f = open('/tmp/IntroIstanbul.txt')
contents = f.read() # read all content of the file
f.close()
words = contents.split(' ')
print words[0:100] # print first 100 words
```

We get output that looks like this:

```
['\n', '', '\n', '', '\n', '', '', '', '\n', '', '', '', '', '',
 '\n', '', '', '', '', '', '', '', 'The', 'City', 'and', 'ITS',
  'People\n', '', '', '', '', '', '', '', 'Istanbul', 'is', 'one', ...]
```

Because we are splitting on the space character, newlines and multiple space characters in a row yield "words" that are useful. We need to transform that list into a new list before it is useful.

**Exercise**: Using the *filter* programming pattern filters `words` for only those words greater than 1 character; place into another list called `words2`. Hint `len(s)` gets the length of string `s`.

## Loading all lines of a file

Reading the contents of a file into a string is not always that useful. We typically want to deal with the words, as we just saw, or the lines of a text file.  Natural language processing (NLP) would focus on using the words, but let's look at some data files, which typically structure files as lines of data.  Each line represents an observation, data point, or record. 

We could split the text contents by `\n` to get the lines, but it is so common that Python provides functions to do that for us. To give us some data to play with, download [prices.txt](https://raw.githubusercontent.com/parrt/msan501/master/data/prices.txt) that has a list of prices, one price per line. Here's another very common programming pattern:

**Pattern**: Read all of the lines of the file into a list.

```python
f = open('/tmp/prices.txt')
prices = f.readlines() # get lines of file into a list
f.close()
print prices[0:10]
```

The output you should get looks like:

```
['0.605\n', '0.600\n', '0.594\n', '0.592\n', '0.600\n', '0.616\n', '0.623\n', '0.628\n', '0.630\n', '0.629\n']
```

**Exercise**: *Without cutting and pasting*, type in that code and make sure you can read the lines of the file into a list. 

The numbers have the `\n` character on the end but that's not a problem because we can easily convert that using [NumPy](http://www.numpy.org/):

```python
import numpy as np
prices = np.array(prices, dtype='float') # convert to array of numbers
print prices[0:10]
```

**Exercise**: Add this conversion to the previous exercise and make sure you get an `array` as output:

```
array([ 0.605,  0.6  ,  0.594,  0.592,  0.6  ,  0.616,  0.623,  0.628,
        0.63 ,  0.629])
```

**Pattern**:  We can call these combined code snippets "load list of numbers into a numpy array."

## Loading CSV files

Let's look at a more complicated data file. Download [heights.csv](https://raw.githubusercontent.com/parrt/msan501/master/data/player-heights.csv), which looks like:

```
Football height, Basketball height
6.329999924, 6.079999924
6.5, 6.579999924
...
```

It is still a text file, but now we start to get the idea that text files can follow a particular format. In this case, we recognize it as a *comma-separated value* (CSV) file. It also has a header line that names the columns, which means we need to treat the first line differently than the remainder of the file.

**Pattern**: Load a CSV file into a 2D numpy array.

We already know how to open a file and get the lines, so let's do that and also separate the lines into the header and the data components:

```python
import numpy as np

f = open('/tmp/player-heights.csv')
lines = f.readlines()
f.close()

header = lines[0]
data = lines[1:]
print header
print data[0:5]
```

**Exercise**:  Type in this code and make sure you get the header and the first five lines of data printed out:

```
Football height, Basketball height
['6.329999924, 6.079999924\n', '6.5, 6.579999924\n', '6.5, 6.25\n', '6.25, 6.579999924\n', '6.5, 6.25\n']
```

Each row of the data is a string with two numbers in it. We need to convert that string into a list with two floating-point numbers using `split(',')`.  Combining all of those two-element lists into an overall list gives us the two-dimensional table we need.

**Exercise**: What pattern should we used to convert the `data` list? Convert the list of strings `data` to a list of number lists called `data2`.

```python
data2 = []
for line in data:
    row = line.split(',')
    data2.append(row)
print data2[0:3]
```

That gives output:

```
[['6.329999924', ' 6.079999924\n'], ['6.5', ' 6.579999924\n'], ['6.5', ' 6.25\n']]
```

Now we are ready to convert it to a two-dimensional array. The numpy `array()` helps us do the conversion from individual strings to numbers and also understands that a list of lists is a two dimensional array:

```python
data2 = np.array(data2, dtype='float')
print data2[0:5]
```

That gives output:

```
[[ 6.32999992  6.07999992]
 [ 6.5         6.57999992]
 [ 6.5         6.25      ]
 [ 6.25        6.57999992]
 [ 6.5         6.25      ]]
```

## Using NumPy to load CSV files

Of course, loading CSV is something that data scientists need to do all of the time and so there is a simple function you can use in the future:

```python
prices = np.genfromtxt('/tmp/prices.txt')
```

This even works for CSV files with header rows:

```python
data = np.genfromtxt('/tmp/player-heights.csv', delimiter=',', names=True)
```

The `delimiter` indicates that commas separate the data elements on a line and `names=True` indicates that there are column names in the first line of the file. If we print `data` we get:

```
array([(6.329999924, 6.079999924), (6.5, 6.579999924), (6.5, 6.25),
       (6.25, 6.579999924), (6.5, 6.25), (6.329999924, 5.920000076),
       (6.25, 7.0), (6.170000076, 6.409999847), (6.420000076, 6.75),
       ...
       (6.170000076, 6.579999924), (6.579999924, 6.829999924), (6.5, 6.5),
       (6.25, 6.579999924)], 
      dtype=[('Football_height', '<f8'), ('Basketball_height', '<f8')])
```

## Processing files line by line

The previous mechanism for getting lines of text into memory works well except that it requires we load everything into memory all at once. That is pretty inefficient and limits the size of the data we can process to the amount of memory we have.

**PATTERN**: Read data line by line not all at once.

We can use a for-each loop where the sequence of data is the file descriptor:

```
f = open('/tmp/prices.txt')
for line in f: # for each line in the file
    print float(line) # process the line in some way
f.close()
```

The output we get looks like:
```
0.605
0.6
0.594
0.592
0.6
...
```

**Exercise**: Try this new version of processing the lines of the file. No cutting and pasting!

Keep in mind that once you close the file, you can read anymore data from it:


```
f = open('/tmp/prices.txt', 'w')
f.close()
f.read()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: I/O operation on closed file
```

## Summary

The key programming patterns to take away from this lecture are:

* **Pattern**: Load all file contents into a string.
* **Pattern**: Load all words of file into a list.
* **Pattern**: Read all of the lines of the file into a list.
* **Pattern**: Load list of numbers into a numpy array.
* **Pattern**: Load a CSV file into a 2D numpy array.

You should be able to code those patterns quickly and easily, and without cutting and pasting from stackoverflow.