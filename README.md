MSAN501 Computational Analytics Bootcamp
=======


This 5-week computational analytics bootcamp is part of the [MS in Analytics program at the University of San Francisco](http://analytics.usfca.edu) and is specifically designed as an introduction to analytics programming for those who are not yet skilled programmers.

# Administrivia

**INSTRUCTOR.** [Terence Parr](http://parrt.cs.usfca.edu). I’m a professor in the computer science department and was founding director of the MS in Analytics program at USF.  Please call me Terence or Professor (the use of “Terry” is a capital offense).

**SPATIAL COORDINATES.** 101 Howard 5th floor Rm527 or Rm529.

**TEMPORAL COORDINATES.** Monday 1-5pm, Tues 10-12pm; July 11 (Mon) - August 9 (Tue).

**INSTRUCTION FORMAT**. Class runs for 4 hours on Monday and then 2 hours on Tuesday. Instructor-student interaction during lecture is encouraged and we'll mix in mini-exercises / labs during class. All programming will be done in the Python programming language, unless otherwise specified.

**TARDINESS.** Please be on time for class. It is a big distraction if you come in late.

**ACADEMIC HONESTY.** You must abide by the copyright laws of the United States and academic honesty policies of USF. You may not copy code from other current or previous students. All suspicious activity will be investigated and, if warranted, passed to the Dean of Sciences for action.  Copying answers or code from other students or sources during a quiz, exam, or for a project is a violation of the university’s honor code and will be treated as such. Plagiarism consists of copying material from any source and passing off that material as your own original work. Plagiarism is plagiarism: it does not matter if the source being copied is on the Internet, from a book or textbook, or from quizzes or problem sets written up by other students. Giving code or showing code to another student is also considered a violation.

The golden rule: **You must never represent another person’s work as your own.**

If you ever have questions about what constitutes plagiarism, cheating, or academic dishonesty in my course, please feel free to ask me.

**Note:** Leaving your laptop unattended is a common means for another student to take your work. It is your responsibility to guard your work. Do not leave your printouts laying around or in the trash. *All persons with common code are likely to be considered at fault.*

**ON DISABILITIES.** If you are a student with a disability or disabling condition, or if you think you may have a disability, please contact USF Student Disability Services (SDS) at 415/422-2613 within the first week of class, or immediately upon onset of the disability, to speak with a disability specialist. If you are determined eligible for reasonable accommodations, please meet with your disability specialist so they can arrange to have your accommodation letter sent to me, and we will discuss your needs for this course. For more information, please visit http://www.usfca.edu/sds/ or call 415/422-2613.

## Student evaluation

| Artifact | Grade Weight | Due date |
|--------|--------|--------|
|[Image processing](https://github.com/parrt/msan501/raw/master/projects/images.pdf)| 12%| Sunday July 17, 2016 midnight |
| [Confidence Intervals for Price of Hostess Twinkies](https://github.com/parrt/msan501/raw/master/projects/conf.pdf) | 6%| Sunday July 24, 2016 midnight |
| [Is Free Beer Good For Tips?](https://github.com/parrt/msan501/raw/master/projects/hyp.pdf) | 7%| Sunday July 24, 2016 midnight |
| [Predicting Murder Rates With Gradient Descent](https://github.com/parrt/msan501/raw/master/projects/regression-gradient-descent.pdf)| 12%| Sunday July 31, 2016 midnight |
| [Search Engine Implementation](https://github.com/parrt/msan501/blob/master/projects/hashtable.md)| 12%| Sunday August 7, 2016 midnight |
|Quiz 1| 6%| Tuesday, July 12 |
|Quiz 2| 11%| Monday, July 18 |
|Quiz 3| 11%| Monday, July 25 |
|Quiz 4| 11%| Monday, August 1 |
|Quiz 5| 11%| Tuesday, August 9 |

All projects are graded in binary fashion: They either work or they do not. Each project has a hard deadline and only those projects working correctly before the deadline get credit (100%).  My grading script pulls from github at the deadline. If you miss the deadline, you can still get 80% for the project if you complete it correctly by end of last class period.

This class is pass/fail and we expect most people to pass, but those getting below 80% raw average score are in the danger zone.

# Syllabus

[Computer/lab/account setup](notes/setup.md)

## Introduction

* Administrivia
* [Lightning lab: Problem solving](lightning/think.pdf)
* [How computers work](notes/architecture.md)
* [The representation of data](notes/info.pdf)
 * unary, binary
 * ascii characters
 * images, audio ([audio plot](https://github.com/parrt/msan501/blob/master/notes/code/plotaiff.py), [audio scale](https://github.com/parrt/msan501/blob/master/notes/code/scaleaiff.py))
 * python atomic types

## Python at lightspeed

* ['Bash' your way to victory](notes/bash-intro.md)
* [Lightning lab: Say Hello](lightning/hello.md)
* [Simple statements and functions](notes/area.md)
* [Lists and loops with vectors](notes/vectors.md)
* [Objects versus primitive types](notes/ptrs.md)
* [Computing point stats](notes/stats.md)
* [Importing library code](notes/imports.md)
* [Importing your own code](notes/myimport.md)
* [Generating histograms](notes/hist.md)
* [Scatter plots and line fitting](notes/scatter.md)

Topics:

* Expressions; arithmetic, powers, roots, string `%`, string `in`
* Assignment to (global) variables
* Demo [Python tutor](http://www.pythontutor.com)
* Calling built-in functions
* Relational operators
* Conditional statements
* List comprehensions
* Command-line arguments
* Read input from stdin
* While loops
* For loops
* [Basic debugging of loops with PyCharm](notes/debugging.md); see [PyCharm doc](https://www.jetbrains.com/help/pycharm/2016.1/debugging.html)
* Functions
 * purpose, def
 * Generating Uniform Random Numbers
 * args, locals, use of globals
 * qualified calls; packages, objects
 * debugging of funcs with PyCharm
* Histograms using matplotlib
* Image processing (**project**)

### Resources

* [PyCharm](notes/pycharm.pdf)
* [Raw python notes](notes/python.md)
* You will need to [Git on it](notes/git.pdf) to submit your first project.

## Empirical statistics

* [Generating pseudorandom variables](notes/runif.md)
* [The Central limit theorem in action](notes/clt.pdf)
* Boostrapping, resampling
* Empirical Confidence Intervals
  * [Confidence Intervals for Price of Hostess Twinkies](https://github.com/parrt/msan501/raw/master/projects/conf.pdf) (**project**)
* Empirical p-values
  * [Is Free Beer Good For Tips?](https://github.com/parrt/msan501/raw/master/projects/hyp.pdf) (**project**)

## Basic I/O

* [Reading and writing files](notes/files.md)

## Optimization and Prediction

* [Approximating square root through iteration](notes/sqrt.md)
* [Using recursion to compute n factorial](notes/fact.md)
* [Iterative Optimization Via Gradient Descent](https://github.com/parrt/msan501/raw/master/notes/gradient-descent.pdf)
* [Predicting Murder Rates With Gradient Descent](https://github.com/parrt/msan501/raw/master/projects/regression-gradient-descent.pdf) (**project**)

## Use/Implementation of Data structures

* [Lists and tuples](notes/lists-tuples.md)
* [Matrix operations](notes/matrix.md)
* [Sets](notes/sets.md)
* [Linked Lists](notes/linked-lists.md)
* [Dictionaries](notes/dictionaries.md)
* [Search Engine Implementation](https://github.com/parrt/msan501/blob/master/projects/hashtable.md) (**project**)

## Running remote programs

* [Launching a Virtual Machine at Amazon Web Services](labs/aws.md)
* [S3 storage at AWS](labs/s3.md)
* [Linux command line (`bash`)](labs/bash.md)