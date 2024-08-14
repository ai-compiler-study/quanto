# Experiment Results

## Sd3 - Batch Size: 1, Data Type: bf16

<table>
<tr>
<td><img src='http://localhost:8000/experiment_results/ckpt@sd3-bs@1-dtype@bf16-qtype@int8-qte@0-fuse@1.png' alt='qtype: int8, qte: 0, fuse: 1' width='300'/><br>qtype: int8, qte: 0, fuse: 1</td>
<td><img src='http://localhost:8000/experiment_results/ckpt@sd3-bs@1-dtype@bf16-qtype@fp8-qte@0-fuse@1.png' alt='qtype: fp8, qte: 0, fuse: 1' width='300'/><br>qtype: fp8, qte: 0, fuse: 1</td>
<td><img src='http://localhost:8000/experiment_results/ckpt@sd3-bs@1-dtype@bf16-qtype@int8-qte@1-fuse@1.png' alt='qtype: int8, qte: 1, fuse: 1' width='300'/><br>qtype: int8, qte: 1, fuse: 1</td>
</tr>
<tr>
<td><img src='http://localhost:8000/experiment_results/ckpt@sd3-bs@1-dtype@bf16-qtype@int8-qte@1-fuse@0.png' alt='qtype: int8, qte: 1, fuse: 0' width='300'/><br>qtype: int8, qte: 1, fuse: 0</td>
<td><img src='http://localhost:8000/experiment_results/ckpt@sd3-bs@1-dtype@bf16-qtype@fp8-qte@0-fuse@0.png' alt='qtype: fp8, qte: 0, fuse: 0' width='300'/><br>qtype: fp8, qte: 0, fuse: 0</td>
<td><img src='http://localhost:8000/experiment_results/ckpt@sd3-bs@1-dtype@bf16-qtype@int8-qte@0-fuse@0.png' alt='qtype: int8, qte: 0, fuse: 0' width='300'/><br>qtype: int8, qte: 0, fuse: 0</td>
</tr>
<tr>
<td><img src='http://localhost:8000/experiment_results/ckpt@sd3-bs@1-dtype@bf16-qtype@fp8-qte@1-fuse@1.png' alt='qtype: fp8, qte: 1, fuse: 1' width='300'/><br>qtype: fp8, qte: 1, fuse: 1</td>
<td><img src='http://localhost:8000/experiment_results/ckpt@sd3-bs@1-dtype@bf16-qtype@none-qte@1-fuse@1.png' alt='qtype: none, qte: 1, fuse: 1' width='300'/><br>qtype: none, qte: 1, fuse: 1</td>
<td><img src='http://localhost:8000/experiment_results/ckpt@sd3-bs@1-dtype@bf16-qtype@fp8-qte@1-fuse@0.png' alt='qtype: fp8, qte: 1, fuse: 0' width='300'/><br>qtype: fp8, qte: 1, fuse: 0</td>
</tr>
<tr>
<td><img src='http://localhost:8000/experiment_results/ckpt@sd3-bs@1-dtype@bf16-qtype@none-qte@1-fuse@0.png' alt='qtype: none, qte: 1, fuse: 0' width='300'/><br>qtype: none, qte: 1, fuse: 0</td>
<td><img src='http://localhost:8000/experiment_results/ckpt@sd3-bs@1-dtype@bf16-qtype@none-qte@0-fuse@1.png' alt='qtype: none, qte: 0, fuse: 1' width='300'/><br>qtype: none, qte: 0, fuse: 1</td>
<td><img src='http://localhost:8000/experiment_results/ckpt@sd3-bs@1-dtype@bf16-qtype@none-qte@0-fuse@0.png' alt='qtype: none, qte: 0, fuse: 0' width='300'/><br>qtype: none, qte: 0, fuse: 0</td>
</tr>
</table>

### Sorted by Memory Usage (Ascending)

| Quantization | Quantize TE | Fuse QKV | Memory (GB) | Latency (s) |
|--------------|-------------|----------|-------------|-------------|
| FP8          | Yes         | No       | 7.628       | 2.659       |
| INT8         | Yes         | No       | 7.628       | 2.531       |
| INT8         | Yes         | Yes      | 7.963       | 2.527       |
| FP8          | Yes         | Yes      | 7.968       | 2.637       |
| INT8         | No          | No       | 12.598      | 2.475       |
| FP8          | No          | No       | 12.598      | 2.598       |
| FP8          | No          | Yes      | 12.926      | 2.574       |
| INT8         | No          | Yes      | 12.929      | 2.458       |
| NONE         | No          | No       | 14.526      | 1.998       |
| NONE         | Yes         | No       | 14.526      | 2.000       |
| NONE         | No          | Yes      | 15.183      | 2.000       |
| NONE         | Yes         | Yes      | 15.183      | 2.003       |

