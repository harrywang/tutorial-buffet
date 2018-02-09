# Introduction
This tutorial is originally published by William Koehrsen at https://towardsdatascience.com/time-series-analysis-in-python-an-introduction-70d5a5b1d52a

# Setup (Mac)

- Install python 3 using Homebrew if not done yet: `$ brew install python3`

- Create python3 virtualenv: `virtualenv -p python3 venv`

- Activate it: `source venv/bin/activate`

- Install packages: `$ pip3 install -r requirements.txt`, which include quandl seaborn matplotlib numpy pandas scipy scikit-learn fbprophet

- Change API key for Quandl: We will access financial data using the Quandl library. Please go to https://www.quandl.com/ and register to get your api_key. You will need to use your own api_key to pull data from the quandl financial library. **You should never put your real API key in the code and push to Github.** We use a local environment variable for the API key: `quandl.ApiConfig.api_key = os.environ.get('QUANDL_KEY')`. You need to add one line `export QUANDL_KEY='your_real_api_key'` to the `~/.bash_profile` file (use `vim` to edit, `source` to execute it, then use `env` to double check):
```
$ vim ~/.bash_profile
$ source ~/.bash_profile
$ env
```
**NOTE: You may need to close the Terminal window and restart it for Jupyter Notebook to read the new QUANDL_KEY you just added.**

# Run

- Start Virtual Env:
```
$ virtualenv -p python3 venv
$ source venv/bin/activate
```
- Run Jupyter: `jupyter notebook`
- Run additive_models.ipynb

### TODO: Get rid of the Deprecation Warnings
