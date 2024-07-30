# Vault Example Load testing
Using Locust.io to load test Vault

## To Install
```bash
brew install locust
```

# Get Key-Value (KV)

* On Start, create KV mount locust-load-test
* Write KV some-key with data {"hello": "world"}
* Read KV some-key

## How to Run Get KV

```bash
export VAULT_TOKEN=[TOKEN]
locust -f get_kv.py
```

* Then goto [locust](http://127.0.0.1:8089/)
* Select host - http://127.0.0.1:8200


# TODO

* Set up Prometheus and Grafana monitoring
* Add some PKI
* Add some service token generation
* Add some batch token generation
* Take advantage of [Resource quotas](https://developer.hashicorp.com/vault/docs/concepts/resource-quotas)
* Look into [Adaptive overload protection](https://developer.hashicorp.com/vault/docs/concepts/adaptive-overload-protection)