### Sorted by Latency (Ascending)

| Quantization | Quantize TE | Fuse QKV | Memory (GB) | Latency (s) |
|--------------|-------------|----------|-------------|-------------|
| NONE         | No          | No       | 14.526      | 1.998       |
| NONE         | Yes         | No       | 14.526      | 2.000       |
| NONE         | No          | Yes      | 15.183      | 2.000       |
| NONE         | Yes         | Yes      | 15.183      | 2.003       |
| INT8         | No          | Yes      | 12.929      | 2.458       |
| INT8         | No          | No       | 12.598      | 2.475       |
| INT8         | Yes         | Yes      | 7.963       | 2.527       |
| INT8         | Yes         | No       | 7.628       | 2.531       |
| FP8          | No          | Yes      | 12.926      | 2.574       |
| FP8          | No          | No       | 12.598      | 2.598       |
| FP8          | Yes         | Yes      | 7.968       | 2.637       |
| FP8          | Yes         | No       | 7.628       | 2.659       |


## Sd3 - Batch Size: 1, Data Type: fp16

<table>
<tr>
<td><img src='http://localhost:8000/experiment_results/ckpt@sd3-bs@1-dtype@fp16-qtype@int8-qte@0-fuse@0.png' alt='qtype: int8, qte: 0, fuse: 0' width='300'/><br>qtype: int8, qte: 0, fuse: 0</td>
<td><img src='http://localhost:8000/experiment_results/ckpt@sd3-bs@1-dtype@fp16-qtype@int8-qte@1-fuse@1.png' alt='qtype: int8, qte: 1, fuse: 1' width='300'/><br>qtype: int8, qte: 1, fuse: 1</td>
<td><img src='http://localhost:8000/experiment_results/ckpt@sd3-bs@1-dtype@fp16-qtype@none-qte@1-fuse@0.png' alt='qtype: none, qte: 1, fuse: 0' width='300'/><br>qtype: none, qte: 1, fuse: 0</td>
</tr>
<tr>
<td><img src='http://localhost:8000/experiment_results/ckpt@sd3-bs@1-dtype@fp16-qtype@none-qte@0-fuse@0.png' alt='qtype: none, qte: 0, fuse: 0' width='300'/><br>qtype: none, qte: 0, fuse: 0</td>
<td><img src='http://localhost:8000/experiment_results/ckpt@sd3-bs@1-dtype@fp16-qtype@none-qte@1-fuse@1.png' alt='qtype: none, qte: 1, fuse: 1' width='300'/><br>qtype: none, qte: 1, fuse: 1</td>
<td><img src='http://localhost:8000/experiment_results/ckpt@sd3-bs@1-dtype@fp16-qtype@fp8-qte@0-fuse@0.png' alt='qtype: fp8, qte: 0, fuse: 0' width='300'/><br>qtype: fp8, qte: 0, fuse: 0</td>
</tr>
<tr>
<td><img src='http://localhost:8000/experiment_results/ckpt@sd3-bs@1-dtype@fp16-qtype@none-qte@0-fuse@1.png' alt='qtype: none, qte: 0, fuse: 1' width='300'/><br>qtype: none, qte: 0, fuse: 1</td>
<td><img src='http://localhost:8000/experiment_results/ckpt@sd3-bs@1-dtype@fp16-qtype@fp8-qte@1-fuse@0.png' alt='qtype: fp8, qte: 1, fuse: 0' width='300'/><br>qtype: fp8, qte: 1, fuse: 0</td>
<td><img src='http://localhost:8000/experiment_results/ckpt@sd3-bs@1-dtype@fp16-qtype@int8-qte@0-fuse@1.png' alt='qtype: int8, qte: 0, fuse: 1' width='300'/><br>qtype: int8, qte: 0, fuse: 1</td>
</tr>
<tr>
<td><img src='http://localhost:8000/experiment_results/ckpt@sd3-bs@1-dtype@fp16-qtype@fp8-qte@0-fuse@1.png' alt='qtype: fp8, qte: 0, fuse: 1' width='300'/><br>qtype: fp8, qte: 0, fuse: 1</td>
<td><img src='http://localhost:8000/experiment_results/ckpt@sd3-bs@1-dtype@fp16-qtype@int8-qte@1-fuse@0.png' alt='qtype: int8, qte: 1, fuse: 0' width='300'/><br>qtype: int8, qte: 1, fuse: 0</td>
<td><img src='http://localhost:8000/experiment_results/ckpt@sd3-bs@1-dtype@fp16-qtype@fp8-qte@1-fuse@1.png' alt='qtype: fp8, qte: 1, fuse: 1' width='300'/><br>qtype: fp8, qte: 1, fuse: 1</td>
</tr>
</table>

