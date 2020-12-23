# About
The examples at https://github.com/allegroai/clearml/tree/master/examples/frameworks

By default, the results are logged to the demo server (no authorization configuration needed and all users SHARE all results!!): https://demoapp.trains.allegro.ai/login
# Setup and Run

```
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt 
$ pip install -r matplotlib/requirements.txt
$ python matplotlib/mlp_grouped_errorbar.py
```
Then follow the address in the terminal to view the result:

```
TRAINS results page: https://demoapp.trains.allegro.ai/projects/7b8167f284e0477389cd1d3701dad113/experiments/89618f511e4346debc7679d3f55ab8bc/output/log
```

# Notes

1. 12/22/2020 - you have to lock PyJWT==1.7.1, the latest 2.0.0 breaks the system
2. when using matplotlib if you have problem with tkinter for certain python version, using agg instead:

```
import matplotlib
matplotlib.use('agg') # use agg instead of tkinter
```

See my example at `matplotlib/mlp_grouped_errorbar.py`, only need to add the following lines:

```
from trains import Task
task = Task.init(project_name='examples', task_name='Matplotlib GroupedBar example by Harry')
```