# Reading and writing files

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

## Loading text files

As we discussed early in the semester, files are just bits. It's how we interpret it that is meaningful. The bits could represent an image, a movie, some text, Python program text, whatever.

Text files are usually 1 byte (8 bits) per character and have the notion of a line. A line is just a sequence of characters terminated with either `\r\n` (Windows) or `\n` (UNIX, Mac). A text file is usually then a sequence of lines.

A binary file is, well, anything else. It still could represent an image or a song but we know at least it's not text.

https://raw.githubusercontent.com/parrt/msan501/master/data/berlitz1/IntroIstanbul.txt

You cannot do anything after the file is closed

```
f = open('/tmp/foo.txt', 'w')
f.close()
f.read()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: I/O operation on closed file
```

## Loading data files

data file

One value per row, no header:

https://raw.githubusercontent.com/parrt/msan501/master/data/prices.txt


https://raw.githubusercontent.com/parrt/msan501/master/data/player-heights.csv

### Opening/closing files

Here is how to open and immediately close a file:

```
f = open('/tmp/foo.txt', 'w')
f.close()
```

The second argument indicates whether we are going to read `"r"`, write `"w"`, or append `"a"`.

The file `/tmp/foo.txt` is created if it doesn't already exist because of the `"w"`.


### Reading from a text file

Now lets use the `"r"` file open mode.

Assume `/tmp/names.txt` has:

```
3 parrt
2 jcoker
8 tombu
```

**PATTERN**: load all file contents into string

```
f = open('/tmp/names.txt', 'r')
contents = f.read() # read all content of the file
f.close()
print contents
```

Reading the entire contents is often not as useful as reading the input line by line. Because it is a text file, we know there are \n characters there:

```
$ od -c /tmp/names.txt
0000000 3 p a r r t \n 2 j c o k e r
0000020 \n 8 t o m b u \n
0000031
```

**Q.** `open("/tmp/names.txt")` is the same as `open("/tmp/names.txt", "r")`. How does that work?

Here is how we could read in the three lines of the file:

```
f = open('/tmp/names.txt')
first = f.readline()
second = f.readline()
third = f.readline()
f.close()
print first, second, third
```

That prints the same thing as we had before except now we have access to the individual lines. Also note that `readline()` strips off the newline but we get it back because of the normal newline given by print.

Here's how to split the entire contents into lines with a single read:

```
f = open('/tmp/names.txt')
contents = f.read() # read all content of the file
f.close()
lines = contents.strip().split("\n")
```

The `strip()` is important because it drops the last newline, which would otherwise give us an empty string as the last element. It's easier to do this:

**PATTERN**: get all lines in a file into memory

```
f = open('/tmp/names.txt')
lines = f.readlines()
f.close()
print lines # note that this keeps the \n on the end of lines
```

That works well except that it requires we load everything into memory, which is pretty inefficient and limits the size of the data we can process.

**PATTERN**: To read data in line by line easily, we can use the `for` loop:

```
f = open('/tmp/names.txt')
for line in f: # for each line in the file
 print line,
f.close()
```

Once we have a line of text, we can treat them like we did when we had raw input from the user.

```
f = open('/tmp/names.txt')
for line in f: # for each line in the file
    print line.strip().split(" ")
f.close()
```

### Writing to a text file

To write a text file, we open with `"w"` mode, do some `write()`s, and make sure to close. If you use `"r"` instead of `"w"` and then `write()`, you will get this error:

```
IOError: File not open for writing
```

Sample code:

```
f = open('/tmp/foo.txt', 'w')
f.write("This is easy\n") # we need \n in there
f.write("Ok, not too bad\n")
f.close()
```

When you execute that code you get what you would expect into `/tmp/foo.txt`:

```
$ cat /tmp/foo.txt
This is easy
Ok, not too bad
```

**PATTERN**: Write a floating-point number to a file in text representation (not binary):

```
f = open('/tmp/foo.txt', 'w')
f.write("32.921323\n")
f.close()
```

```
$ cat /tmp/foo.txt
32.921323
```

**PATTERN**: Write a list of words to a file, one per line:

```
words = "Dogs have masters Cats have staff".split(" ")
f = open('/tmp/foo.txt', 'w')
for w in words:
    f.write(w)
    f.write("\n")
f.close()
```

```
$ cat /tmp/foo.txt
Dogs
have
masters
Cats
have
staff
$
```