### Sorted by Memory Usage (Ascending)

| Quantization | Quantize TE | Fuse QKV | Memory (GB) | Latency (s) |
|--------------|-------------|----------|-------------|-------------|
| INT8         | Yes         | No       | 7.625       | 2.553       |
| FP8          | Yes         | No       | 7.630       | 2.682       |
| INT8         | Yes         | Yes      | 7.963       | 2.517       |
| FP8          | Yes         | Yes      | 7.963       | 2.628       |
| FP8          | No          | No       | 14.469      | 2.630       |
| INT8         | No          | No       | 14.473      | 2.499       |
| INT8         | No          | Yes      | 14.804      | 2.464       |
| FP8          | No          | Yes      | 14.838      | 2.571       |
| NONE         | No          | No       | 16.397      | 2.046       |
| NONE         | Yes         | No       | 16.403      | 2.053       |
| NONE         | Yes         | Yes      | 17.058      | 2.054       |
| NONE         | No          | Yes      | 17.058      | 2.051       |

### Sorted by Latency (Ascending)

| Quantization | Quantize TE | Fuse QKV | Memory (GB) | Latency (s) |
|--------------|-------------|----------|-------------|-------------|
| NONE         | No          | No       | 16.397      | 2.046       |
| NONE         | No          | Yes      | 17.058      | 2.051       |
| NONE         | Yes         | No       | 16.403      | 2.053       |
| NONE         | Yes         | Yes      | 17.058      | 2.054       |
| INT8         | No          | Yes      | 14.804      | 2.464       |
| INT8         | No          | No       | 14.473      | 2.499       |
| INT8         | Yes         | Yes      | 7.963       | 2.517       |
| INT8         | Yes         | No       | 7.625       | 2.553       |
| FP8          | No          | Yes      | 14.838      | 2.571       |
| FP8          | Yes         | Yes      | 7.963       | 2.628       |
| FP8          | No          | No       | 14.469      | 2.630       |
| FP8          | Yes         | No       | 7.630       | 2.682       |


## Pixart - Batch Size: 1, Data Type: bf16

