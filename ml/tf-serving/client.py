import json
import requests
import base64
 
data = {}
with open('images/animal.jpg', mode='rb') as file:
    img = file.read()
data = {"inputs":[{"b64":base64.encodebytes(img).decode("utf-8")}]}
 
# Making the request
r = requests.post("http://localhost:8501/v1/models/mobilenet_v2_test:predict", data=json.dumps(data))
print(r.content)
# And returns:
# b'{\n    "outputs": [\n        "giant panda"\n    ]\n}'