# vault-load-testing
Using locust.io to load test Vault

## To Install
```bash
brew install locust
```

## How To Run
```bash
export VAULT_TOKEN=[TOKEN]
locust -f locustfile.py 
```
* Then goto [locust](http://127.0.0.1:8089/)
* Select host - http://127.0.0.1:8200
