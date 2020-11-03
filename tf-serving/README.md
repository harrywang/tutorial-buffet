# About

My revised code based on:

- https://thelongrun.blog/2020/01/12/rest-api-tensorflow-serving-pt1/
- https://thelongrun.blog/2020/01/26/rest-api-tensorflow-serving-pt2/


# Setup

Setup virtual environment and install packages:
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Pull tf serving docker image (I assume you installed docker: https://docs.docker.com/get-docker/): 
```
docker pull tensorflow/serving:latest
```

Create tf serving servables from tf functions and pre-trained models, two servables will be generated and saved in `/models/` folder:

```
python make_servables.py
```

# Start TF Serving Servers

Use tf serving to serve two models from different host ports: 8501 and 8502 by running the following command **in the repo root folder**:
```
docker run -t --rm -p 8501:8501 -v "$(pwd)/models/mobilenet_v2_test:/models/mobilenet_v2_test" -e MODEL_NAME=mobilenet_v2_test tensorflow/serving &

docker run -t --rm -p 8502:8501 -v "$(pwd)/models/add_two:/models/add_two" -e MODEL_NAME=add_two tensorflow/serving &
```

You should see two docker apps running:

<img width="753" alt="Screen Shot 2020-11-03 at 5 45 23 PM" src="https://user-images.githubusercontent.com/595772/98048786-6c3f8b80-1dfc-11eb-808d-f4c0697305ae.png">

# Use REST APIs for Computing/Inference

Call the `AddTwo()` function using `curl`, which will add 2 to each number in the tensor:
```
curl -H "Content-Type: application/json" -d '{"instances":[1.0, 5.0, 4.0]}'  http://localhost:8502/v1/models/add_two:predict
```

Call MobileNet classifier using `curl`:
```
chmod +x client_curl.sh 
./client_curl.sh ./images/animal.jpg
```

Call MobileNet classifier using `curl` via python: 

```
python client.py
```


