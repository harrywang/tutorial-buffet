## Document Clustering with Python 3

This is my revision of the great tutorial at http://brandonrose.org/clustering - many thanks to the author.

## TL;DR
**Data**: Top 100 movies (http://www.imdb.com/list/ls055592025/) with title, genre, and synopsis (IMDB and Wiki)

**Goal**: Put 100 movies into 5 clusters by text-mining their synopses and plot the result as follows

<img width="771" alt="screenshot 2016-05-23 20 50 20" src="https://cloud.githubusercontent.com/assets/595772/15488829/5b863710-2128-11e6-843b-25aac76bd134.png">

## Setup

First, clone the repo, go to the repo folder, setup the virtual environment, and install the required packages:

```
$ cd path_to_document-clustering
$ virtualenv -p python3 venv
$ source venv/bin/activate
$ pip3 install -r requirements.txt
```
Second, use nltk.download() to download all nltk packages (a GUI will open and you can choose to install all packages: ~ 3.5G), which are saved to /Users/your_mac_username/nltk_data

```
ipython
import nltk
nltk.download()
```

Lastly, run `$ jupyter notebook` to go over the tutorial step-by-step.

## Key Steps
1. **Read data**: read titles, genres, synopses, rankings into four arrays
2. **Tokenize and stem**: break paragraphs into sentences, then to words, stem the words (without removing stopwords) - each synopsis essentially becomes a bag of stemmed words.
3. **Generate tf-idf matrix**: each row is a term (unigram, bigram, trigram...generated from the bag of words in 2.), each column is a synopsis.
4. **Generate clusters**: based on the tf-idf matrix, 5 (or any number) clusters are generated using k-means. The top key terms are selected for each cluster.
5. **Calculate similarity**: generate the cosine similarity matrix using the tf-idf matrix (100x100), then generate the distance matrix (1 - similarity matrix), so each pair of synopsis has a distance number between 0 and 1.
6. **Plot clusters**: use multidimensional scaling (MDS) to convert distance matrix to a 2-dimensional array, each synopsis has (x, y) that represents their relative location based on the distance matrix. Plot the 100 points with their (x, y) using matplotlib (I added an example on using plotly.js).
