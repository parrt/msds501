# Filter out one letter words

with open('../data/IntroIstanbul.txt') as f:
    contents = f.read() # read all content of the file
words = contents.split(' ')

words = [w for w in words if len(w)>1]
print(words[0:50])

# Do same thing but as a function

def getwords(filename):
    with open(filename) as f:
    	contents = f.read() # read all content of the file
    words = contents.split(' ')
    words2 = [w for w in words if len(w)>1]
    return words2

words = getwords('../data/IntroIstanbul.txt')
print(words[0:50])

# Strip off \n chars

with open('../data/prices.txt') as f:
    prices = f.readlines() # get lines of file into a list
prices = [p.strip() for p in prices]
prices[0:10]

# Load list of numbers from a file into numpy array

import numpy as np

with open('../data/prices.txt') as f:
    prices = f.readlines() # get lines of file into a list
prices = np.array(prices, dtype=float) # convert to array of numbers
print(prices[0:10])

# getcsv

def getcsv(filename):
    with open(filename) as f:
        lines = f.readlines()

    lines = [line.strip() for line in lines] # remove \n on end
    return [line.split(',') for line in lines]

data = getcsv('../data/player-heights.csv')
print(data)

# Convert to data frame

import pandas as pd

data = pd.DataFrame(data[1:], columns=data[0])
print(data)

# Sum prices in a file

def getsum(filename):
    with open(filename) as f:
        return sum([float(line) for line in f])

print(getsum('../data/prices.txt'))
