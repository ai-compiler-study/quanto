# Experiment Results

## Table 1 (Sorted by Memory)

| Model Name | Batch Size | Quantization | Quantize TE | Memory (GB) | Latency (Seconds) |
| --- | --- | --- | --- | --- | --- |
| pixart | 1 | INT4 | True | 3.066 | 7.493 |
| pixart | 1 | INT4 | True | 3.176 | 7.512 |
| pixart | 1 | INT8 | True | 5.363 | 1.526 |
| pixart | 1 | INT8 | True | 5.364 | 1.429 |
| pixart | 1 | FP8 | True | 5.364 | 1.587 |
| pixart | 1 | FP8 | True | 5.365 | 1.475 |
| pixart | 1 | INT8 | True | 5.537 | 1.471 |
| pixart | 1 | FP8 | True | 5.537 | 1.518 |
| pixart | 1 | FP8 | True | 5.537 | 1.450 |
| pixart | 1 | INT8 | True | 5.537 | 1.403 |
| sd3 | 1 | INT8 | True | 7.625 | 2.553 |
| sd3 | 1 | FP8 | True | 7.628 | 2.659 |
| sd3 | 1 | INT8 | True | 7.628 | 2.531 |
| sd3 | 1 | FP8 | True | 7.630 | 2.682 |
| sd3 | 1 | INT8 | True | 7.963 | 2.527 |
| sd3 | 1 | INT8 | True | 7.963 | 2.517 |
| sd3 | 1 | FP8 | True | 7.963 | 2.628 |
| sd3 | 1 | FP8 | True | 7.968 | 2.637 |
| pixart | 1 | INT4 | False | 9.380 | 7.320 |
| pixart | 1 | INT4 | False | 9.491 | 7.340 |
| pixart | 1 | FP8 | False | 9.672 | 1.434 |
| pixart | 1 | INT8 | False | 9.672 | 1.400 |
| pixart | 1 | FP8 | False | 9.847 | 1.397 |
| pixart | 1 | INT8 | False | 9.847 | 1.375 |
| pixart | 1 | NONE | False | 10.214 | 1.152 |
| pixart | 1 | NONE | True | 10.214 | 1.151 |
| pixart | 1 | NONE | False | 10.560 | 1.142 |
| pixart | 1 | NONE | True | 10.560 | 1.142 |
| pixart | 1 | INT8 | False | 11.547 | 1.494 |
| pixart | 1 | FP8 | False | 11.547 | 1.520 |
| pixart | 1 | INT8 | False | 11.722 | 1.439 |
| pixart | 1 | FP8 | False | 11.722 | 1.472 |
| pixart | 1 | NONE | False | 12.086 | 1.182 |
| pixart | 1 | NONE | True | 12.086 | 1.181 |
| pixart | 1 | NONE | False | 12.433 | 1.172 |
| pixart | 1 | NONE | True | 12.435 | 1.170 |
| sd3 | 1 | INT8 | False | 12.598 | 2.475 |
| sd3 | 1 | FP8 | False | 12.598 | 2.598 |
| sd3 | 1 | FP8 | False | 12.926 | 2.574 |
| sd3 | 1 | INT8 | False | 12.929 | 2.458 |
| sd3 | 1 | FP8 | False | 14.469 | 2.630 |
| sd3 | 1 | INT8 | False | 14.473 | 2.499 |
| sd3 | 1 | NONE | False | 14.526 | 1.998 |
| sd3 | 1 | NONE | True | 14.526 | 2.000 |
| sd3 | 1 | INT8 | False | 14.804 | 2.464 |
| sd3 | 1 | FP8 | False | 14.838 | 2.571 |
| sd3 | 1 | NONE | False | 15.183 | 2.000 |
| sd3 | 1 | NONE | True | 15.183 | 2.003 |
| flux | 1 | FP8 | True | 15.997 | 8.994 |
| flux | 1 | FP8 | True | 15.998 | 9.067 |
| flux | 1 | INT8 | True | 15.999 | 8.435 |
| flux | 1 | INT8 | True | 15.999 | 8.420 |
| sd3 | 1 | NONE | False | 16.397 | 2.046 |
| sd3 | 1 | NONE | True | 16.403 | 2.053 |
| sd3 | 1 | NONE | True | 17.058 | 2.054 |
| sd3 | 1 | NONE | False | 17.058 | 2.051 |
| flux | 1 | FP8 | False | 20.393 | 8.963 |
| flux | 1 | INT8 | False | 20.395 | 8.372 |
| flux | 1 | INT8 | False | 22.270 | 8.400 |
| flux | 1 | FP8 | False | 22.271 | 9.013 |
| flux | 1 | NONE | False | 33.345 | 6.657 |
| flux | 1 | NONE | True | 33.345 | 6.672 |

