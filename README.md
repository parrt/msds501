MSAN501 Computational Data Science Bootcamp
=======

This 6-week computational bootcamp is part of the [MS in Data Science (formerly MS Analytics) program at the University of San Francisco](https://www.usfca.edu/arts-sciences/graduate-programs/data-science) and is specifically designed as an introduction to data science programming for those who are not yet skilled programmers.

# Administrivia

**INSTRUCTOR.** [Terence Parr](http://parrt.cs.usfca.edu). I’m a professor in the computer science department and was founding director of the MS in Data Science program at USF.  Please call me Terence or Professor (the use of “Terry” is a capital offense).

**TA.** Prince Grover (class of 2018) `pgrover3` at usfca.edu. Or, see him on slack.

**SPATIAL COORDINATES:**<br>

* Class is held at 101 Howard on main floor classroom 155/156 (both sections).
* Quizzes are held on Tuesdays on first floor, 9:25 - 9:55. Both sections meet together Tuesday mornings for this. After taking the quiz, sec02 wanders off but sec01 stays in 155/156 for class.
* My office is room 607 up on the mezzanine above the agora open area.

**TEMPORAL COORDINATES.** Monday/Tuesday Sec01 10am-11:50pm, Sec02 1:10-3pm; July 9 (Mon) - August 7 (Tue).

*Please attend your assigned section to keep the classes balanced!*

**INSTRUCTION FORMAT**. Class runs for 1:50 hours, 2 days per week. Instructor-student interaction during lecture is encouraged and we'll mix in mini-exercises / labs during class. All programming will be done in the Python 3 programming language, unless otherwise specified.

**COMMUNICATION**. Please join slack channel `#msan501`. Email or coming by my office are also ok.

**TARDINESS.** Please be on time for class. It is a big distraction if you come in late.

**LAPTOP POLICY.** My policy is that all student laptops must be closed during class unless we are doing a lab or I specifically ask you to follow along as I type into my computer. All materials for the course are available in this repository, which reduces your need to take notes considerably.

**ACADEMIC HONESTY.** You must abide by the copyright laws of the United States and academic honesty policies of USF. You may not copy code from other current or previous students. All suspicious activity will be investigated and, if warranted, passed to the Dean of Sciences for action.  Copying answers or code from other students or sources during a quiz, exam, or for a project is a violation of the university’s honor code and will be treated as such. Plagiarism consists of copying material from any source and passing off that material as your own original work. Plagiarism is plagiarism: it does not matter if the source being copied is on the Internet, from a book or textbook, or from quizzes or problem sets written up by other students. Giving code or showing code to another student is also considered a violation.

The golden rule: **You must never represent another person’s work as your own.**

If you ever have questions about what constitutes plagiarism, cheating, or academic dishonesty in my course, please feel free to ask me.

**Note:** Leaving your laptop unattended is a common means for another student to take your work. It is your responsibility to guard your work. Do not leave your printouts laying around or in the trash. *All persons with common code are likely to be considered at fault.*

**ON DISABILITIES.** If you are a student with a disability or disabling condition, or if you think you may have a disability, please contact USF Student Disability Services (SDS) at 415/422-2613 within the first week of class, or immediately upon onset of the disability, to speak with a disability specialist. If you are determined eligible for reasonable accommodations, please meet with your disability specialist so they can arrange to have your accommodation letter sent to me, and we will discuss your needs for this course. For more information, please visit http://www.usfca.edu/sds/ or call 415/422-2613.

## Student evaluation

| Artifact | Grade Weight | Due date |
|--------|--------|--------|
|[Image processing](https://github.com/parrt/msan501/blob/master/projects/images.md)| 12%| Mon, July 23 |
| [Word similarity and relationships](https://github.com/parrt/msan501/blob/master/projects/wordsim.md) | 12%| Mon, July 30 |
| [Predicting Death Rates With Gradient Descent](https://rawgit.com/parrt/msan501/master/projects/regression/index.html)| 12%| Mon, August 6 |
|[Quiz 0](https://usfca.instructure.com/courses/1578156/quizzes/2327034)| 0%| Before Mon, July 9|
|Quiz 1| 16%| 9:25am Tue, July 17 |
|Quiz 2| 16%| 9:25am Tue, July 24 |
|Quiz 3| 16%| 9:25am Tue, August 31 |
|Quiz 4| 16%| 9:25am Tue, August 7 |

**Quizzes** 1-4 are held in rooms 154-156. All quizzes use [LockDown Browser](https://www.respondus.com/lockdown/download.php?id=953641626) to log into Canvas so you can take the quiz.  Quizzes have strict time limits and you will be unable to do anything other than take the quiz; no access to the Internet etc.  You will have one chance to answer each question and they will appear in random order. Students should read the [Student LockDown Browser Instructions](https://myusf.usfca.edu/sites/default/files/ets-Respondus.pdf) section. In a nutshell, download the [LockDown Browser](https://www.respondus.com/lockdown/download.php?id=953641626), install it, and when you launch it it will take your browser window to Canvas for login.

All projects will be graded with the specific input or tests given in the project description, so you understand precisely what is expected of your program. Consequently, projects will be graded in binary fashion: They either work or they do not.  The only exception is when your program does not run on the grader's or my machine because of some cross-platform issue. This is typically because a student has hardcoded some file name or directory into their program. In that case, we will take off just 20% instead of giving you a 0. Please go to github and verify that the website has the proper files for your solution. That is what I will download for testing.

Each project has a hard deadline and only those projects working correctly before the deadline get credit (100%).  My grading script pulls from github at the deadline.  On the due date, projects are due at the **start** of your section's class period for that day.

**Grading standards.** This class is a standard, graded course with letter grades A - F. I consider an A grade to be above and beyond what most students have achieved. A B grade is an average grade for a student or what you could call "competence" in a business setting. A C grade means that you either did not or could not put forth the effort to achieve competence. Below C implies you did very little work or had great difficulty with the class compared to other students.

# Syllabus

Writing software is about problem solving, computer languages, algorithms, data structures, libraries, tools, and computing devices.  In this boot camp, I'm hoping to teach you how to approach programming, review the key elements of Python, teach you some of the core libraries, give you an introduction to the command line, and finally introduce you to cloud computing. You will go over algorithms and data structures in more detail in the machine learning courses as well as the problem-solving course Spring semester.

Start your engines!

* [A bit of motivation (Audio processing)](notes/sound.ipynb) (Day 1)
  * [A first taste of Python tools](labs/hello.md) (Day 1)
  * [Playing sounds](labs/sound.md) (Day 1)

Designing and building programs

* [Introduction to programming](notes/programming.md) (Day 1 (before conjuring code), 2)
* [Representing data in memory](notes/data-in-memory.ipynb) (Day 2 (before `dict`), 3)
* [Model of Computation](notes/computation.ipynb) (Day 3)
* [Programming Patterns in Python](notes/python-patterns.ipynb) (Day ?)
* [Data aliasing](notes/aliasing.ipynb) (Day ?)
* [Organizing your code with functions](notes/functions.ipynb) (Day ?)
* [How to read code](notes/reading-code.md) (Day ?)

Common programming tools

* [Bash your way to victory](notes/bash-intro.md) (Day ?)
* [Introduction to git and revision control](notes/git.md) (Day 2)
* [Launching a Virtual Machine at Amazon Web Services](notes/aws.md) (Day ?)

Key programming patterns

* [Loading files](notes/files.ipynb) (Day ?)
* [Manipulating and Visualizing Data](notes/data.ipynb) (Day ?)

Iterative methods for computation and optimization

* [Generating Uniform Random Numbers](notes/random-uniform.ipynb) (Day ?)
* [Approximating square root](notes/sqrt.ipynb) (Day ?)
* [Iterative Optimization Via Gradient Descent](notes/gradient-descent.pdf) (pdf) (Day ?)

Optional

* [Linked lists](notes/linked-list.ipynb) (Day ?)
