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

    Ignore weird email addresses like:

    If missing a "To:" line, ignore email


### Building the script

My approach to this problem was to simply write code that I knew I was going to throw away, in order to explore the email messages and the structure of the data.

    
<img src="figures/condense.png" width="10%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="figures/condense-refactored.png" width="10%">

## Exploring email traffic

## Exploring email connection graph

<img src="figures/skill ing-k1.png" width="50%">


## Deliverables

In your repository, you should submit file 

## Evaluation

We will run [test_wordsim.py](https://github.com/parrt/msds501/blob/master/projects/test_wordsim.py) from the command line as follows using the  vectors (where I have placed my datafiles in directory `~/data`):

```bash
$ python -m pytest -v test_wordsim.py ~/data
...
```

**That test rig must run in under 40 seconds on my machine to get credit for the project.**