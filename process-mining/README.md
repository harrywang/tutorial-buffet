# About

A script to convert a txt log into process mining log format. The key of this notebook is to show how to use a pre-defined time gap to identify a user session

## Data

The log file is very big, the following commands can help get a small sample of the file for EDA and other tasks.

### Utility Commands

Run `$ wc -l search.txt` to find out the total number of lines in the file. When the file is too big for efficient pandas analysis and you can split it into smaller files with 100,000 lines each by using Linux version of `split`.

```
$ brew install coreutils
$ gsplit -a 4 -d -l 10000 file.txt search_
```

## Setup

Tested with Python 3.6 via virtual environment:
```shell
$ python3.6 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ jupyter notebook
```

- log2csv notebook converts the text into a csv.
- log-eda notebook converts the log into process mining log