## Table 1 (Sorted by Latency)

| Model Name | Batch Size | Quantization | Quantize TE | Memory (GB) | Latency (Seconds) |
| --- | --- | --- | --- | --- | --- |
| pixart | 1 | NONE | False | 10.560 | 1.142 |
| pixart | 1 | NONE | True | 10.560 | 1.142 |
| pixart | 1 | NONE | True | 10.214 | 1.151 |
| pixart | 1 | NONE | False | 10.214 | 1.152 |
| pixart | 1 | NONE | True | 12.435 | 1.170 |
| pixart | 1 | NONE | False | 12.433 | 1.172 |
| pixart | 1 | NONE | True | 12.086 | 1.181 |
| pixart | 1 | NONE | False | 12.086 | 1.182 |
| pixart | 1 | INT8 | False | 9.847 | 1.375 |
| pixart | 1 | FP8 | False | 9.847 | 1.397 |
| pixart | 1 | INT8 | False | 9.672 | 1.400 |
| pixart | 1 | INT8 | True | 5.537 | 1.403 |
| pixart | 1 | INT8 | True | 5.364 | 1.429 |
| pixart | 1 | FP8 | False | 9.672 | 1.434 |
| pixart | 1 | INT8 | False | 11.722 | 1.439 |
| pixart | 1 | FP8 | True | 5.537 | 1.450 |
| pixart | 1 | INT8 | True | 5.537 | 1.471 |
| pixart | 1 | FP8 | False | 11.722 | 1.472 |
| pixart | 1 | FP8 | True | 5.365 | 1.475 |
| pixart | 1 | INT8 | False | 11.547 | 1.494 |
| pixart | 1 | FP8 | True | 5.537 | 1.518 |
| pixart | 1 | FP8 | False | 11.547 | 1.520 |
| pixart | 1 | INT8 | True | 5.363 | 1.526 |
| pixart | 1 | FP8 | True | 5.364 | 1.587 |
| sd3 | 1 | NONE | False | 14.526 | 1.998 |
| sd3 | 1 | NONE | True | 14.526 | 2.000 |
| sd3 | 1 | NONE | False | 15.183 | 2.000 |
| sd3 | 1 | NONE | True | 15.183 | 2.003 |
| sd3 | 1 | NONE | False | 16.397 | 2.046 |
| sd3 | 1 | NONE | False | 17.058 | 2.051 |
| sd3 | 1 | NONE | True | 16.403 | 2.053 |
| sd3 | 1 | NONE | True | 17.058 | 2.054 |
| sd3 | 1 | INT8 | False | 12.929 | 2.458 |
| sd3 | 1 | INT8 | False | 14.804 | 2.464 |
| sd3 | 1 | INT8 | False | 12.598 | 2.475 |
| sd3 | 1 | INT8 | False | 14.473 | 2.499 |
| sd3 | 1 | INT8 | True | 7.963 | 2.517 |
| sd3 | 1 | INT8 | True | 7.963 | 2.527 |
| sd3 | 1 | INT8 | True | 7.628 | 2.531 |
| sd3 | 1 | INT8 | True | 7.625 | 2.553 |
| sd3 | 1 | FP8 | False | 14.838 | 2.571 |
| sd3 | 1 | FP8 | False | 12.926 | 2.574 |
| sd3 | 1 | FP8 | False | 12.598 | 2.598 |
| sd3 | 1 | FP8 | True | 7.963 | 2.628 |
| sd3 | 1 | FP8 | False | 14.469 | 2.630 |
| sd3 | 1 | FP8 | True | 7.968 | 2.637 |
| sd3 | 1 | FP8 | True | 7.628 | 2.659 |
| sd3 | 1 | FP8 | True | 7.630 | 2.682 |
| flux | 1 | NONE | False | 33.345 | 6.657 |
| flux | 1 | NONE | True | 33.345 | 6.672 |
| pixart | 1 | INT4 | False | 9.380 | 7.320 |
| pixart | 1 | INT4 | False | 9.491 | 7.340 |
| pixart | 1 | INT4 | True | 3.066 | 7.493 |
| pixart | 1 | INT4 | True | 3.176 | 7.512 |
| flux | 1 | INT8 | False | 20.395 | 8.372 |
| flux | 1 | INT8 | False | 22.270 | 8.400 |
| flux | 1 | INT8 | True | 15.999 | 8.420 |
| flux | 1 | INT8 | True | 15.999 | 8.435 |
| flux | 1 | FP8 | False | 20.393 | 8.963 |
| flux | 1 | FP8 | True | 15.997 | 8.994 |
| flux | 1 | FP8 | False | 22.271 | 9.013 |
| flux | 1 | FP8 | True | 15.998 | 9.067 |

