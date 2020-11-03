# $1 refers to the path where the image file is located
ENCODED_IMG="$(base64 $1)"
(echo '{"inputs": [{"b64": "'; echo "$ENCODED_IMG"; echo '"}]}') | curl -H "Content-Type: application/json" -d @-  http://localhost:8501/v1/models/mobilenet_v2_test:predict