# Say Hello

##  Interactive Python

Launch `Terminal.app` (Mac) or whatever the `bash` *terminal* or *commandline prompt* program is on your flavor of UNIX. From the prompt, type `python` followed by return/newline:

```bash
$ python
Python 2.7.12 |Anaconda 4.2.0 (x86_64)| (default, Jul  2 2016, 17:43:17) 
[GCC 4.2.1 (Based on Apple Inc. build 5658) (LLVM build 2336.11.00)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
Anaconda is brought to you by Continuum Analytics.
Please check out: http://continuum.io/thanks and https://anaconda.org
```

You should see that it is using the Anaconda version. If not, that means you are using the default Python on your system. You need to look at the documentation for Anaconda and figure out why you are not running the appropriate Python. (Most likely something is wrong with your `PATH` environment variable.) That's okay for now.

Now, from the Python prompt `>>>` (we are no longer in `bash`), type `500+1` followed by newline. You should see something like this:

```python
>>> 500+1
501
>>> 
```

Python has evaluated the expression and printed the result back to the screen. It is as if we had used a `print` statement, which gives us the same result:

```python
>>> print 500+1
501
>>> 
```

The Python interactive shell prints expression values immediately, but that is not the case when running a program as a script (i.e., not interactively).
 
## Scripting Python

Go to a suitable directory on your disk, or create one, such as `/Users/YOURID/msan501/inclass`. **Do not use space it is in any of your directory or filenames...ever!** Now create a **text file** called `hello.py` that contains exactly one line:

```python
500+1
```

This is exactly what you typed in first in the interactive Python shell. Save the file in the `inclass` directory.

Here are solutions to  the most common errors:

1. Do not put `.txt` at the end of the file name
2. Do NOT use M$ Word or any other word processor; You think it's text but it's not. There are lots of text editors out there including Mac's `TextEdit.app`. Just make sure save as plain text not "rich text". There are also plenty of text editor such as [Sublime](https://www.sublimetext.com/) and [TextMate](https://macromates.com/).  (If you are really hard-core, you will learn `vi` or `emacs`, which you will see me use in class.) You can also use `nano` from the command line for editing.

Once you get the file written to the disk, you should be able to jump to that directory using the commandline shell. Use `ls` to get a directory listing:

```bash
$ cd /Users/YOURID/msan501/inclass
$ ls
hello.py
```

Now, we're going to run that program/script:

```bash
$ python hello.py
$ 
```

We do not get any output. This is a critical difference. The interactive Python shell immediately prints expression values because it is interactive. When you run a file from the commandline, it assumes you wanted to execute the code like a script in batch mode. That is why we do not get any output.

Now edit that file and change it to

```python
print 500+1
```

Save the file and rerun it. Now you should see:

```bash
$ python hello.py 
501
$ 
```

## PyCharm

Now, we're going to do the exact same thing except using the development environment PyCharm.

1. Launch PyCharm and then under `File` menu, tell it to open a directory with `Open...` menu item. 
2. Navigate to your `/Users/YOURID/msan501/inclass` directory and click okay. You should see your `hello.py` in the `Project` pane of the development environment. 
3. Double-click on it to open it in the editor pane.
4. Right click in the editor window and select `Run hello` item. Another pane will open on the bottom of the IDE that looks something like:

<img src=images/pycharm.png width=400>

Notice the `501` output in the console below the program text.

**You should be able to test out small programs or Python snippets very very quickly. Rehearse these procedures until they are second nature.**