## Table 2 (Sorted by Memory)

| Model Name | Batch Size | Quantization | Memory (GB) | Latency (Seconds) |
| --- | --- | --- | --- | --- |
| pixart | 1 | INT4 | 9.380 | 7.320 |
| pixart | 1 | INT4 | 9.491 | 7.340 |
| pixart | 1 | FP8 | 9.672 | 1.434 |
| pixart | 1 | INT8 | 9.672 | 1.400 |
| pixart | 1 | FP8 | 9.847 | 1.397 |
| pixart | 1 | INT8 | 9.847 | 1.375 |
| pixart | 1 | NONE | 10.214 | 1.152 |
| pixart | 1 | NONE | 10.560 | 1.142 |
| pixart | 1 | INT8 | 11.547 | 1.494 |
| pixart | 1 | FP8 | 11.547 | 1.520 |
| pixart | 1 | INT8 | 11.722 | 1.439 |
| pixart | 1 | FP8 | 11.722 | 1.472 |
| pixart | 1 | NONE | 12.086 | 1.182 |
| pixart | 1 | NONE | 12.433 | 1.172 |
| sd3 | 1 | INT8 | 12.598 | 2.475 |
| sd3 | 1 | FP8 | 12.598 | 2.598 |
| sd3 | 1 | FP8 | 12.926 | 2.574 |
| sd3 | 1 | INT8 | 12.929 | 2.458 |
| sd3 | 1 | FP8 | 14.469 | 2.630 |
| sd3 | 1 | INT8 | 14.473 | 2.499 |
| sd3 | 1 | NONE | 14.526 | 1.998 |
| sd3 | 1 | INT8 | 14.804 | 2.464 |
| sd3 | 1 | FP8 | 14.838 | 2.571 |
| sd3 | 1 | NONE | 15.183 | 2.000 |
| sd3 | 1 | NONE | 16.397 | 2.046 |
| sd3 | 1 | NONE | 17.058 | 2.051 |
| flux | 1 | FP8 | 20.393 | 8.963 |
| flux | 1 | INT8 | 20.395 | 8.372 |
| flux | 1 | INT8 | 22.270 | 8.400 |
| flux | 1 | FP8 | 22.271 | 9.013 |
| flux | 1 | NONE | 33.345 | 6.657 |

## Table 2 (Sorted by Latency)

| Model Name | Batch Size | Quantization | Memory (GB) | Latency (Seconds) |
| --- | --- | --- | --- | --- |
| pixart | 1 | NONE | 10.560 | 1.142 |
| pixart | 1 | NONE | 10.214 | 1.152 |
| pixart | 1 | NONE | 12.433 | 1.172 |
| pixart | 1 | NONE | 12.086 | 1.182 |
| pixart | 1 | INT8 | 9.847 | 1.375 |
| pixart | 1 | FP8 | 9.847 | 1.397 |
| pixart | 1 | INT8 | 9.672 | 1.400 |
| pixart | 1 | FP8 | 9.672 | 1.434 |
| pixart | 1 | INT8 | 11.722 | 1.439 |
| pixart | 1 | FP8 | 11.722 | 1.472 |
| pixart | 1 | INT8 | 11.547 | 1.494 |
| pixart | 1 | FP8 | 11.547 | 1.520 |
| sd3 | 1 | NONE | 14.526 | 1.998 |
| sd3 | 1 | NONE | 15.183 | 2.000 |
| sd3 | 1 | NONE | 16.397 | 2.046 |
| sd3 | 1 | NONE | 17.058 | 2.051 |
| sd3 | 1 | INT8 | 12.929 | 2.458 |
| sd3 | 1 | INT8 | 14.804 | 2.464 |
| sd3 | 1 | INT8 | 12.598 | 2.475 |
| sd3 | 1 | INT8 | 14.473 | 2.499 |
| sd3 | 1 | FP8 | 14.838 | 2.571 |
| sd3 | 1 | FP8 | 12.926 | 2.574 |
| sd3 | 1 | FP8 | 12.598 | 2.598 |
| sd3 | 1 | FP8 | 14.469 | 2.630 |
| flux | 1 | NONE | 33.345 | 6.657 |
| pixart | 1 | INT4 | 9.380 | 7.320 |
| pixart | 1 | INT4 | 9.491 | 7.340 |
| flux | 1 | INT8 | 20.395 | 8.372 |
| flux | 1 | INT8 | 22.270 | 8.400 |
| flux | 1 | FP8 | 20.393 | 8.963 |
| flux | 1 | FP8 | 22.271 | 9.013 |

