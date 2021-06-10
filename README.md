# MSDS501 Computational Data Science Bootcamp

This 5-week computational bootcamp is part of the [MS in Data Science program at the University of San Francisco](https://www.usfca.edu/arts-sciences/graduate-programs/data-science) and is specifically designed as an introduction to data science programming for those who are not yet skilled programmers.

Writing software is about problem solving, computer languages, algorithms, data structures, libraries, tools, and computing devices.  In this boot camp, I'm hoping to teach you how to approach programming, review the key elements of Python, teach you some of the core libraries, give you an introduction to the command line, and finally introduce you to cloud computing. You will go over algorithms and data structures in more detail in the machine learning courses as well as the problem-solving course Spring semester.

# Class details

**INSTRUCTOR.** [Terence Parr](http://parrt.cs.usfca.edu). I’m a professor in the computer science and [data science program](https://www.usfca.edu/arts-sciences/graduate-programs/data-science) departments and was founding director of the MS in Analytics program at USF (which became the MS data science program).  Please call me Terence or Professor (“Terry” is not ok).

**SPATIAL COORDINATES:**<br>

* Class is held at 101 Howard in 1st floor classroom 155-156.
* Exams are held in 154-156. Both sections meet together.
* My office is room 607 @ 101 Howard up on mezzanine above the open area on 5th floor

**TEMPORAL COORDINATES.** Wed July 7 to Wed Aug 11.

* Lectures: Mon/Wed 10AM - 11:50AM

<!--
* Exams: Fri 5-6PM Nov 8; Fri 10-11:30AM Dec 6; Room 154-156
-->

**INSTRUCTION FORMAT**. Class runs for 1:50 hours, 2 days/week. Instructor-student interaction during lecture is encouraged and we'll mix in mini-exercises / labs during class. All programming will be done in the Python 3 programming language, unless otherwise specified.

**TARDINESS.** Please be on time for class. It is a big distraction if you come in late.

**LAPTOP POLICY.** My policy is that all student laptops must be closed during class unless we are doing a lab or I specifically ask you to follow along as I type into my computer. All materials for the course are available in this repository, which reduces your need to take notes considerably.

## Student evaluation

| Artifact | Grade Weight | Due date |
|--------|--------|--------|
|[Github/USF survey](https://usfca.instructure.com/courses/1600702/assignments/7086080)| 0%| July 7 |
|[Image processing](https://github.com/parrt/msan501/blob/master/projects/images.md)| 15%| Mon, July 21 |
| [Word similarity and relationships](https://github.com/parrt/msds501/blob/master/projects/wordsim.md) | 10%| Mon, July 28 |
| [Exploration of Enron email data set](https://github.com/parrt/msds501/blob/master/projects/enron.md)| 15%| Mon, August 13 |
|Quiz 1| 16%| 9:15am Wed, July 14 |
|Quiz 2| 16%| 9:15am Mon, July 26 |
|Quiz 3| 16%| 9:15am Mon, August 2 |
|Quiz 4| 16%| 9:15am Mon, August 11 (last day of class) | 

**Quizzes** 1-4 are held in rooms 154-156. All quizzes use HonorLock to log into Canvas so you can take the quiz.  Quizzes have strict time limits and you will be unable to do anything other than take the quiz; no access to the Internet etc.  You will have one chance to answer each question. 

All projects will be graded with the specific input or tests given in the project description, so you understand precisely what is expected of your program. Consequently, projects will be graded in binary fashion: They either work or they do not.  The only exception is when your program does not run on the grader's or my machine because of some cross-platform issue. This is typically because a student has hardcoded some file name or directory into their program. In that case, we will take off just 20% instead of giving you a 0. Please go to github and verify that the website has the proper files for your solution. That is what I will download for testing.

Each project has a hard deadline and only those projects working correctly before the deadline get credit (100%).  My grading script pulls from github at the deadline.  On the due date, projects are due at the **start** of your section's class period for that day.

**No partial credit**. Students are sometimes frustrated about not getting partial credit for solutions they labored on that do not actually work. Unfortunately, "almost working" just never counts in a job situation because nonfunctional solutions have no value.  We are not writing essays in English that have some value even if they are not superb.  When it comes to software, there is no fair way to assign such partial credit, other than a generic 30% or whatever for effort.  The only way to determine what is wrong with your project is for me to fix and/or complete the project. That is just not possible for 90 students. Even if that were possible, there is no way to fairly assign partial credit between students.  A few incorrect but critical characters can mean the difference between perfection and absolute failure. If it takes a student 20 hours to find that problem, is that worth more or less partial credit than another project that is half-complete but could be finished in five hours? To compensate, I try to test multiple pieces of the functionality in an effort to approximate partial credit.

Each project has a hard deadline and only those projects working correctly before the deadline get credit.  My grading script pulls from github at the deadline.  *All projects are due at the start of class on the day indicated, unless otherwise specified.*

*I reserve the right to change projects until the day they are assigned.*

**Grading standards**. I consider an **A** grade to be above and beyond what most students have achieved. A **B** grade is an average grade for a student or what you could call "competence" in a business setting. A **C** grade means that you either did not or could not put forth the effort to achieve competence. Below **C** implies you did very little work or had great difficulty with the class compared to other students.

# Syllabus

## Designing and building programs

* [Overview of a Python programmer's world](slides/) (Day 1)
* [Intro to Python programming](slides/) (Day 1)
* [Programming patterns](slides/) (Day 1)
* [packages / modules]()
* [Organizing your code with functions]()
* [key data structures]()
* [aliasing]()
* [files]()
* [problem-solving]() (data / files processing)
* [how to read code]()
* [OO]()

## Programming ecosystem

* [command-line]() (Day 2)
* [git and github]() (Day 2)
* [AWS]()

### OLD
Start your engines!

* [A bit of motivation (Audio processing)](notes/sound.ipynb) (Day 1)
  * [A first taste of Python tools](labs/hello.md) (Day 1)
  * [Playing sounds](labs/sound.md) (Day 1)

Designing and building programs

* [Introduction to programming](notes/programming.md) (Day 1 (before conjuring code), 2)
* [Representing data in memory](notes/data-in-memory.ipynb) (Day 2 (before `dict`), 3)
* [Model of Computation](notes/computation.ipynb) (Day 3)
* [Programming Patterns in Python](notes/python-patterns.ipynb) (Day 4)
* [Data aliasing](notes/aliasing.ipynb) (Day 4)
* [Organizing your code with functions](notes/functions.ipynb) (Day 4 up to search function, Day 5)
* [How to read code](notes/reading-code.md) (Day 10)
* [Object-oriented programming](notes/OO.ipynb) (Day 9 up to Simple Set Impl)

Key programming patterns

* [Loading files](notes/files.ipynb) (Day 5 up to CSV, finish Day 6)
* [Pandas dataframes](notes/dataframes.ipynb) (Day 6 up to clean up, finish Day 7)
* ?? [Manipulating and Visualizing Data](notes/data.ipynb) (Day ?)

Iterative methods for computation and optimization

* [Generating Uniform Random Numbers](notes/random-uniform.ipynb) (Day 8)
* [Approximating square root](notes/sqrt.ipynb) (Day 8)
* [Iterative Optimization Via Gradient Descent](https://nbviewer.jupyter.org/github/parrt/msan501/blob/master/notes/gradient-descent.ipynb) (Day 8)

Common programming tools

* [Bash your way to victory](notes/bash-intro.md) (Day ?)
* [Introduction to git and revision control](notes/git.md) (Day 2)
* [Launching a Virtual Machine at Amazon Web Services](notes/aws.md) (Day 10)

Optional

* [Linked lists](notes/linked-list.ipynb) (Day ?)

  
# Administrivia

**ACADEMIC HONESTY.** You must abide by the copyright laws of the United States and academic honesty policies of USF. You may not copy code from other current or previous students. All suspicious activity will be investigated and, if warranted, passed to the Dean of Sciences for action.  Copying answers or code from other students or sources during a quiz, exam, or for a project is a violation of the university’s honor code and will be treated as such. Plagiarism consists of copying material from any source and passing off that material as your own original work. Plagiarism is plagiarism: it does not matter if the source being copied is on the Internet, from a book or textbook, or from quizzes or problem sets written up by other students. Giving code or showing code to another student is also considered a violation.

The golden rule: **You must never represent another person’s work as your own.**

If you ever have questions about what constitutes plagiarism, cheating, or academic dishonesty in my course, please feel free to ask me.

All students are expected to know and adhere to the University's <a href="https://usfca.edu/academic-integrity/">Honor Code</a>.

**Note:** Leaving your laptop unattended is a common means for another student to take your work. It is your responsibility to guard your work. Do not leave your printouts laying around or in the trash. *All persons with common code are likely to be considered at fault.*

**USF policies and legal declarations**

*Students with Disabilities*

If you are a student with a disability or disabling condition, or if you think you may have a disability, please contact <a href="https://www.usfca.edu/student-disability-services">USF Student Disability Services</a> (SDS) for information about accommodations.  Students should contact SDS at the beginning of the semester. **Accommodations are not retroactive.**

*Illnesses and Emergencies*

If you fall ill or have an emergency (personal or otherwise) that significantly affects your ability to complete a project or take an exam, you must notify the instructor before the task or artifact is due. Do not simply skip an exam or an assignment and say you were sick after the fact. Always make arrangements with the instructor beforehand, rather than declaring illness or emergency later. **Accommodations are not retroactive.**  Illness and emergency related situations must be disclosed to both the instructor and program director in writing. Illness-related issues must be accompanied by a doctor’s note.
  
*Behavioral Expectations*

All students are expected to behave in accordance with the <a href="https://usfca.edu/fogcutter">Student Conduct Code</a> and other University policies.

*Counseling and Psychological Services (CAPS)*

CAPS provides confidential, free <a href="https://usfca.edu/student-health-safety/caps">counseling</a> to student members of our community.

*Confidentiality, Mandatory Reporting, and Sexual Assault*

For information and resources regarding sexual misconduct or assault visit the <a href="https://myusf.usfca.edu/title-ix">Title IX</a> coordinator or USFs <a href="http://usfca.callistocampus.org" target="_blank">Callisto website</a>.