<table>
<tr>
<td><img src='http://localhost:8000/experiment_results/ckpt@pixart-bs@1-dtype@bf16-qtype@int4-qte@1-fuse@0.png' alt='qtype: int4, qte: 1, fuse: 0' width='300'/><br>qtype: int4, qte: 1, fuse: 0</td>
<td><img src='http://localhost:8000/experiment_results/ckpt@pixart-bs@1-dtype@bf16-qtype@int4-qte@0-fuse@1.png' alt='qtype: int4, qte: 0, fuse: 1' width='300'/><br>qtype: int4, qte: 0, fuse: 1</td>
<td><img src='http://localhost:8000/experiment_results/ckpt@pixart-bs@1-dtype@bf16-qtype@fp8-qte@1-fuse@1.png' alt='qtype: fp8, qte: 1, fuse: 1' width='300'/><br>qtype: fp8, qte: 1, fuse: 1</td>
</tr>
<tr>
<td><img src='http://localhost:8000/experiment_results/ckpt@pixart-bs@1-dtype@bf16-qtype@fp8-qte@1-fuse@0.png' alt='qtype: fp8, qte: 1, fuse: 0' width='300'/><br>qtype: fp8, qte: 1, fuse: 0</td>
<td><img src='http://localhost:8000/experiment_results/ckpt@pixart-bs@1-dtype@bf16-qtype@fp8-qte@0-fuse@1.png' alt='qtype: fp8, qte: 0, fuse: 1' width='300'/><br>qtype: fp8, qte: 0, fuse: 1</td>
<td><img src='http://localhost:8000/experiment_results/ckpt@pixart-bs@1-dtype@bf16-qtype@int8-qte@0-fuse@1.png' alt='qtype: int8, qte: 0, fuse: 1' width='300'/><br>qtype: int8, qte: 0, fuse: 1</td>
</tr>
<tr>
<td><img src='http://localhost:8000/experiment_results/ckpt@pixart-bs@1-dtype@bf16-qtype@int8-qte@0-fuse@0.png' alt='qtype: int8, qte: 0, fuse: 0' width='300'/><br>qtype: int8, qte: 0, fuse: 0</td>
<td><img src='http://localhost:8000/experiment_results/ckpt@pixart-bs@1-dtype@bf16-qtype@int8-qte@1-fuse@1.png' alt='qtype: int8, qte: 1, fuse: 1' width='300'/><br>qtype: int8, qte: 1, fuse: 1</td>
<td><img src='http://localhost:8000/experiment_results/ckpt@pixart-bs@1-dtype@bf16-qtype@none-qte@0-fuse@1.png' alt='qtype: none, qte: 0, fuse: 1' width='300'/><br>qtype: none, qte: 0, fuse: 1</td>
</tr>
<tr>
<td><img src='http://localhost:8000/experiment_results/ckpt@pixart-bs@1-dtype@bf16-qtype@int8-qte@1-fuse@0.png' alt='qtype: int8, qte: 1, fuse: 0' width='300'/><br>qtype: int8, qte: 1, fuse: 0</td>
<td><img src='http://localhost:8000/experiment_results/ckpt@pixart-bs@1-dtype@bf16-qtype@fp8-qte@0-fuse@0.png' alt='qtype: fp8, qte: 0, fuse: 0' width='300'/><br>qtype: fp8, qte: 0, fuse: 0</td>
<td><img src='http://localhost:8000/experiment_results/ckpt@pixart-bs@1-dtype@bf16-qtype@int4-qte@1-fuse@1.png' alt='qtype: int4, qte: 1, fuse: 1' width='300'/><br>qtype: int4, qte: 1, fuse: 1</td>
</tr>
<tr>
<td><img src='http://localhost:8000/experiment_results/ckpt@pixart-bs@1-dtype@bf16-qtype@none-qte@1-fuse@0.png' alt='qtype: none, qte: 1, fuse: 0' width='300'/><br>qtype: none, qte: 1, fuse: 0</td>
<td><img src='http://localhost:8000/experiment_results/ckpt@pixart-bs@1-dtype@bf16-qtype@none-qte@1-fuse@1.png' alt='qtype: none, qte: 1, fuse: 1' width='300'/><br>qtype: none, qte: 1, fuse: 1</td>
<td><img src='http://localhost:8000/experiment_results/ckpt@pixart-bs@1-dtype@bf16-qtype@none-qte@0-fuse@0.png' alt='qtype: none, qte: 0, fuse: 0' width='300'/><br>qtype: none, qte: 0, fuse: 0</td>
</tr>
<tr>
<td><img src='http://localhost:8000/experiment_results/ckpt@pixart-bs@1-dtype@bf16-qtype@int4-qte@0-fuse@0.png' alt='qtype: int4, qte: 0, fuse: 0' width='300'/><br>qtype: int4, qte: 0, fuse: 0</td>
</tr>
</table>

### Sorted by Memory Usage (Ascending)

| Quantization | Quantize TE | Fuse QKV | Memory (GB) | Latency (s) |
|--------------|-------------|----------|-------------|-------------|
| INT4         | Yes         | No       | 3.066       | 7.493       |
| INT4         | Yes         | Yes      | 3.176       | 7.512       |
| INT8         | Yes         | No       | 5.364       | 1.429       |
| FP8          | Yes         | No       | 5.365       | 1.475       |
| FP8          | Yes         | Yes      | 5.537       | 1.450       |
| INT8         | Yes         | Yes      | 5.537       | 1.403       |
| INT4         | No          | No       | 9.380       | 7.320       |
| INT4         | No          | Yes      | 9.491       | 7.340       |
| FP8          | No          | No       | 9.672       | 1.434       |
| INT8         | No          | No       | 9.672       | 1.400       |
| FP8          | No          | Yes      | 9.847       | 1.397       |
| INT8         | No          | Yes      | 9.847       | 1.375       |
| NONE         | No          | No       | 10.214      | 1.152       |
| NONE         | Yes         | No       | 10.214      | 1.151       |
| NONE         | No          | Yes      | 10.560      | 1.142       |
| NONE         | Yes         | Yes      | 10.560      | 1.142       |