## Table 3 (Sorted by Memory)

| Model Name | Batch Size | Quantization | Quantize TE 1 | Quantize TE 2 | Quantize TE 3 | Memory (GB) | Latency (Seconds) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| pixart | 1 | INT4 | 1 | 1 | 1 | 3.066 | 7.493 |
| pixart | 1 | INT4 | 1 | 1 | 1 | 3.176 | 7.512 |
| pixart | 1 | INT8 | 1 | 1 | 1 | 5.363 | 1.526 |
| pixart | 1 | INT8 | 1 | 1 | 1 | 5.364 | 1.429 |
| pixart | 1 | FP8 | 1 | 1 | 1 | 5.364 | 1.587 |
| pixart | 1 | FP8 | 1 | 1 | 1 | 5.365 | 1.475 |
| pixart | 1 | INT8 | 1 | 1 | 1 | 5.537 | 1.471 |
| pixart | 1 | FP8 | 1 | 1 | 1 | 5.537 | 1.518 |
| pixart | 1 | FP8 | 1 | 1 | 1 | 5.537 | 1.450 |
| pixart | 1 | INT8 | 1 | 1 | 1 | 5.537 | 1.403 |
| sd3 | 1 | INT8 | 1 | 1 | 1 | 7.625 | 2.553 |
| sd3 | 1 | FP8 | 1 | 1 | 1 | 7.628 | 2.659 |
| sd3 | 1 | INT8 | 1 | 1 | 1 | 7.628 | 2.531 |
| sd3 | 1 | FP8 | 1 | 1 | 1 | 7.630 | 2.682 |
| sd3 | 1 | INT8 | 1 | 1 | 1 | 7.963 | 2.527 |
| sd3 | 1 | INT8 | 1 | 1 | 1 | 7.963 | 2.517 |
| sd3 | 1 | FP8 | 1 | 1 | 1 | 7.963 | 2.628 |
| sd3 | 1 | FP8 | 1 | 1 | 1 | 7.968 | 2.637 |
| pixart | 1 | INT4 | 0 | 0 | 0 | 9.380 | 7.320 |
| pixart | 1 | INT4 | 0 | 0 | 0 | 9.491 | 7.340 |
| pixart | 1 | FP8 | 0 | 0 | 0 | 9.672 | 1.434 |
| pixart | 1 | INT8 | 0 | 0 | 0 | 9.672 | 1.400 |
| pixart | 1 | FP8 | 0 | 0 | 0 | 9.847 | 1.397 |
| pixart | 1 | INT8 | 0 | 0 | 0 | 9.847 | 1.375 |
| pixart | 1 | NONE | 0 | 0 | 0 | 10.214 | 1.152 |
| pixart | 1 | NONE | 1 | 1 | 1 | 10.214 | 1.151 |
| pixart | 1 | NONE | 0 | 0 | 0 | 10.560 | 1.142 |
| pixart | 1 | NONE | 1 | 1 | 1 | 10.560 | 1.142 |
| pixart | 1 | INT8 | 0 | 0 | 0 | 11.547 | 1.494 |
| pixart | 1 | FP8 | 0 | 0 | 0 | 11.547 | 1.520 |
| pixart | 1 | INT8 | 0 | 0 | 0 | 11.722 | 1.439 |
| pixart | 1 | FP8 | 0 | 0 | 0 | 11.722 | 1.472 |
| pixart | 1 | NONE | 0 | 0 | 0 | 12.086 | 1.182 |
| pixart | 1 | NONE | 1 | 1 | 1 | 12.086 | 1.181 |
| pixart | 1 | NONE | 0 | 0 | 0 | 12.433 | 1.172 |
| pixart | 1 | NONE | 1 | 1 | 1 | 12.435 | 1.170 |
| sd3 | 1 | INT8 | 0 | 0 | 0 | 12.598 | 2.475 |
| sd3 | 1 | FP8 | 0 | 0 | 0 | 12.598 | 2.598 |
| sd3 | 1 | FP8 | 0 | 0 | 0 | 12.926 | 2.574 |
| sd3 | 1 | INT8 | 0 | 0 | 0 | 12.929 | 2.458 |
| sd3 | 1 | FP8 | 0 | 0 | 0 | 14.469 | 2.630 |
| sd3 | 1 | INT8 | 0 | 0 | 0 | 14.473 | 2.499 |
| sd3 | 1 | NONE | 0 | 0 | 0 | 14.526 | 1.998 |
| sd3 | 1 | NONE | 1 | 1 | 1 | 14.526 | 2.000 |
| sd3 | 1 | INT8 | 0 | 0 | 0 | 14.804 | 2.464 |
| sd3 | 1 | FP8 | 0 | 0 | 0 | 14.838 | 2.571 |
| sd3 | 1 | NONE | 0 | 0 | 0 | 15.183 | 2.000 |
| sd3 | 1 | NONE | 1 | 1 | 1 | 15.183 | 2.003 |
| flux | 1 | FP8 | 1 | 1 | 1 | 15.997 | 8.994 |
| flux | 1 | FP8 | 1 | 1 | 1 | 15.998 | 9.067 |
| flux | 1 | INT8 | 1 | 1 | 1 | 15.999 | 8.435 |
| flux | 1 | INT8 | 1 | 1 | 1 | 15.999 | 8.420 |
| sd3 | 1 | NONE | 0 | 0 | 0 | 16.397 | 2.046 |
| sd3 | 1 | NONE | 1 | 1 | 1 | 16.403 | 2.053 |
| sd3 | 1 | NONE | 1 | 1 | 1 | 17.058 | 2.054 |
| sd3 | 1 | NONE | 0 | 0 | 0 | 17.058 | 2.051 |
| flux | 1 | FP8 | 0 | 0 | 0 | 20.393 | 8.963 |
| flux | 1 | INT8 | 0 | 0 | 0 | 20.395 | 8.372 |
| flux | 1 | INT8 | 0 | 0 | 0 | 22.270 | 8.400 |
| flux | 1 | FP8 | 0 | 0 | 0 | 22.271 | 9.013 |
| flux | 1 | NONE | 0 | 0 | 0 | 33.345 | 6.657 |
| flux | 1 | NONE | 1 | 1 | 1 | 33.345 | 6.672 |

