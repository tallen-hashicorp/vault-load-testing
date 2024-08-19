# Basic Benchmark config options
vault_addr = "http://127.0.0.1:8200"
vault_namespace="root"
duration = "60s"
cleanup = true

test "approle_auth" "approle_logins" {
  weight = 20
  config {
    role {
      role_name = "benchmark-role"
      token_ttl="2m"
    }
  }
}

test "kvv2_write" "static_secret_writes" {
  weight = 10
  config {
    numkvs = 100
    kvsize = 100
  }
}

test "pki_issue" "pki_issue_test1" {
  weight = 10
  config {
      setup_delay="2s"
      root_ca {
        common_name = "benchmark.test"
      }
      intermediate_csr {
        common_name = "benchmark.test Intermediate Authority"
      }
      role {
        ttl = "10m"
        key_type = "ed25519"
      }
  }
}

test "transit_sign" "transit_sign_test_1" {
    weight = 10
}

test "transit_verify" "transit_verify_test_1" {
    weight = 10
    config {
        verify {
            signature_algorithm = "pkcs1v15"
        }
    }
}

test "transit_encrypt" "transit_encrypt_test_1" {
    weight = 10
    config {
      payload_len = 128
      context_len = 32
      keys {
        convergent_encryption = true
        derived = true
        type = "aes128-gcm96"
      }
    }
}

test "transit_decrypt" "transit_decrypt_test_1" {
    weight = 10
    config {
        payload_len = 64
    }
}

test "userpass_auth" "userpass_test1" {
    weight = 20
    config {
        username = "test-user"
        password = "password"
    }
}