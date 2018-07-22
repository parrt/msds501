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
