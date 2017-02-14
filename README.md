# PythonDataFreq

Problem A

The programming in this problem will be fairly straightforward, but it is important that you understand the motivation, as follows.

Imagine a 3-question survey, with each question asking the respondent to rate a product from 1 to 5. There will be 53 = 125 possible patterns, i.e. (1,1,1), (1,1,2),...,(5,5,5). We are interested in determining which patterns in our data set are most common.

For example, say there are 7 people who completed the survey, and they answered (5,4,5), (5,2,3), (5,4,5), (1,4,2), (3,3,3), (5,4,5), (1,4,2). Then the most frequent pattern was (5,4,5), and the second-most frequent one was (1,4,2).

We might store our frequencies in a two-dimensional array, with the first 3 columns being the pattern and the last column being the frequency. So, we'd have 4 rows, one for each of the patterns we found, with one of the rows being (5,4,5,3).

Now consider what would happen if the survey had 50 questions, with a large number of respondents. There would now be 550 possible patterns, and though most patterns would not show up in the data, the above 2-D array would have a ton of rows. That in itself is not so bad, but what if we want to do many queries, asking the frequencies of various patterns? Then we would have to do a search through the array each time, which could be really slow.

A better approach would be the use a Python dictionary. In the above example, we might create a dictionary freqs, with for instance freqs['5,4,5'] equal to 3. This way we could do associative lookups; for instance, we would submit the query '5,4,5' and the return value would be 3. This would be much faster, because Python dictionaries are implemented as hash tables.

The other issue is that real-world data is messy, with a lot of missing values. For example, we might have a record consisting of (5,4,NA), where NA means "not available." This is an R term, roughly the same as Python's None. But it partly matches the (5,4,5) pattern in our data, so we might count it as 2/3 of a match to (5,4,5). So, the frequency of (5,4,5) would be 3 2/3. And if we had had, say, a (5,4,1) record in our data, that would count 2/3 as well. If we have 4 questions in our survey, a record with 2 NAs but which matches an intact record in the other 2 components, it would count as half a match. Partial matches are made only of nonintact patterns to intact patterns.

So here are the specs:

Write a function calcfreqs(infile,nqs,maxrat, with arguments as follows: The input file name is given by infile; the number of questions in the survey is nqs; and the choice of responses is 1...maxrat. The return value is a Python dictionary as described above.
The input file's line format is, e.g.
5 4 NA
Have your code raise an exception, with an error message printed, if the file doesn't exist, or if a line in the file is found to have an error.
Write a function highfreqs(freqs,k), where freqs is the output of calcfreqs(), and k is a positive integer. The return value is the subdictionary corresponding to the patterns with the k highest frequencies. If two different patterns have the same frequency and the latter is among the k highest, include them both. Also, if k is negative, find the least frequent patterns, not the most.
Place your entire code in a file ProblemA.py.
Below is an example, using the file y,

5 4 5
NA 3 3
5 2 3
5 4 5
1 4 2
5 4 NA
4 NA 1
5 4 1
3 3 3
5 2 3
5 4 5
1 4 2
>>> from Freq import *
>>> fr = calcfreqs('y',3,5)
>>> fr
{'5,4,5': 3.6666666666666665, '1,4,2': 2, '5,4,1': 1.6666666666666665,
'3,3,3': 1.6666666666666665, '5,2,3': 2}
>>> highfreqs(fr,2)
{'5,4,5': 3.6666666666666665, '1,4,2': 2, '5,2,3': 2}