### Sorted by Latency (Ascending)

| Quantization | Quantize TE | Fuse QKV | Memory (GB) | Latency (s) |
|--------------|-------------|----------|-------------|-------------|
| NONE         | No          | Yes      | 10.560      | 1.142       |
| NONE         | Yes         | Yes      | 10.560      | 1.142       |
| NONE         | Yes         | No       | 10.214      | 1.151       |
| NONE         | No          | No       | 10.214      | 1.152       |
| INT8         | No          | Yes      | 9.847       | 1.375       |
| FP8          | No          | Yes      | 9.847       | 1.397       |
| INT8         | No          | No       | 9.672       | 1.400       |
| INT8         | Yes         | Yes      | 5.537       | 1.403       |
| INT8         | Yes         | No       | 5.364       | 1.429       |
| FP8          | No          | No       | 9.672       | 1.434       |
| FP8          | Yes         | Yes      | 5.537       | 1.450       |
| FP8          | Yes         | No       | 5.365       | 1.475       |
| INT4         | No          | No       | 9.380       | 7.320       |
| INT4         | No          | Yes      | 9.491       | 7.340       |
| INT4         | Yes         | No       | 3.066       | 7.493       |
| INT4         | Yes         | Yes      | 3.176       | 7.512       |


## Pixart - Batch Size: 1, Data Type: fp16

<table>
<tr>
<td><img src='http://localhost:8000/experiment_results/ckpt@pixart-bs@1-dtype@fp16-qtype@fp8-qte@0-fuse@0.png' alt='qtype: fp8, qte: 0, fuse: 0' width='300'/><br>qtype: fp8, qte: 0, fuse: 0</td>
<td><img src='http://localhost:8000/experiment_results/ckpt@pixart-bs@1-dtype@fp16-qtype@none-qte@0-fuse@1.png' alt='qtype: none, qte: 0, fuse: 1' width='300'/><br>qtype: none, qte: 0, fuse: 1</td>
<td><img src='http://localhost:8000/experiment_results/ckpt@pixart-bs@1-dtype@fp16-qtype@fp8-qte@1-fuse@1.png' alt='qtype: fp8, qte: 1, fuse: 1' width='300'/><br>qtype: fp8, qte: 1, fuse: 1</td>
</tr>
<tr>
<td><img src='http://localhost:8000/experiment_results/ckpt@pixart-bs@1-dtype@fp16-qtype@int8-qte@1-fuse@0.png' alt='qtype: int8, qte: 1, fuse: 0' width='300'/><br>qtype: int8, qte: 1, fuse: 0</td>
<td><img src='http://localhost:8000/experiment_results/ckpt@pixart-bs@1-dtype@fp16-qtype@none-qte@1-fuse@0.png' alt='qtype: none, qte: 1, fuse: 0' width='300'/><br>qtype: none, qte: 1, fuse: 0</td>
<td><img src='http://localhost:8000/experiment_results/ckpt@pixart-bs@1-dtype@fp16-qtype@int8-qte@1-fuse@1.png' alt='qtype: int8, qte: 1, fuse: 1' width='300'/><br>qtype: int8, qte: 1, fuse: 1</td>
</tr>
<tr>
<td><img src='http://localhost:8000/experiment_results/ckpt@pixart-bs@1-dtype@fp16-qtype@int8-qte@0-fuse@0.png' alt='qtype: int8, qte: 0, fuse: 0' width='300'/><br>qtype: int8, qte: 0, fuse: 0</td>
<td><img src='http://localhost:8000/experiment_results/ckpt@pixart-bs@1-dtype@fp16-qtype@fp8-qte@0-fuse@1.png' alt='qtype: fp8, qte: 0, fuse: 1' width='300'/><br>qtype: fp8, qte: 0, fuse: 1</td>
<td><img src='http://localhost:8000/experiment_results/ckpt@pixart-bs@1-dtype@fp16-qtype@int8-qte@0-fuse@1.png' alt='qtype: int8, qte: 0, fuse: 1' width='300'/><br>qtype: int8, qte: 0, fuse: 1</td>
</tr>
<tr>
<td><img src='http://localhost:8000/experiment_results/ckpt@pixart-bs@1-dtype@fp16-qtype@none-qte@0-fuse@0.png' alt='qtype: none, qte: 0, fuse: 0' width='300'/><br>qtype: none, qte: 0, fuse: 0</td>
<td><img src='http://localhost:8000/experiment_results/ckpt@pixart-bs@1-dtype@fp16-qtype@fp8-qte@1-fuse@0.png' alt='qtype: fp8, qte: 1, fuse: 0' width='300'/><br>qtype: fp8, qte: 1, fuse: 0</td>
<td><img src='http://localhost:8000/experiment_results/ckpt@pixart-bs@1-dtype@fp16-qtype@none-qte@1-fuse@1.png' alt='qtype: none, qte: 1, fuse: 1' width='300'/><br>qtype: none, qte: 1, fuse: 1</td>
</tr>
</table>