## Table 3 (Sorted by Latency)

| Model Name | Batch Size | Quantization | Quantize TE 1 | Quantize TE 2 | Quantize TE 3 | Memory (GB) | Latency (Seconds) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| pixart | 1 | NONE | 0 | 0 | 0 | 10.560 | 1.142 |
| pixart | 1 | NONE | 1 | 1 | 1 | 10.560 | 1.142 |
| pixart | 1 | NONE | 1 | 1 | 1 | 10.214 | 1.151 |
| pixart | 1 | NONE | 0 | 0 | 0 | 10.214 | 1.152 |
| pixart | 1 | NONE | 1 | 1 | 1 | 12.435 | 1.170 |
| pixart | 1 | NONE | 0 | 0 | 0 | 12.433 | 1.172 |
| pixart | 1 | NONE | 1 | 1 | 1 | 12.086 | 1.181 |
| pixart | 1 | NONE | 0 | 0 | 0 | 12.086 | 1.182 |
| pixart | 1 | INT8 | 0 | 0 | 0 | 9.847 | 1.375 |
| pixart | 1 | FP8 | 0 | 0 | 0 | 9.847 | 1.397 |
| pixart | 1 | INT8 | 0 | 0 | 0 | 9.672 | 1.400 |
| pixart | 1 | INT8 | 1 | 1 | 1 | 5.537 | 1.403 |
| pixart | 1 | INT8 | 1 | 1 | 1 | 5.364 | 1.429 |
| pixart | 1 | FP8 | 0 | 0 | 0 | 9.672 | 1.434 |
| pixart | 1 | INT8 | 0 | 0 | 0 | 11.722 | 1.439 |
| pixart | 1 | FP8 | 1 | 1 | 1 | 5.537 | 1.450 |
| pixart | 1 | INT8 | 1 | 1 | 1 | 5.537 | 1.471 |
| pixart | 1 | FP8 | 0 | 0 | 0 | 11.722 | 1.472 |
| pixart | 1 | FP8 | 1 | 1 | 1 | 5.365 | 1.475 |
| pixart | 1 | INT8 | 0 | 0 | 0 | 11.547 | 1.494 |
| pixart | 1 | FP8 | 1 | 1 | 1 | 5.537 | 1.518 |
| pixart | 1 | FP8 | 0 | 0 | 0 | 11.547 | 1.520 |
| pixart | 1 | INT8 | 1 | 1 | 1 | 5.363 | 1.526 |
| pixart | 1 | FP8 | 1 | 1 | 1 | 5.364 | 1.587 |
| sd3 | 1 | NONE | 0 | 0 | 0 | 14.526 | 1.998 |
| sd3 | 1 | NONE | 1 | 1 | 1 | 14.526 | 2.000 |
| sd3 | 1 | NONE | 0 | 0 | 0 | 15.183 | 2.000 |
| sd3 | 1 | NONE | 1 | 1 | 1 | 15.183 | 2.003 |
| sd3 | 1 | NONE | 0 | 0 | 0 | 16.397 | 2.046 |
| sd3 | 1 | NONE | 0 | 0 | 0 | 17.058 | 2.051 |
| sd3 | 1 | NONE | 1 | 1 | 1 | 16.403 | 2.053 |
| sd3 | 1 | NONE | 1 | 1 | 1 | 17.058 | 2.054 |
| sd3 | 1 | INT8 | 0 | 0 | 0 | 12.929 | 2.458 |
| sd3 | 1 | INT8 | 0 | 0 | 0 | 14.804 | 2.464 |
| sd3 | 1 | INT8 | 0 | 0 | 0 | 12.598 | 2.475 |
| sd3 | 1 | INT8 | 0 | 0 | 0 | 14.473 | 2.499 |
| sd3 | 1 | INT8 | 1 | 1 | 1 | 7.963 | 2.517 |
| sd3 | 1 | INT8 | 1 | 1 | 1 | 7.963 | 2.527 |
| sd3 | 1 | INT8 | 1 | 1 | 1 | 7.628 | 2.531 |
| sd3 | 1 | INT8 | 1 | 1 | 1 | 7.625 | 2.553 |
| sd3 | 1 | FP8 | 0 | 0 | 0 | 14.838 | 2.571 |
| sd3 | 1 | FP8 | 0 | 0 | 0 | 12.926 | 2.574 |
| sd3 | 1 | FP8 | 0 | 0 | 0 | 12.598 | 2.598 |
| sd3 | 1 | FP8 | 1 | 1 | 1 | 7.963 | 2.628 |
| sd3 | 1 | FP8 | 0 | 0 | 0 | 14.469 | 2.630 |
| sd3 | 1 | FP8 | 1 | 1 | 1 | 7.968 | 2.637 |
| sd3 | 1 | FP8 | 1 | 1 | 1 | 7.628 | 2.659 |
| sd3 | 1 | FP8 | 1 | 1 | 1 | 7.630 | 2.682 |
| flux | 1 | NONE | 0 | 0 | 0 | 33.345 | 6.657 |
| flux | 1 | NONE | 1 | 1 | 1 | 33.345 | 6.672 |
| pixart | 1 | INT4 | 0 | 0 | 0 | 9.380 | 7.320 |
| pixart | 1 | INT4 | 0 | 0 | 0 | 9.491 | 7.340 |
| pixart | 1 | INT4 | 1 | 1 | 1 | 3.066 | 7.493 |
| pixart | 1 | INT4 | 1 | 1 | 1 | 3.176 | 7.512 |
| flux | 1 | INT8 | 0 | 0 | 0 | 20.395 | 8.372 |
| flux | 1 | INT8 | 0 | 0 | 0 | 22.270 | 8.400 |
| flux | 1 | INT8 | 1 | 1 | 1 | 15.999 | 8.420 |
| flux | 1 | INT8 | 1 | 1 | 1 | 15.999 | 8.435 |
| flux | 1 | FP8 | 0 | 0 | 0 | 20.393 | 8.963 |
| flux | 1 | FP8 | 1 | 1 | 1 | 15.997 | 8.994 |
| flux | 1 | FP8 | 0 | 0 | 0 | 22.271 | 9.013 |
| flux | 1 | FP8 | 1 | 1 | 1 | 15.998 | 9.067 |

