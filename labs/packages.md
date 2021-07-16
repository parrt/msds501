# Packages and modules lab

The goal of this lab is to get familiar importing existing packages/modules and to create and import your own modules.

**You should retype these exercises rather than cutting/pasting, which doesn't help you remember anything.**

## Importing standard packages

By now, you've probably seen lots of examples and have used `import` many times for various projects. Just for completeness, let's go through the basics.
 
In a file called `basics.py` import the `math`, `numpy`, and `pandas` packages with the following.

```python
import math
import numpy as np
import pandas as pd
```

Please note the standard aliases given for the second two packages; this is what you will see in all code examples and it's good to keep to the standard. The `as np` is an alias that we can use as a shorthand.

Let's verify that the import statements have worked:

```python
print(math.pi)
print(np.sum(np.array([1,2,3])))

df = pd.DataFrame([[100,'parrt'],[105,'tombu']],
                  columns=['ID','user'])
print(df)
```

The output you get should look like this:
 
```
$ python basics.py 
3.141592653589793
6
    ID   user
0  100  parrt
1  105  tombu
```

Now, let's try out a variation on the import statement that imports a single variable instead of all variables. It allows us to directly reference `pi` instead of the package name prefix `math.pi`. In the same file or different file, execute this:

```python
from math import pi
print(pi)
```

## Importing our own module

To learn more about how modules work, let's create our own module. The good news is it's just another Python file. If we import it into another file it acts like a module rather than a script that we execute. As a general rule, modules that you import should not have a main program (code outside of functions). The only exception is when you need to create a variable that you want to be available to the file importing your module.

Create a file called `mymath.py` that will hold a variable and function definition mimicking standard math stuff:

```python
pi = 3.14159

def pow2(n):
    v = 1
    for i in range(n):
        v *= 2
    return v
```

Now, create a script called `usemymath.py` that will import that code and test it:

```python
from mymath import *

print(pi)
print(pow2(0))
print(pow2(10))
```

From the command line the output looks like this:
 
```bash
$ python usemymath.py 
3.14159
1
1024
```
   
The whole point of this exercise is to learn that organizing related functions into modules that you can reuse makes you more productive. You can even publish these packages so that other people can use your code.

If you get stuck, you can check out the [solution](https://github.com/parrt/msds501/tree/master/labs/code/packages).