### Sorted by Memory Usage (Ascending)

| Quantization | Quantize TE | Fuse QKV | Memory (GB) | Latency (s) |
|--------------|-------------|----------|-------------|-------------|
| INT8         | Yes         | No       | 5.363       | 1.526       |
| FP8          | Yes         | No       | 5.364       | 1.587       |
| INT8         | Yes         | Yes      | 5.537       | 1.471       |
| FP8          | Yes         | Yes      | 5.537       | 1.518       |
| INT8         | No          | No       | 11.547      | 1.494       |
| FP8          | No          | No       | 11.547      | 1.520       |
| INT8         | No          | Yes      | 11.722      | 1.439       |
| FP8          | No          | Yes      | 11.722      | 1.472       |
| NONE         | No          | No       | 12.086      | 1.182       |
| NONE         | Yes         | No       | 12.086      | 1.181       |
| NONE         | No          | Yes      | 12.433      | 1.172       |
| NONE         | Yes         | Yes      | 12.435      | 1.170       |

### Sorted by Latency (Ascending)

| Quantization | Quantize TE | Fuse QKV | Memory (GB) | Latency (s) |
|--------------|-------------|----------|-------------|-------------|
| NONE         | Yes         | Yes      | 12.435      | 1.170       |
| NONE         | No          | Yes      | 12.433      | 1.172       |
| NONE         | Yes         | No       | 12.086      | 1.181       |
| NONE         | No          | No       | 12.086      | 1.182       |
| INT8         | No          | Yes      | 11.722      | 1.439       |
| INT8         | Yes         | Yes      | 5.537       | 1.471       |
| FP8          | No          | Yes      | 11.722      | 1.472       |
| INT8         | No          | No       | 11.547      | 1.494       |
| FP8          | Yes         | Yes      | 5.537       | 1.518       |
| FP8          | No          | No       | 11.547      | 1.520       |
| INT8         | Yes         | No       | 5.363       | 1.526       |
| FP8          | Yes         | No       | 5.364       | 1.587       |


## Flux-dev - Batch Size: 1, Data Type: fp16

<table>
<tr>
<td><img src='http://localhost:8000/experiment_results/ckpt@flux-dev-bs@1-dtype@fp16-qtype@none-qte@0-fuse@0.png' alt='qtype: none, qte: 0, fuse: 0' width='300'/><br>qtype: none, qte: 0, fuse: 0</td>
<td><img src='http://localhost:8000/experiment_results/ckpt@flux-dev-bs@1-dtype@fp16-qtype@none-qte@1-fuse@0.png' alt='qtype: none, qte: 1, fuse: 0' width='300'/><br>qtype: none, qte: 1, fuse: 0</td>
<td><img src='http://localhost:8000/experiment_results/ckpt@flux-dev-bs@1-dtype@fp16-qtype@int8-qte@1-fuse@0.png' alt='qtype: int8, qte: 1, fuse: 0' width='300'/><br>qtype: int8, qte: 1, fuse: 0</td>
</tr>
<tr>
<td><img src='http://localhost:8000/experiment_results/ckpt@flux-dev-bs@1-dtype@fp16-qtype@int8-qte@0-fuse@0.png' alt='qtype: int8, qte: 0, fuse: 0' width='300'/><br>qtype: int8, qte: 0, fuse: 0</td>
<td><img src='http://localhost:8000/experiment_results/ckpt@flux-dev-bs@1-dtype@fp16-qtype@fp8-qte@0-fuse@0.png' alt='qtype: fp8, qte: 0, fuse: 0' width='300'/><br>qtype: fp8, qte: 0, fuse: 0</td>
<td><img src='http://localhost:8000/experiment_results/ckpt@flux-dev-bs@1-dtype@fp16-qtype@fp8-qte@1-fuse@0.png' alt='qtype: fp8, qte: 1, fuse: 0' width='300'/><br>qtype: fp8, qte: 1, fuse: 0</td>
</tr>
</table>

