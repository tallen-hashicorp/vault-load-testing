# Enterprise vs. OSS Basic Test

In this test, I performed a basic benchmark to compare the performance of different versions of Vault, focusing on both the Enterprise and Open Source (OSS) editions. The benchmark involved 50% AppRole logins and 50% static secret writes, simulating a mix of typical operations. While the test doesn't fully replicate a production environment, it offers a rough estimate of the throughput differences between the versions. The tests were conducted on a local laptop running a 3-node Vault cluster using the Raft storage backend, providing insights into performance under controlled conditions.

## How to Run

```bash
export VAULT_TOKEN=""
vault-benchmark run -config=vault-benchmark/basic.hcl
```

## Results

### Vault Enterprise 1.16.7

| Operation              | Count | Rate (ops/sec) | Throughput (ops/sec) | Mean Latency | 95th Percentile Latency | 99th Percentile Latency | Success Ratio |
|------------------------|-------|----------------|----------------------|--------------|------------------------|------------------------|---------------|
| AppRole Logins         | 5166  | 172.18         | 172.06               | 30.56 ms     | 50.31 ms               | 65.32 ms               | 100.00%       |
| Static Secret Writes   | 4905  | 163.56         | 163.42               | 28.98 ms     | 51.09 ms               | 67.79 ms               | 100.00%       |

### Vault OSS 1.16

| Operation              | Count | Rate (ops/sec) | Throughput (ops/sec) | Mean Latency | 95th Percentile Latency | 99th Percentile Latency | Success Ratio |
|------------------------|-------|----------------|----------------------|--------------|------------------------|------------------------|---------------|
| AppRole Logins         | 4477  | 149.23         | 149.14               | 34.94 ms     | 53.41 ms               | 69.67 ms               | 100.00%       |
| Static Secret Writes   | 4447  | 148.26         | 148.15               | 32.28 ms     | 55.04 ms               | 71.72 ms               | 100.00%       |

### Vault Enterprise 1.13.13

| Operation              | Count | Rate (ops/sec) | Throughput (ops/sec) | Mean Latency | 95th Percentile Latency | 99th Percentile Latency | Success Ratio |
|------------------------|-------|----------------|----------------------|--------------|------------------------|------------------------|---------------|
| AppRole Logins         | 2188  | 72.96          | 72.80                | 69.95 ms     | 86.75 ms               | 110.11 ms              | 100.00%       |
| Static Secret Writes   | 2209  | 73.63          | 73.47                | 66.64 ms     | 81.78 ms               | 99.59 ms               | 100.00%       |

## Conclusion

From the results, we can observe the following trends:

1. **Performance Comparison**:
   - **Enterprise 1.16.7** shows the best performance among the versions tested, with the highest operation rates and the lowest latencies.
   - **OSS 1.16** performs slightly worse than Enterprise 1.16.7, with lower throughput and higher latencies, though it still maintains strong performance.
   - **Enterprise 1.13.13** has significantly lower performance compared to both 1.16 versions, with approximately half the operation rate and higher latencies.

2. **Version Impact**:
   - Upgrading from **Enterprise 1.13.13** to **1.16.7** provides a substantial performance boost, highlighting the optimizations and improvements made in newer versions.
   - The **Enterprise** version consistently outperforms the **OSS** version of the same release, indicating additional performance enhancements available in the enterprise edition.