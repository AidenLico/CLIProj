#####################################################

### monitoring/cpu.py
### Author: Aiden Lico
### Date: 28/08/2026
### Last Updated: 31/08/2026

#####################################################

## Imports

import psutil

## Testing functions

# print(psutil.cpu_percent(interval=1))
## Determines the CPU Percentage over the last second interval (avg of all cores)
# print(psutil.cpu_percent(interval=1, percpu=True))
## Breaks down CPU per core (includes logi cores)
# print(psutil.cpu_count(logical=False))
## Physical core count
# print(psutil.cpu_count(logical=True))
## Phys and logi core count
# print(psutil.cpu_freq())
## curr cpu req, min report freq and max reported freq
# print(psutil.cpu_stats())
# print(psutil.cpu_freq())
# print(psutil.cpu_times())

## Functions

# # Returns cpu usage based on interval amount (seconds)
# def cpu_usage(intervalAmount):
#     return psutil.cpu_percent(interval=intervalAmount)
# # Returns cpu usage per cpu core based on interval amount
# def cpu_usage_pcore(intervalAmount):
#     return psutil.cpu_percent(interval=intervalAmount, percpu=True)
# # Returns cpu count (can be logi and phys or just phys)
# def cpu_cores(logicalTF):
#     return psutil.cpu_count(logical=logicalTF)
# # Returns cpu freq stats
# def cpu_freq():
#     return psutil.cpu_freq()

## updated function returns values as a library
def get_cpu_metrics(intervalAmount):
    return {
        "usage": psutil.cpu_percent(interval=intervalAmount),
        "per_core": psutil.cpu_percent(interval=intervalAmount, percpu=True),
        "physical": psutil.cpu_count(logical=False),
        "logical": psutil.cpu_count(logical=True),
        "freq": psutil.cpu_freq()
    }
