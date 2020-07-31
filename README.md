# ns1-test

## Build and Run: 
```
docker-compose up
```
Server runs on port 5000

1. POST to `/messages` endpoint: `curl -i -H "Content-Type: application/json" -X POST -d '{"message":"hello"}' localhost:5000/messages`
2. This returns a hashed string
3. GET message using hash string: `curl -i localhost:5000/messages/<hash>`
4. Get `/metrics` endpoint: `curl -i localhost:5000/metrics`