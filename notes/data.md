# Data Massaging

Our generic analytics program template

1. Acquire data, which means finding a suitable file or collecting data from the web and storing in a file
2. Load data from disk and place into memory organized into data structures
2. Normalize, clean, or otherwise prepare data
3. Process the data, which can mean training a machine learning model, computing summary statistics, or optimizing a cost function
4. Emit results, which can be anything from simply printing an answer to saving data to the disk to generating a fancy visualization


To make loading data meaningful, we'll also learn how to generate histograms from data files using [matplotlib](https://matplotlib.org/).

tuples
set
list of tuples
dict

X to x, y

missing values
	delete row
	insert value

scatter

sine wave

histogram; unif, normal

## Word clouds

Python has a nice library you can use:

```bash
$ pip install wordcloud
```

```python
from wordcloud import WordCloud
from csvcols import get_column
import matplotlib.pyplot as plt
import sys

...
wordcloud = WordCloud(width=1800,
                      height=1400,
                      max_words=10000,
                      random_state=1,
                      relative_scaling=0.25)

... get tuples with (word,count) from categories Counter ...                      
wordcloud.fit_words(wordtuples)

plt.imshow(wordcloud)
plt.axis("off")
plt.show()
```
