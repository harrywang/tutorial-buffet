# About
The examples at https://github.com/allegroai/clearml/tree/master/examples/frameworks

# Setup and Run

## Demo Server
By default, the results are logged to the demo server (no authorization configuration needed and all users SHARE all results!!): https://demoapp.demo.clear.ml/

```
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt 
$ pip install -r matplotlib/requirements.txt
$ python matplotlib/mlp_grouped_errorbar.py
```

Then follow the address in the terminal to view the result:

```
ClearML results page: https://demoapp.demo.clear.ml/projects/7b8167f284e0477389cd1d3701dad113/experiments/395a49ae59b2464299fddc479146fc27/output/log
```
<img width="1272" alt="Screen Shot 2020-12-22 at 7 11 25 PM" src="https://user-images.githubusercontent.com/595772/102944700-8b1bdf00-4489-11eb-9717-b327a2fb2de3.png">

## ClearML Server or Self-Hosted Server

You can self host ClearML server by following my note at: https://github.com/harrywang/tutorial-buffet/tree/master/clearml-server

Once the server is up and running, you can login and get to the profile page to get the credentials.

Go to https://app.community.clear.ml/, login and go to profile page, create a new credential, you should see the following page:

<img width="1038" alt="Screen Shot 2020-12-27 at 2 37 40 PM" src="https://user-images.githubusercontent.com/595772/103178498-51fcb980-4851-11eb-9522-fab299acbf87.png">

Create `clearml.conf` with the information from the screen above: `$ vim ~/clearml.conf` or run `clearml-init` to setup the file step by step.

Now, run `$ python matplotlib/mlp_grouped_errorbar.py` again and your result is logged to the community server under your username (login required), e.g., https://app.community.clear.ml/projects/5a0ad99dd5b749d4931dee5da1e47870/experiments/7b9eae9bbd0a42bdbe887bf111c80b13/output/log


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