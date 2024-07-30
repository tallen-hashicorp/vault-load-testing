# Vault Example Load Testing
Using Locust.io to load test Vault

## To Install
```bash
brew install locust
```

# Get Key-Value (KV)

* On Start, create KV mount `locust-load-test`
* Write KV `some-key` with data `{"hello": "world"}`
* Read KV `some-key`

## How to Run Get KV

```bash
export VAULT_TOKEN=[TOKEN]
locust -f get_kv.py
```

* Then go to [locust](http://127.0.0.1:8089/)
* Select host - `http://127.0.0.1:8200`

# Monitoring

To help us monitor Vault, I have included a basic Prometheus and Grafana Docker setup. In order to run:
* Create a file in `./vault_monitor` called `prometheus-token` that contains a token to access Vault's metrics. For this, I'm personally using the root token.
* Update the `targets` in `./vault_monitor/prometheus.yml` to point at the Vault server.
* Run:
    ```bash
    cd vault_monitor
    docker compose up
    ```
* Go to [http://127.0.0.1:3000](http://127.0.0.1:3000)
* Login with `admin/admin`
* Then add Prometheus
* Set the Prometheus server URL to `http://prometheus:9090` 
* Click `Create your first dashboard`
* Select `Import`
* Select ID `12904`
* Select `Promxy` as your Prometheus

# TODO

* Add some PKI
* Add some service token generation
* Add some batch token generation
* Take advantage of [Resource quotas](https://developer.hashicorp.com/vault/docs/concepts/resource-quotas)
* Look into [Adaptive overload protection](https://developer.hashicorp.com/vault/docs/concepts/adaptive-overload-protection)