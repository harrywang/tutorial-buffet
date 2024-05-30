## About

This is my revised code of the tutorial at: https://medium.com/abn-amro-developer/data-pipeline-orchestration-on-steroids-apache-airflow-tutorial-part-1-87361905db6d


## Setup
I assume you have airflow (2.1.0) running locally on your mac by running the commands at https://airflow.apache.org/docs/apache-airflow/stable/start/local.html

```
export AIRFLOW_HOME=~/airflow
pip install apache-airflow
airflow db init
airflow users create \
    --username admin \
    --firstname Harry \
    --lastname Wang \
    --role Admin \
    --email harryjwang@gmail.com

# start the web server, default port is 8080
airflow webserver --port 8080

# start the scheduler
# open a new terminal or else run webserver with ``-D`` option to run it as a daemon
airflow scheduler

```

Now, you can access airflow at http://localhost:8080

Open `/Users/harrywang/airflow/airflow.cfg` you can find the path to hold your dag python file: `dags_folder = /Users/harrywang/airflow/dags` you may need to create this folder. 

`simple_bash_dag.py` is a simple DAG that create an empty txt file and then rename it - two tasks in a sequence. 

copy the dag files to the dag folder, then run `airflow scheduler` (airflow does not auto refresh, you have to run this command manually to see the newly added dag file), you should be able to see the dag via UI.

You can trigger the DAG as follows:

<img width="1270" alt="Screen Shot 2021-06-01 at 11 37 32 AM" src="https://user-images.githubusercontent.com/595772/120351408-defae180-c2cd-11eb-8997-42d3fbb689de.png">






