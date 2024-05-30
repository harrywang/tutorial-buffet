# About

This is the pre-processing script to convert a csv to arff for openml data upload at https://www.openml.org/d/42634

After a csv is created, you need to use the weka to load and save the csv as raff file and then upload to openml.org:

<img width="496" alt="Screen Shot 2020-08-28 at 4 26 08 PM" src="https://user-images.githubusercontent.com/595772/91612350-39d06880-e94b-11ea-968a-1f44e1fb6afa.png">


NOTE: https://pypi.org/project/csv2arff/ does not work - lots of errors.



## Setup

Tested with Python 3.6 via virtual environment:
```shell
$ python3.6 -m venv venv
$ source venv/bin/activate
$ jupyter notebook
```

