# A first taste of Python tools

## Launch a commandline app

Launch `Terminal.app` (Mac) or whatever the `bash` *terminal*, *shell*, or *commandline prompt* program is on your flavor of UNIX. You should see a blinking cursor and a `$` prompt:

```bash
$ 
```

The `$` sign above is just the prompt that indicates the terminal is waiting for you to type something. After command executes, you will see the `$` prompt again.

The commandline is a very low-level interface for communicating with the operating system of your computer. You can think of the terminal as the diagnostics computer that mechanics plug into your car to really take control. The dashboard is analogous to the windowing graphical interface we use most of the time.  Becoming a programmer is like becoming a mechanic; sometimes you need more powerful but more complicated tools to operate machinery.

The command line is actually a full programming language with loops and everything but most of the time we simply execute commands. Commands have arguments just like function calls in a programming language have arguments. Here's how to say hello from the command line:

```bash
$ echo "hello"
hello
$ 
```

The `echo` command is analogous to the `print` command in Python code. Commands are terminated by hitting the return key.  After executing the command, the prompt returns indicating you can type another command. 

##  Interactive Python

From the `$` prompt, type `ipython` (or `python`) followed by return/newline:

```bash
$ ipython
Python 2.7.12 |Anaconda 4.2.0 (x86_64)| (default, Jul  2 2016, 17:43:17) 
Type "copyright", "credits" or "license" for more information.

IPython 5.1.0 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.
In [1]: 
```

You should see that it is using the **Anaconda** version. If not, that means you are using the default Python on your system. To figure out where the Python program executable is using the command line, type `which ipython` like this:

```bash
$ which python
/Users/parrt/anaconda2/bin/python
$ which ipython
/Users/parrt/anaconda2/bin/ipython
```

Both of the programs are in the Anaconda `bin` (binary) directory, that holds all of the binary executables. If you don't see anaconda somewhere in the output from the `which` command, you need to look at the documentation for Anaconda and figure out why you are not running the appropriate Python. (Most likely something is wrong with your `PATH` environment variable.) That's okay for now as we can use any 2.X version of Python running.

Now, from the Python prompt "`In [n]`" (we are no longer in `bash`), type `500+1` followed by newline. You should see something like this:

```python

In [1]: 500+1
Out[1]: 501

In [2]: 
```

Python has evaluated the expression and printed the result back to the screen. It is as if we had used a `print` statement, which gives us the same result:

```python
In [2]: print 500+1
501

In [3]: 
```

The Python interactive shell prints expression values immediately, but that is not the case when running a program as a script (i.e., not interactively).

To exit the interactive shell and go back to the command line (the terminal program), say `quit` (or control-D) and hit return:

```bash
In [3]: quit
$ 
```

The `$` prompt indicates that you are back at the bash command line.

## Scripting Python

Go to a suitable directory (folder) on your disk, or create one, such as `/Users/YOURID/msan501/inclass`. (**Do not use spaces in any of your directory or file names...ever!**) Now create a **text file** called `hello.py` that contains exactly one line:

```python
500+1
```

This is exactly what you typed in first in the interactive Python shell. Save the file in the `inclass` directory.

Here are solutions to  the most common errors:

1. Do not put `.txt` at the end of the file name; it must be `.py`
2. Do NOT use M$ Word or any other word processor; You think it's text but it's not. There are lots of text editors out there including Mac's `TextEdit.app`. Just make sure save as plain text not "rich text". There are also plenty of text editor such as [Sublime](https://www.sublimetext.com/) and [TextMate](https://macromates.com/).  (If you are really hard-core, you will learn `vi` or `emacs`, which you will see me use in class.) You can also use `nano` from the command line for editing directly in the command line window.

Once you get the Python file written to the disk, you should be able to jump to that directory using `cd` (change directory) from the commandline:

```bash
$ cd /Users/YOURID/msan501/inclass
```

Use `ls` to get a directory listing:

```bash
$ ls
hello.py
```

Now, we're going to run that program/script:

```bash
$ ipython hello.py
$ 
```

We do not get any output. This is a critical difference. The interactive Python shell immediately prints expression values because it is interactive. When you run a file from the commandline, it assumes you wanted to execute the code like a script in batch mode. That is why we do not get any output without a print statement.

Now edit that file and change it to

```python
print 500+1
```

Save the file and rerun it. Now you should see:

```bash
$ ipython hello.py 
501
$ 
```

## PyCharm

Now, we're going to do the exact same thing except using the development environment PyCharm, which you all should've downloaded and installed.

1. Launch PyCharm and then under `File` menu, tell it to open a directory with `Open...` menu item. 
2. Navigate to your `/Users/YOURID/msan501/inclass` directory and click okay. You should see your `hello.py` in the `Project` pane of the development environment. 
3. Double-click on it to open it in the editor pane.
4. Right click in the editor window and select `Run hello` item. Another pane will open on the bottom of the IDE that looks something like:

<img src=images/pycharm.png width=400>

Notice the `501` output in the console below the program text.

**You should be able to test out small programs or Python snippets very very quickly. Rehearse these procedures until they are second nature.**