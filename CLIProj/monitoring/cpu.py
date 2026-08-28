#####################################################

### monitoring/cpu.py
### Author: Aiden Lico
### Date: 28/08/2026
### Last Updated: 28/08/2026

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

