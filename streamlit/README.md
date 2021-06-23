# About

This is my revised code for tutorial at https://towardsdatascience.com/streamlit-101-an-in-depth-introduction-fc8aad9492f2

Changes:

- changed data file and make it self-contained in the repo
- added requirements.txt and virtual environment setup

## Local Setup

Python 3 required, see my tutorial to setup Python 3: https://bit.ly/2uX6wAX

Clone the repo, go to the repo folder, setup the virtual environment, and install the required packages:


```shell
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

Run the app locally (Local URL: http://localhost:8501) using terminal: `streamlit run airbnb.py` 

Stop the app by using ctrl + C or closing the terminal

Deploy the app to the cloud for public access via services such as streamlit share, heroku, aws by following my tutorial at https://github.com/harrywang/streamlit-basics. you can see an example at: https://st-demo-harrywang.herokuapp.com/
