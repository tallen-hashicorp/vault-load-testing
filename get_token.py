from locust import HttpUser, between, task
import os

vault_token = os.getenv('VAULT_TOKEN')

class WriteSecret(HttpUser):
    @task
    def create_token(self):
        self.client.post(url="/v1/auth/token/create", 
                         headers={"X-Vault-Token": vault_token},
                         json={"ttl": "1h"})
        
    
    @task
    def create_orphan_token(self):
        self.client.post(url="/v1/auth/token/create-orphan", 
                         headers={"X-Vault-Token": vault_token},
                         json={"ttl": "1h"})
    
    @task
    def create_batch_token(self):
        self.client.post(url="/v1/auth/token/create", 
                         headers={"X-Vault-Token": vault_token},
                         json={"policies":["test"],"ttl":"20m0s","explicit_max_ttl":"0s","period":"0s","display_name":"","num_uses":0,"renewable":"false","type":"batch","entity_alias":""})