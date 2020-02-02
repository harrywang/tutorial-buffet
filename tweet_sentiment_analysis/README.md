## Tweet Sentiment Analysis with Python 3

This is my revision of the tutorial at https://dev.to/rodolfoferro/sentiment-analysis-on-trumpss-tweets-using-python - many thanks to the author. The original repo is at https://github.com/RodolfoFerro/pandas_twitter

The original author provides markdown version of his tutorial. I combine all files into one: tutorial.md and create a English version of the Jupyter notebook (the author only had a Spanish version).

## Summary
**Data**: 200 Tweets from Donald Trump: https://twitter.com/realDonaldTrump

**Goal**: Conduct a sentiment analysis of the tweets with sample result:

- Percentage of positive tweets: 53.5%
- Percentage of neutral tweets: 23.0%
- Percentage of negative tweets: 23.5%

Python packages used: jupyter, pandas, numpy, tweepy, textblob

## API Keys
Change API key for Twitter: In order to extract tweets for a posterior analysis, we need to access to our Twitter account and create an app. The website to do this is https://apps.twitter.com/. (If you don't know how to do this, you can follow this tutorial video https://www.youtube.com/watch?v=BOA7SD_09Qk to create an account and an application.)


- Consumer Key (API Key)
- Consumer Secret (API Secret)
- Access Token
- Access Token Secret

**You should never put your real API key in the code and push to Github.** We use local environment variables for the API keys:

```
# Get the API key from local environment variable
CONSUMER_KEY = os.environ.get('TWITTER_CONSUMER_KEY')
CONSUMER_SECRET = os.environ.get('TWITTER_CONSUMER_SECRET')
ACCESS_TOKEN = os.environ.get('TWITTER_ACCESS_TOKEN')
ACCESS_SECRET = os.environ.get('TWITTER_ACCESS_SECRET')
```

You need to add the following lines to the `~/.bash_profile` file
```
export TWITTER_CONSUMER_KEY='yourealkey'
export TWITTER_CONSUMER_SECRET='yourealkey'
export TWITTER_ACCESS_TOKEN='yourealkey'
export TWITTER_ACCESS_SECRET='yourealkey'
```

then, use `vim` to edit, `source` to execute it, then use `env` to double check):

```
$ vim ~/.bash_profile
$ source ~/.bash_profile
$ env
```
**NOTE: You may need to close the Terminal window and restart it for Jupyter Notebook to read the new variables you just added.**

## Setup

Clone the repo, go to the repo folder, setup the virtual environment, and install the required packages:

```
$ cd path_to_document-clustering
$ virtualenv -p python3 venv
$ source venv/bin/activate
$ pip3 install -r requirements.txt
```

Run `$ jupyter notebook` to go over the tutorial step-by-step.
