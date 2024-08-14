# Vault Example Load Testing

This guide demonstrates how to use Locust.io to load test Vault in a Kubernetes environment. The example uses Vault Enterprise, but you can switch to the OSS version by changing the image in `3-ClusterStatefulSet.yaml`.


## Running Vault in Kubernetes

This guide provides a comprehensive setup for deploying a highly available Vault cluster in Kubernetes using StatefulSets. The setup includes:

- **Three-Node Vault Cluster**: Ensures high availability and fault tolerance for your Vault deployment.
- **StatefulSets**: Utilizes Kubernetes StatefulSets to manage the deployment and scaling of Vault instances with persistent storage.
- **Automatic Unsealing**: Configured with Vault’s auto-unseal feature for simplified secure operations without manual intervention.
- **Load Testing**: Designed with load testing in mind, this setup prioritises test environments over persistent storage. It is optimized for running tests and is not intended for long-term data persistence other then outage simulation. 
- **Monitoring**: Equipped with Prometheus and Grafana for real-time monitoring and visualization of Vault metrics and health.

This setup is designed to provide a robust environment for both development and production scenarios with one click, offering a scalable and monitored Vault deployment with built-in resilience.

![Kubernetes Architecture](docs/vault-k8s.png)

### Start Vault

To deploy Vault and set up port forwarding, run the following commands:

```bash
kubectl apply -f k8s
kubectl -n vault get secrets vault-cluster-unseal-init-secrets -o jsonpath="{.data.vault_data}" | base64 -d
kubectl -n vault port-forward service/vault-cluster-service 8200:8200
```

### Scale Vault to Zero Replicas

If you wish to simulate a Vault outage you can by scaling down the StatefulSet to zero replicas:

```bash
kubectl -n vault scale statefulset vault-cluster --replicas=0
```

### Scale Vault Back to Three Replicas

Restore Vault to its normal state by scaling the StatefulSet back to three replicas:

```bash
kubectl -n vault scale statefulset vault-cluster --replicas=3
```

### Cleanup

To delete the deployed resources and clean up the environment, run:

```bash
kubectl delete -f k8s
```

**Note:** This environment is intended for temporary use and will be cleaned up after testing. If you plan to run it for an extended period, consider scaling down the StatefulSet instead of deleting everything.

## Locust Installation

To install Locust, use the following command:

```bash
brew install locust
```

## Key-Value (KV) Operations

### Create and Use KV Mount
The locust test will perform the following:
1. On startup, create a KV mount named `locust-load-test`.
2. Write a KV entry with key `some-key` and data `{"hello": "world"}`.
3. Read the KV entry for `some-key`.

### Run Locust for KV Operations

```bash
export VAULT_TOKEN=[TOKEN]
locust -f get_kv.py
```

- Open [Locust UI](http://127.0.0.1:8089/) in your browser.
- Set the host to `http://127.0.0.1:8200`.

## Monitoring Vault

To monitor Vault, a basic Prometheus and Grafana setup is provided. Follow these steps:

1. Create a file named `prometheus-token` in the `./vault_monitor` directory containing a token to access Vault's metrics (e.g., the root token).
2. Update the `targets` section in `./vault_monitor/prometheus.yml` to point to your Vault server.
3. Start Prometheus and Grafana using Docker Compose:

    ```bash
    cd vault_monitor
    docker compose up
    ```

4. Access Grafana at [http://127.0.0.1:3000](http://127.0.0.1:3000).
5. Log in with the username `admin` and password `admin`.
6. Add Prometheus as a data source:
   - Set the Prometheus server URL to `http://prometheus:9090`.
7. Click `Create your first dashboard`.
8. Select `Import`.
9. Enter the dashboard ID `12904`.
10. Choose `Promxy` as your Prometheus instance.

## Additional Notes

- Ensure that your Kubernetes cluster and Docker environment are properly configured before starting the setup.
- For further details on Vault configuration and Locust setup, refer to their respective official documentation.
