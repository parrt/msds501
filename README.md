MSAN501 Computational Analytics Bootcamp
=======

This 5-week computational analytics bootcamp is part of the [MS in Analytics program at the University of San Francisco](http://analytics.usfca.edu) and is specifically designed as an introduction to analytics programming for those who are not yet skilled programmers.

# Administrivia

**INSTRUCTOR.** [Terence Parr](http://parrt.cs.usfca.edu). I’m a professor in the computer science department and was founding director of the MS in Analytics program at USF.  Please call me Terence or Professor (the use of “Terry” is a capital offense).

**SPATIAL COORDINATES:**<br>

* Class is held at 101 Howard in 5th floor classroom 529.
* Quizzes are held on first floor, 152/154; Last four fridays 9:15-10am (no quiz July 14th). Both sections meet together Friday mornings. After taking the quiz, wander upstairs to 529 if your section meets Friday mornings at 10.
* My office is room 608 (which I share with Prof. John Veitch).

**TEMPORAL COORDINATES.** Thursday/Friday Sec01 10am-12pm, Sec02 1-3pm; July 13 (Thu) - August 11 (Fri). *One exception: Thur 20th class moved to Tue 18th.*

**INSTRUCTION FORMAT**. Class runs for 2 hours, 2 days per week. Instructor-student interaction during lecture is encouraged and we'll mix in mini-exercises / labs during class. All programming will be done in the Python 2 programming language, unless otherwise specified.

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
|[Image processing](https://github.com/parrt/msan501/raw/master/projects/images.pdf)| 10%| Thur, July 27 |
| [Word similarity and relationships](https://github.com/parrt/msan501/blob/master/projects/wordsim.md) | 10%| Thur, August 3 |
| [Predicting Murder Rates With Gradient Descent](https://github.com/parrt/msan501/raw/master/projects/regression-gradient-descent.pdf)| 8%| Thur, August 10 |
|Quiz 0| 0% | 9:15am Thur, July 13 |
|Quiz 1| 18%| 9:15am Fri, July 21 |
|Quiz 2| 18%| 9:15am Fri, July 28 |
|Quiz 3| 18%| 9:15am Fri, August 4 |
|Quiz 4| 18%| 9:15am Fri, August 11 |

All projects will be graded with the specific input or tests given in the project description, so you understand precisely what is expected of your program. Consequently, projects will be graded in binary fashion: They either work or they do not.  The only exception is when your program does not run on the grader's or my machine because of some cross-platform issue. This is typically because a student has hardcoded some filename into their program. In that case, we will take off just 20% instead of giving you a 0.

Each project has a hard deadline and only those projects working correctly before the deadline get credit (100%).  My grading script pulls from github at the deadline.  On the due date, projects are due at the **start** of your section's class period for that day.

This class is pass/fail and we expect most people to pass, but those getting below 80% raw average score are in the danger zone.

# Syllabus

Start your engines!

* [A bit of motivation (Audio processing)](notes/sound.ipynb) (Day 1)
  * [A first taste of Python tools](labs/hello.md) (Day 1)
  * [Playing sounds](labs/sound.md) (Day 1)

Learning to design programs

* [Introduction to programming](notes/programming.md) (Day 2)
* [Representing data in memory](notes/data-in-memory.md) (Day 2)
* [Common programming operations](notes/operations.md) (Day 2)
* [Program planning](notes/planning.md) (Day 3)
* [Functions](notes/functions.md) (Day 3)
* [Introduction to Python coding](notes/coding.ipynb) (Students should review if needed)
* [Model of Computation](notes/computation.md) (Day 4)

Common programming tools

* [Bash your way to victory](notes/bash-intro.md)
* [Introduction to git and revision control](notes/git.md) (Day 2)

Implementing program work plans (actual coding)

* [Programming Patterns in Python](notes/python-patterns.ipynb) (Day 5)
* [Organizing your code with functions](notes/coding-functions.ipynb) (Day 6)
* [How to read code](notes/reading-code.md)

Key programming patterns

* [Loading files](notes/files.ipynb) (Day 6, 7)
* [Manipulating and Visualizing Data](notes/data.ipynb) (Day 8,9)
* [Extracting information from text](notes/text.ipynb) (Day 9)

Iterative methods for computation and optimization

* [Generating Uniform Random Numbers](notes/random-uniform.ipynb) (Day 7)
* [Approximating square root](notes/sqrt.ipynb) (Day 7)
* [Iterative Optimization Via Gradient Descent](notes/gradient-descent.pdf) (pdf) (Day 7,8)
