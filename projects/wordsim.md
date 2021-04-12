# Word similarity and relationships

## Goal

In this project, you will leverage an important advance in natural language processing called [word2vec](http://arxiv.org/pdf/1301.3781.pdf) (or just *word vectors* / *word embeddings*) to study the similarity between words. In particular, we're going to use a "database" from [Stanford's GloVe project](https://nlp.stanford.edu/projects/glove/).  For example, given a single word, we can find the *n* closest words, at least according to the corpus from which the word vectors were derived:

```
Enter a word or 'x:y as z:'
> dog
dog is similar to {dogs puppy pet cat pup}
> cow
cow is similar to {pig sheep goat cattle bull}
> united
united is similar to {kingdom america country britain us}
> chinese
chinese is similar to {korean china vietnamese japanese thai}
> alien
alien is similar to {extraterrestrial spaceship evil planet creature}
> approach
approach is similar to {methodology understanding strategy rather perspective}
```

Given three words, we can also use word vectors to fill in the blank of partial analogies of the form "*x is to y as z is to _____*":

```
Enter a word or 'x:y as z:'
> king:queen as man:
king is to queen as man is to {woman girl lady wonder guy}
> apple:tree as seed:
apple is to tree as seed is to {tree leaf planting plant seedling}
> hammer:nail as comb: 
hammer is to nail as comb is to {nail manicure hair cuticle brush}
> dog:puppy as cat:
dog is to puppy as cat is to {kitten puppy pup kitty pug}
> like:love as dislike:
like is to love as dislike is to {love adore hate liking loathe}
```

Your goal is to implement a simple interactive program that repeatedly accepts either a word or a partial analogy in the form `x:y as z:` for 3 words x, y, and z. I provide the main program for you that actually queries words or analogies from the user and then calls a set of functions you must implement.

## Description

Imagine trying to compare two documents for similarity. One document might be about "Installing Windows software" and another one might be about "Deinstalling Microsoft programs."  Because there are no words in common, at least for these titles, it's hard for a computer to tell these titles are related. A human, on the other hand, can easily equate Windows with Microsoft and software with programs etc., thus, finding the titles similar.

Until 2013, software could really only compare two words for exact match or a so-called *edit distance* (how many character edits to go from one word to the other). With word vector, we have a model for the "meaning" of a word in the form of a big vector of floats (usually 50 to 300 dimensional). These vectors are derived from a neural network that learns to map a word to an output vector such that neighboring words in some large corpus are close in 300-space. ("*The main intuition underlying the model is the simple observation that ratios of word-word co-occurrence probabilities have the potential for encoding some form of meaning.*" see [GloVe project](https://nlp.stanford.edu/projects/glove/)) For example, given the words ['petal','love','king', 'cat'], here is a two-dimensional projection of the vectors for those words and the 3 nearest to those words (there is some overlap):

<img src="figures/wordvec1.png" width=400>

The amazing thing about these vectors is that somehow they really encode the relationship between words. From the original paper, which you can also verify with this project code, the vector arithmetic `king - man + woman` is extremely close to the vector for `queen`!  The GloVe project at Stanford has a nice example showing the vector difference between various words:

<img src="https://nlp.stanford.edu/projects/glove/images/man_woman.jpg" width=400>

A good place to start this project is look at the provided main program as it identifies the key sequence of operations.

### Main program

To provide a little commandline interpreter where users can type in words or partial analogies, you will use this main program:
 
```python
if __name__ == '__main__':
    glove_dirname = sys.argv[1]
    gloves = load_glove(glove_dirname)

    plot_words(gloves,['petal','love','king', 'cat'], 3)

    print("Enter a word or 'x:y as z:' (type 'exit' to quit)")
    cmd = ''
    while cmd!=None:
        cmd = input("> ")
        if cmd.strip()=='exit':
            break
        match = re.search(r'(\w+):(\w+) as (\w+):', cmd)
        if match is not None and len(match.groups())==3:
            x = match.group(1).lower()
            y = match.group(2).lower()
            z = match.group(3).lower()
            if x not in gloves:
                print(f"{x} is not a word that I know")
                continue
            if y not in gloves:
                print(f"{y} is not a word that I know")
                continue
            if z not in gloves:
                print(f"{z} is not a word that I know")
                continue
            words = analogies(gloves, x, y, z, 5)
            print("%s is to %s as %s is to {%s}" % (x,y,z,' '.join(words)))
        elif re.match(r'\w+', cmd) is not None:
            if cmd not in gloves:
                print(f"{cmd} is not a word that I know")
                continue
            words = closest_words(gloves, cmd.lower(), 5)
            print("%s is similar to {%s}" % (cmd,' '.join(words)))
        else:
            print("Enter a word or 'x:y as z:'")
```

where you just have to fill in the arguments to `analogies(...)` and `closest_words(...)` and write those functions, as described below.

To learn more about passing arguments from the command line to your Python program, see the bottom of our [bash intro](https://github.com/parrt/msds501/blob/master/notes/bash-intro.md).

Users can quit the program by typing "exit" instead of a word or word analogy (you can also kill the running program by using control-C or control-D (on unix), which means "end of file"). That makes the loop terminate and therefore the program.

### Getting word vector data

The first thing your program needs to do is load the word vector "database". Download the (HUGE) [Common Crawl (42B tokens, 1.9M vocab, uncased, 300d vectors, 1.75 GB download): glove.42B.300d.zip](http://nlp.stanford.edu/data/glove.42B.300d.zip) file from the [GloVe project](https://nlp.stanford.edu/projects/glove) and unzip it into a data directory. (I recommend directory `data` sitting at the root of your user account; e.g., mine is `/Users/parrt/data`.) The unzipped filename is `glove.42B.300d.txt`:

```bash
$ mkdir ~/data # a good place to store data
$ cd ~/data
$ unzip glove.42B.300d.zip
$ ls -l
...
-rw-rw-r--@    1 parrt  staff  5025028820 Oct 24  2015 glove.42B.300d.txt
...
```

(`~` from the command line means your user home directory, such as `/Users/parrt`.)

You will pass that directory name containing your glove data to the main `wordsim.py` program so that it knows where the data is (which will be different on your machine than mine, so we use a command line argument).

The space-separated format of the glove word vector file is extremely simple: it's just the token (usually a word) followed by the components of the word vector. For example:

```
, 0.18378 -0.12123 -0.11987 0.015227 ...
the -0.20838 -0.14932 -0.017528 -0.028432 ...
. 0.10876 0.0022438 0.22213 -0.12102 ...
and -0.09611 -0.25788 -0.3586 -0.32887 ...
...
```

One of the problems we have in data science is that files can be huge, as is the case here. 5,025,028,820 characters is 5 gigabytes (5G), which could expand to much more after loading it into memory.  This will start to get close to the amount of RAM you have in your laptop but you should be okay. Even with a fast machine with an SSD instead of a spinning disk, it takes a few minutes to load all of that text and convert it into floating-point numbers. That will be painfully slow as you try to develop your code because you must reload that data every time you start up `wordsim.py`.

#### Saving the word vectors in NumPy binary

To make development faster and easier, let's convert that text file into a binary format that is not only smaller but much faster to load.  The idea will be to write a small script to load in the text once and save it in binary into a different file. I call my script `save_np.py`, but you can call it whatever you want since I'm not going to run it during testing; it's for your own use. Subsequent runs of your main program can load the faster version of the file. The goal of the script is to create two new files from the original text version:

* `~/data/glove.42B.300d.vocab.txt` A list of words from the original word vector file; one word per line
* `~/data/glove.42B.300d.npy` A matrix containing all of the word vectors as saved by NumPy's `save()` method. Each row of the matrix represents the word vector for a word.

My script reads the original glove text file line by line using `f.readlines()`. If you try to load the entire thing with `f.read()` and do a `split('\n')` or similar, you will run out of memory or run into speed problems for sure. So, process the lines one by one, adding the associated word to a vocabulary list of strings and the word vector to a list of numpy arrays.  Given a line, `split(' ')` will give us a list containing the vocabulary word as the first element and the word vector as the remaining 300.  If those 300 strings, one per floating-point number, is in `v` then `np.array(v, dtype=np.float32)` will get you a fast conversion to a numpy array.  From the list of arrays, we can make a matrix with `np.array(mylistofvectors)`. Save the list of vocabulary words, one per line, into the `glove.42B.300d.vocab.txt` file and use `np.save()` to save the matrix into `glove.42B.300d.npy`.

On my machine, it takes about 3 minutes 30 seconds to load the original text the data file and save the two new files in the same directory. From the command line, you can time how long things take easily:

```bash
$ time python save_np.py 
Loaded matrix of shape (1917494, 300)
Saved 1917494 words into vocabulary file
Saved matrix into .npy file

real	3m29.343s
user	1m51.068s
sys	0m28.134s
```

The resulting binary file is half the size:

```
$ ls -l ~/data/glove.42B.300d.*
-rw-r--r--  1 parrt  staff  2300992928 Apr  8 16:35 /Users/parrt/data/glove.42B.300d.npy
-rw-rw-r--@ 1 parrt  staff  5025028820 Oct 24  2015 /Users/parrt/data/glove.42B.300d.txt
-rw-r--r--  1 parrt  staff    17597168 Apr  8 16:35 /Users/parrt/data/glove.42B.300d.vocab.txt
```

The real benefit is that loading the matrix from the binary file is much faster than loading from a text file. For example, this code:

```python
# file is called load_np.py
import numpy as np
filename = "/Users/parrt/data/glove.42B.300d.npy"
vecs = np.load(filename)
print(f"Loaded matrix with shape {vecs.shape}")
```

executes in 1.5 seconds instead of 3 1/2 minutes:

```bash
$ time python load_np.py 
Loaded matrix with shape (1917494, 300)

real	0m1.548s
user	0m0.130s
sys	0m1.410s
```

#### Debugging word vector loading

For debugging purposes, as you try to load and save the glove files, you might want to grab the first 50 lines or so from the original text file and store that into a small file. This will take milliseconds to load and you can step through with the debugger to figure out why it is not loading properly or whatever.  The following command on the command line creates such a file for you.

```bash
head -50 glove.42B.300d.txt > glove50.txt
```

The first 50 tokens are: `, the . and to of a in " is for : i ) that ( you it on - with 's this by are at as be from have was or your not ... we ! but ? all will an my can they n't do he more if`. When debugging, you will have to have your program load this file instead of the real `glove.42B.300d.txt` file.


#### Restricting the vocabulary to improve interaction speed

We have another issue with the size of our data set.  While we can load the 1,917,494 words and their vectors quickly, that does not mean we can search through them linearly (one by one) quickly to compute distances and so on.  When I run my solution for this project on the full 1.9M words, it takes about 30 seconds to find similar words and do word analogies.  That does not provide a very good user experience and, while we could fix this using parallel processing, we'll simply restrict the size of the vocabulary to the 235,886 words in the dictionary available on your Mac or Unix machine:

```bash
$ head /usr/share/dict/words 
A
a
aa
aal
aalii
aam
Aani
aardvark
aardwolf
Aaron
$ wc -l /usr/share/dict/words 
  235886 /usr/share/dict/words
```

Being able to choose a reasonable subset of your data for development or other purposes is a useful skill, so let's incorporate that into our final method that loads the words and word vectors:

```python
def load_glove(dir:str) -> dict:
    """
    Given The name of the directory holding files glove.42B.300d.npy and
    glove.42B.300d.vocab.txt, this function returns a dictionary mapping
    a string word to numpy array with the associated 300 dimensional
    word vector. The words are restricted to those found within
    file /usr/share/dict/words (make sure to convert those words to
    lowercase for normalization purposes).
    """
    ...
```

### Computing similar words

Given a word, *w*, the easy way to find the *n* nearest words is to exhaustively compute the distance from *w*'s vector to every other vector in the database. Sort by the distance and take the first *n* words. Here is the signature of the function you must implement and a comment describing its implementation:

```python
def closest_words(gloves, word, n):
	"""
	Given a gloves dictionary of word:vector and a word return the n nearest words
	as a list of strings. The word is not considered his own nearest neighbor,
	so do not include that in the returned list.
	
	Compute the Euclidean distance between the vector for word and
	every other word's vector. Track the distances with a list of tuples
	of the form: (distance, word).  Sort the list by distance. Return a list
	of the first n words from the sorted list. Do not return the tuples, just the words. Return a python list of strings not numpy array.
	"""
	...
```

Given input `lizard`, your program should respond with:

```
lizard is similar to {snake iguana crocodile frog turtle}
```

Given input `russia`, your program should respond with:

```
russia is similar to {moscow russian soviet iran finland}
```

### Computing missing analogy words

Your final goal is to complete partial analogies given to you by the user. In other words, given input "`shoe:foot as glove:`", your program should respond with:

```bash
shoe is to foot as glove is to {foot hand finger thumb leg}
```

(As you can see it's not perfect, but it does get `hand` as the second closest.)

The key is to look at the relationship between words, which means vector difference. Take a look at the following 2D projection of some word vectors and the vector differences, such as `['madam','mister','niece', 'nephew', 'king', 'queen']`.

<img src="figures/male-female-vectors.png" width="250">

In 2D, the vector differences all are semi-flat vectors meaning they are pretty similar. 

Here's how to use vector differences for word analogies `x:y as z:`. Compute the vector difference between the first two words and then look for similar vector differences. The simplest mechanism is to exhaustively compare the x-y vector difference to the vector difference from z to all other words in the table. If we sort by distance, the first n words will be the most appropriate words to finish the analogy. Here is your code template for the function.

```python
def analogies(gloves, x, y, z, n):
    """
    Given a gloves dictionary of word:vector and 3 words from
    "x is to y as z is to _____", return the n best words that fill in
    the blank to complete the analogy.

    Compute the vector difference between x and y then compute the              
    vector difference between z and all vectors, v, in gloves database          
    (ignore v=z).  You care about the distance between the xy vector            
    and the zv vector for all vectors v. Track the distances with a             
    list of tuples of the form: (distance, word).  Sort the list by             
    distance. Return a list of the first n words from the sorted                
    list. Do not return the tuples, just the words.                             
    """
    ...
```

## Where to go from here

### Using PCA to display word vectors

If you are feeling particularly frisky near the end of the boot camp, you can do a nice visualization of word vectors. The idea is to take the very large 300-dimensional vectors and project them onto just 2-dimensional space so that we can plot them. The key to such a compression is to perform *principal components analysis* (PCA) on a set of word vectors, which you might hear about in the linear algebra boot camp. This is how I drew the graph above for the words king, queen, and cat (and 3 nearest neighbors). Here is some skeleton code for you to get started:

```python
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

def plot_words(gloves, words, n):
    """
    Get a list of vectors for n similar words for each w in words.
    Flatten that into a single list of vectors, including the original
    words' vectors.  Compute a word vector for each of those words and
    put into a list. Use PCA to project the vectors onto two dimensions.
    Extra separate X and Y coordinate lists and pass to matplotlib's scatter
    function. Then, iterate through the expanded word list and plot the
    string using text() with, say, fontsize=16. call show().
    """
    ...
    wvecs = ...
    pca = PCA(n_components=2)
    vecs2D = pca.fit_transform(wvecs)
    ...
```

For words `petal`, `software`, and `car` you should get:

<img src="figures/wordvec2.png" width=400>

### Speeding up the data load

**TODO**: next year load CSV, set index of dataframe as word, save as feather. Load is 2.5s not 35s.  Don't need a `dict` when df will suffice. actually, turns out df row access via index is super super slow. loading from feather does help of course.

By playing around, I've managed to drop the time to load data from 30 seconds to 18 seconds using the binary [feather](https://github.com/wesm/feather) format. (This is super useful later when you do machine learning stuff.) The idea is to use Pandas' `read_csv` function to load the text file, which is also faster than reading line by line in Python, and then save the resulting data frame into a feather file. Then you can read that feather file in about 2.5 seconds instead of reading the text file again.  We have to convert the data frame to a dictionary, which is pretty slow to do it manually, but we gain some speed over the previous method. 

Naturally, my tests do not use this feather functionality, but you should consider exploring how to make this happen.

First, you need to have the appropriate libraries installed:

```bash
pip install -U feather-format
```

Then, figure out how to use the parameters of the `read_csv` function to create a data frame in memory of the glove data file. Then save that as a feather file.

Once we have this file laying around, we can use it instead of the original glove text file. Use function `read_feather`.

Once we have a data frame in memory, we can convert it to the appropriate dictionary. I tried using the `itertuples` data frame method to walk the rows to create the dictionary but it was slightly slower than converting the data frame to a numpy matrix first and walking those rows. I also tried using `to_dict` but I couldn't figure out an argument that would make it create the proper dictionary we want for this project.
 
## Deliverables

In your repository, you should submit file `wordsim.py` in the root directory containing all of the code described above, except for the extra plotting code (that you can do in a separate file for your own enjoyment). We will only be testing the nearest neighbor and word analogy functionality.

*Do not add the word vector glove data to the repository!*

You can use numpy (e.g., `np.linalg.norm()`) but please do not refer to a bunch of random packages that I probably don't have installed on my test box. Your test will fail.

*Please do not leave a bunch of debugging print statements in your code.* The output of your program is part of your result so make sure you only emit what you are supposed to.

## Evaluation

Please be aware that, depending on the hardware you run this on, the program could be fairly slow. On my iMac, the test described here takes 50 seconds, which includes time to load and process the 1G file containing 400,000 words. *If it takes many minutes to process, we will assume there’s a problem with your code.*

We will run your program from the command line as follows using the 300-dimensional vectors:

```bash
$ python test_wordsim.py ~/data/glove/glove.6B.300d.txt 
All tests pass
$ 
```

If there is an error, you will see something like this:

```bash
$ python test_wordsim.py ~/data/glove/glove.6B.300d.txt 
similar words for dog should be ['dogs', 'cat', 'pet', 'puppy', 'hound'] but was ['poodle', 'cat', 'pet', 'puppy', 'hound']
$
```

**It must run in under 2 minutes to get credit for the project.**

Here is the test rig file `test_wordsim.py`:

```python
from wordsim import *
import sys

word_input = [
    'dog', 'cow', 'spain', 'king', 'frog', 'run'
]
word_output = [
    ['dogs', 'cat', 'pet', 'puppy', 'hound'],
    ['cows', 'mad', 'bovine', 'sheep', 'goat'],
    ['portugal', 'spanish', 'morocco', 'madrid', 'spaniards'],
    ['queen', 'monarch', 'prince', 'kingdom', 'reign'],
    ['toad', 'frogs', 'monkey', 'squirrel', 'snake'],
    ['running', 'runs', 'ran', 'allowed', 'go']
]

analogy_input = [
    ['building', 'architect', 'software'],
    ['king', 'queen', 'man'],
    ['german', 'english', 'french'],
    ['spanish', 'spain', 'french'],
    ['ship', 'vessel', 'car']
]
analogy_output = [
    ['programmer', 'architect', 'designer', 'computer', 'microsoft'],
    ['woman', 'girl', 'person', 'teenager', 'she'],
    ['english', 'welsh', 'spanish', 'language', 'prohertrib'],
    ['france', 'belgium', 'paris', 'spain', 'prohertrib'],
    ['vehicle', 'cars', 'truck', 'driver', 'driving']
]

glove_filename = sys.argv[1] # must pass in the 300-Dimensional vectors
gloves = load_glove(glove_filename)

errors = []

for i,w in enumerate(word_input):
    closest = closest_words(gloves, w.lower(), 5)
    if sorted(closest) != sorted(word_output[i]):
        errors.append("similar words for %s should be %s but was %s" % (w,word_output[i],closest))

for i,w in enumerate(analogy_input):
    analogs = analogies(gloves, w[0].lower(), w[1].lower(), w[2].lower(), 5)
    if sorted(analogs) != sorted(analogy_output[i]):
        errors.append("analogy for %s should be %s but was %s" % (w,analogy_output[i],analogs))

if len(errors)>0:
    print('\n'.join(errors))
else:
    print("All tests pass")
```

Because the order of words could be slightly different depending on the dictionary implementation, I have sorted the results before comparing them.