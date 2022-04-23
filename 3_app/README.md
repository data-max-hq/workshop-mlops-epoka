# Flask Endpoint

## Request
```bash
curl --location --request POST 'http://localhost:5005/predict' \
--header 'Content-Type: application/json' \
--data-raw '{
    "text": ["This is a text"]
}'
```