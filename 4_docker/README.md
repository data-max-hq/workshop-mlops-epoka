# Build Docker image

```shell
docker build -t mlops-serve:0.1 .
```


```shell
docker run -it -p 5000:5000 mlops-serve:0.1
```

### Send request

```shell
curl --location --request POST 'http://localhost:5005/predict' \
--header 'Content-Type: application/json' \
--data-raw '{
    "text": ["This is a text"]
}'
```