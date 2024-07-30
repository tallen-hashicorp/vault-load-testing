from locust import HttpUser, between, task
import os

vault_token = os.getenv('VAULT_TOKEN')

class WriteSecret(HttpUser):
    wait_time = between(1, 5)
    
    def on_start(self):
        self.client.post(url="/v1/sys/mounts/locust-load-test", 
                         headers={"X-Vault-Token": vault_token},
                         json={"type": "kv", "options": {"version": "2"}})
        
        self.client.post(url="/v1/locust-load-test/data/some-key", 
                         headers={"X-Vault-Token": vault_token},
                         json={"data": {"hello": "world"}})
        
    @task
    def write_secret(self):
        self.client.post(url="/v1/locust-load-test/data/some-key", 
                         headers={"X-Vault-Token": vault_token},
                         json={"data": {"hello": "world"}})
    
    @task(100)
    def read_secret(self):
        for item_id in range(50):
            self.client.get(url="/v1/locust-load-test/data/some-key", 
                         headers={"X-Vault-Token": vault_token})