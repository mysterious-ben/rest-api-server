# REST API server
A simple self-hosted server to test REST request processing.

Supported requests:
- GET requests with JSON data

## Run
Start a local uvicorn server:
```console
uvicorn src.app:app
```

## HTTP Endpoints
- Hello world: `/`
- JSON data with ID: `/items/{item_id}`
- JSON data sample: `/data/sample`
- String data sample: `/data/sample&json=0`
- JSON data with a status code: `/data/raise?code={status_code}`
- JSON data with an incorrect "Content-Length": `/data/wronglength`
- JSON data with a correct "Content-Length": `/data/wronglength?error=0`
