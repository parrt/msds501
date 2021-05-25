# Exploration of Enron email data set

The goal of this project is to learn how to collect, filter, aggregate, explore, and visualize data from a large collection of files. You will also learn how to use the really nice [networkx](https://networkx.org) network analysis library. Our data set is a well-known collection of emails sent and received within an energy company called Enron that was collected by the FBI as part of a massive fraud investigation. According to an [FBI retrospective](https://www.fbi.gov/history/famous-cases/enron), "*The Enron Task Force’s efforts resulted in the convictions of nearly all of Enron’s executive management team*" and goes on to say:

> Top officials at the Houston-based company cheated investors and enriched themselves through complex accounting gimmicks like overvaluing assets to boost cash flow and earnings statements, which made the company even more appealing to investors. When the company declared bankruptcy in December 2001, investors lost millions

This is purely an exercise but it's interesting to see how with a small bit of effort we can identify some unusual email behavior that could indicate inappropriate activity. For example, [Fortune magazine](https://archive.fortune.com/magazines/fortune/fortune_archive/2005/03/07/8253428/index.htm) reports that "*the former head of Enron's trading operations, John Lavorato, [...] sold all his Enron stock in spring 2001 at about \$63 per share. (It was worth pennies by December.)*" Now, take a look at the histogram depicting the email activity sent by Lavorato.  About the time he knew they were going to be busted, he all of a sudden stops communicating over email, at least his work email, which is weird for a top executive. He must have started using a private channel to hide communications with co-conspirators.

<img src="figures/lavorato.png" width="70%">

You have two primary tasks:

1. Load 1.5G worth of email messages and construct a tidy data frame that is much easier to process than the raw data (takes about 3 minutes); you will save this in [feather format](https://pypi.org/project/pyarrow) so that it can be loaded extremely quickly; here's a sample:<br><img src="figures/enron-df.png" width="100%">
2. Create a jupyter notebook that loads the data frame created in the previous step and then generates tables and visualizations as part of an exploration. (Details below.)

Your projects will be graded via a series of unit tests operating on the data frame you create and my evaluation will examine a PDF that you generate and submit from your notebook.

Unlike your previous projects, you will be programming from a blank screen, without a template. As part of your education, you have to learn to start from scratch. Rather than requiring a specific set of methods, unit tests will examine the data frame you save and feather format.  To make it easier for me to grade your notebooks, however, I am providing a standard set of sections you should fill in with code and visualizations.

## Process 1.5G of Enron email

Your first goal is to create a condensed version of the enron email messages in the form of a data frame and then save that in feather format. The email is stored in a series of subdirectories organized by person and by mail folders, where the individual messages are numbered as you can see here:

<img src="figures/maildir.png" width="35%">

Begin by downloading the very large (1.7G) [Enron data set](https://www.cs.cmu.edu/~./enron/enron_mail_20150507.tar.gz) and untar/unzip it. You will find a `maildir`, which contains the email messages organized by user. **Please do not try to add/commit your mail directory or the `.tar.gz` file to your repository!**

Create a Python script in the root of your repository called `condense.py` that accepts the mail directory as a commandline argument so that you will run your program like this:

`python condense.py` *path-to-maildir*

where *path-to-maildir* indicates the exact path of your mail directory. This allows us to place the mail directory anywhere on the disk and still use the same script. The execution of your finished script takes about two or three minutes depending on the speed of your machine. After execution, your script should leave file `enron.feather` in the current directory. The columns of the data frame must be in order exactly: `MailID`, `Date`, `From`, `To`, `Recipients`, `Subject`, `filename`:

<img src="figures/enron-df.png" width="100%">

`Recipients` indicates the number of people on the `To:` line for a single email message and `filename` is the subdirectory of `maildir` that contains the mail message.

### Getting started by sniffing the data

At the beginning of a project, we know very little about how to proceed or what to do, so we have to explore. A great way to start is by looking at the data we have. Here's a simple email message with all of the email headers as a prefix:

<img src="figures/email1.png" width="60%">

The grayed out stuff is what we can ignore in order to build the data frame. The orange is the data we need to extract and the black text is the set of sentinels we must look for to extract the data. This is more or less easy to extract because everything is on a line by itself with clear line prefixes. Unfortunately, sometimes there's a long `To:` list and the email recipient list spans multiple lines so you will have to deal with that as well:

<img src="figures/email2.png" width="55%">

We'll also ignore the `CC:` and `BCC:` lines.  The `X-From:` etc... lines should be ignored for our purposes. All we need can be derived from the four headers  highlighted in orange.

Many of the email messages should be ignored. There are messages that have no `To:` line, which we can discard.  Ignore and sender and recipient email addresses, such as `tradersnewsindexes@ipgdirect.com`, `pep <performance.>`, and `dbaughman@houston.rr.com`.  Naturally, ignore any email message that has empty sender or recipient values after filtering.  Some addresses are from Enron but are weird and we should filter them out:

* `/o=enron/ou=eu/cn=recipients/cn=jtaylo3...@enron.com`
* `#32@enron.com`
* `legal<.hall@enron.com>`
* `e-mail<.bo@enron.com>`

Normalize the email addresses by getting rid of single quotes and delete any `.` (dot) at the start of an email address:
 
* `'.''bill@enron.com` &rightarrow; `bill@enron.com`
* `'arnold@enron.com` &rightarrow; `arnold@enron.com`
* `'.'delaney@enron.com` &rightarrow; `delaney@enron.com`


### Building the script

My approach to this problem was to simply write code that I knew I was going to throw away, in order to explore the email messages and the structure of the data. That's how I figured out what we should ignore and what we should filter and normalize. I ended up with a big junk drawer of code with all sorts of commented out sections from previous experiments. Once I built something that worked properly, I reorganized it into multiple methods that made it much easier to understand and simpler to debug.  This is an important step when you're developing code commercially because someone, possibly you, must maintain this code in the future. The better structured it is the easier it will be to maintain. Always be good to your future self. To get an idea of the structure before and after, consider the following to blurred code outlines.

<img src="figures/condense.png" width="10%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="figures/condense-refactored.png" width="10%">

My structured code is organized well. For example, my main program (at the bottom) consists of code to essentially process all of the email into a data frame and then save it. Processing all of the email means getting a list of all message files and then loading those files one by one. As I load, I filter and normalize the information into a list of records (tuples). My primary method then converts that to a data frame and returns it to the main program, which saves it and feather format. I also have a method to extract the relevant bits from an email message and a method to normalize an email address.

You can structure your code anyway you want, but it must save the `enron.feather` file in the current working directory. That way my `test_enron.py` tests will find the data file. 

## Exploring email traffic

## Exploring email connection graph

<img src="figures/skill ing-k1.png" width="50%">


## Deliverables

In your repository, you should submit file 

## Evaluation

I will execute your `condense.py` script from the command line with an argument indicating where I have my `maildir` directory. For example, I probably will executed like this:

```python
$ python condense.py ~/data/maildir
...
```

**Execution time of condense.py to create enron.feather must be under 3.5 minutes on my machine to get credit for the project.**  It must also leave the `enron.feather` file in the current directory so that the unit tests know how to find the file.

I will test the contents of `enron.feather` using the [test_enron.py]() test rig:

```bash
$ python -m pytest -v test_enron.py
================================= test session starts =================================
platform darwin -- Python 3.8.8, pytest-6.2.3, py-1.10.0, pluggy-0.13.1 -- /Users/parrt/opt/anaconda3/bin/python
cachedir: .pytest_cache
rootdir: /Users/parrt/courses/msds501-private/projects/enron
plugins: anyio-2.2.0
collected 6 items                                                                     

test_enron.py::test_overall_stats PASSED                                        [ 16%]
test_enron.py::test_addrs PASSED                                                [ 33%]
test_enron.py::test_lavorato_filenames PASSED                                   [ 50%]
test_enron.py::test_kay_mann PASSED                                             [ 66%]
test_enron.py::test_tim_johanson PASSED                                         [ 83%]
test_enron.py::test_ken_lay_senders PASSED                                      [100%]

================================= 6 passed in 15.05s ==================================
```