### Sorted by Memory Usage (Ascending)

| Quantization | Quantize TE | Fuse QKV | Memory (GB) | Latency (s) |
|--------------|-------------|----------|-------------|-------------|
| FP8          | Yes         | No       | 15.998      | 9.067       |
| INT8         | Yes         | No       | 15.999      | 8.435       |
| INT8         | No          | No       | 22.270      | 8.400       |
| FP8          | No          | No       | 22.271      | 9.013       |
| NONE         | No          | No       | 33.345      | 6.657       |
| NONE         | Yes         | No       | 33.345      | 6.672       |

### Sorted by Latency (Ascending)

| Quantization | Quantize TE | Fuse QKV | Memory (GB) | Latency (s) |
|--------------|-------------|----------|-------------|-------------|
| NONE         | No          | No       | 33.345      | 6.657       |
| NONE         | Yes         | No       | 33.345      | 6.672       |
| INT8         | No          | No       | 22.270      | 8.400       |
| INT8         | Yes         | No       | 15.999      | 8.435       |
| FP8          | No          | No       | 22.271      | 9.013       |
| FP8          | Yes         | No       | 15.998      | 9.067       |


## Flux-dev - Batch Size: 1, Data Type: bf16

<table>
<tr>
<td><img src='http://localhost:8000/experiment_results/ckpt@flux-dev-bs@1-dtype@bf16-qtype@fp8-qte@1-fuse@0.png' alt='qtype: fp8, qte: 1, fuse: 0' width='300'/><br>qtype: fp8, qte: 1, fuse: 0</td>
<td><img src='http://localhost:8000/experiment_results/ckpt@flux-dev-bs@1-dtype@bf16-qtype@int4-qte@0-fuse@0.png' alt='qtype: int4, qte: 0, fuse: 0' width='300'/><br>qtype: int4, qte: 0, fuse: 0</td>
<td><img src='http://localhost:8000/experiment_results/ckpt@flux-dev-bs@1-dtype@bf16-qtype@int8-qte@0-fuse@0.png' alt='qtype: int8, qte: 0, fuse: 0' width='300'/><br>qtype: int8, qte: 0, fuse: 0</td>
</tr>
<tr>
<td><img src='http://localhost:8000/experiment_results/ckpt@flux-dev-bs@1-dtype@bf16-qtype@fp8-qte@0-fuse@0.png' alt='qtype: fp8, qte: 0, fuse: 0' width='300'/><br>qtype: fp8, qte: 0, fuse: 0</td>
<td><img src='http://localhost:8000/experiment_results/ckpt@flux-dev-bs@1-dtype@bf16-qtype@int8-qte@1-fuse@0.png' alt='qtype: int8, qte: 1, fuse: 0' width='300'/><br>qtype: int8, qte: 1, fuse: 0</td>
</tr>
</table>

### Sorted by Memory Usage (Ascending)

| Quantization | Quantize TE | Fuse QKV | Memory (GB) | Latency (s) |
|--------------|-------------|----------|-------------|-------------|
| INT4         | No          | No       | 15.234      | 62.075      |
| FP8          | Yes         | No       | 15.997      | 8.994       |
| INT8         | Yes         | No       | 15.999      | 8.420       |
| FP8          | No          | No       | 20.393      | 8.963       |
| INT8         | No          | No       | 20.395      | 8.372       |

### Sorted by Latency (Ascending)

| Quantization | Quantize TE | Fuse QKV | Memory (GB) | Latency (s) |
|--------------|-------------|----------|-------------|-------------|
| INT8         | No          | No       | 20.395      | 8.372       |
| INT8         | Yes         | No       | 15.999      | 8.420       |
| FP8          | No          | No       | 20.393      | 8.963       |
| FP8          | Yes         | No       | 15.997      | 8.994       |
| INT4         | No          | No       | 15.234      | 62.075      |


