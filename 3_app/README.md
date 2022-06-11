# Flask Endpoint

## Import Postman Collection

## Request
```bash
curl --request POST 'http://localhost:5000/predict' \
--header 'Content-Type: application/json' \
--data-raw '{
"fixed acidity": 5,
"volatile acidity": 5,
"citric acid":5,
"residual sugar": 5,
"chlorides": 5,
"free sulfur dioxide": 5,
"total sulfur dioxide": 5,
"density": 5,
"pH": 5,
"sulphates": 5,
"alcohol": 5
}'
```